from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database import db
from models import Make, Model, Engine, Listing, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql.expression import func
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pycars.db'
app.config['SECRET_KEY'] = 'cheie-secreta-foarte-sigura'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    marci = Make.query.order_by(Make.name).all()
    random_listings = Listing.query.order_by(func.random()).limit(6).all()
    return render_template('index.html', marci=marci, listings=random_listings)

@app.route('/cautare')
def search():
    query = Listing.query.join(Engine).join(Model).join(Make)

    marca = request.args.get('make')
    if marca and marca != 'Toate':
        query = query.filter(Make.name == marca)

    model = request.args.get('model')
    if model:
        query = query.filter(Model.name.ilike(f"%{model}%"))

    min_price = request.args.get('min_price')
    if min_price:
        query = query.filter(Listing.price >= int(min_price))
    
    max_price = request.args.get('max_price')
    if max_price:
        query = query.filter(Listing.price <= int(max_price))

    min_year = request.args.get('min_year')
    if min_year:
        query = query.filter(Listing.year >= int(min_year))
    
    max_year = request.args.get('max_year')
    if max_year:
        query = query.filter(Listing.year <= int(max_year))

    fuel = request.args.get('fuel_type')
    if fuel and fuel != 'Toate':
        query = query.filter(Engine.fuel_type == fuel)

    min_hp = request.args.get('min_hp')
    if min_hp:
        query = query.filter(Engine.power_hp >= int(min_hp))

    sort_by = request.args.get('sort')
    if sort_by == 'price_asc':
        query = query.order_by(Listing.price.asc())
    elif sort_by == 'price_desc':
        query = query.order_by(Listing.price.desc())
    elif sort_by == 'newest':
        query = query.order_by(Listing.created_at.desc())
    elif sort_by == 'mileage_asc':
        query = query.order_by(Listing.mileage.asc())

    results = query.all()
    marci = Make.query.order_by(Make.name).all()
    
    return render_template('results.html', listings=results, marci=marci)

@app.route('/anunt/<int:listing_id>')
def listing_detail(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return render_template('listing_detail.html', listing=listing)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        nume = request.form.get('nume')
        telefon = request.form.get('telefon')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email-ul există deja!', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            email=email,
            name=nume,
            phone=telefon,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256')
        )
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Email sau parolă incorectă.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/postare', methods=['GET', 'POST'])
@login_required
def create_listing():
    if request.method == 'POST':
        flash('Anunțul a fost postat cu succes!', 'success')
        return redirect(url_for('home'))

    marci = Make.query.order_by(Make.name).all()
    return render_template('add_listing.html', marci=marci)

@app.route('/api/models/<int:make_id>')
def get_models(make_id):
    models = Model.query.filter_by(make_id=make_id).all()
    models_list = [{'id': m.id, 'name': m.name} for m in models]
    return jsonify({'models': models_list})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)