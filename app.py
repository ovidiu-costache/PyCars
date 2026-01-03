import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy.sql.expression import func

# Importam db si modelele din fisierele tale
from database import db
from models import Make, Model, Engine, Listing, User

app = Flask(__name__)

# --- CONFIGURARI ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pycars.db'
app.config['SECRET_KEY'] = 'cheie-super-secreta-pentru-sesiune'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initializam baza de date cu aplicatia
db.init_app(app)

# --- CONFIGURARE LOGIN MANAGER ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Daca nu esti logat, te trimite aici


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- RUTE PRINCIPALE ---

@app.route('/', methods = ['GET'])
def home():
    marci = Make.query.all()
    modele = Model.query.all()

    # Luam tipurile de combustibil unice
    combustibili = db.session.query(Engine.fuel_type).distinct().all()
    lista_combustibili = [c[0] for c in combustibili]

    # 4 anunturi random pentru prima pagina
    anunturi_random = Listing.query.order_by(func.random()).limit(4).all()

    return render_template('index.html',
                           marci = marci,
                           modele = modele,
                           combustibili = lista_combustibili,
                           anunturi = anunturi_random,
                           user = current_user)


@app.route('/cautare', methods = ['GET'])
def cautare():
    # Preluam parametrii din URL
    marca_id = request.args.get('marca')
    model_id = request.args.get('model')
    combustibil = request.args.get('combustibil')

    pret_min = request.args.get('pret_min')
    pret_max = request.args.get('pret_max')

    an_min = request.args.get('an_min')
    an_max = request.args.get('an_max')

    km_min = request.args.get('km_min')
    km_max = request.args.get('km_max')

    # Incepem query-ul de baza (join intre tabele)
    query = Listing.query.join(Engine).join(Model).join(Make)

    # --- FILTRARE ---
    # CORECTIE IMPORTANTA: Folosim marca_id aici, nu model_id!
    if marca_id and marca_id != "0":
        query = query.filter(Make.id == int(marca_id))

    if model_id and model_id != '0':
        query = query.filter(Model.id == int(model_id))

    if combustibil and combustibil != '0':
        query = query.filter(Engine.fuel_type == combustibil)

    if pret_min and pret_min != '':
        query = query.filter(Listing.price >= int(pret_min))
    if pret_max and pret_max != '':
        query = query.filter(Listing.price <= int(pret_max))

    if an_min and an_min != '':
        query = query.filter(Listing.year >= int(an_min))
    if an_max and an_max != '':
        query = query.filter(Listing.year <= int(an_max))

    if km_min and km_min != '':
        query = query.filter(Listing.mileage >= int(km_min))
    if km_max and km_max != '':
        query = query.filter(Listing.mileage <= int(km_max))

    # --- SORTARE ---
    sortare = request.args.get('sortare')
    if sortare == 'pret_cresc':
        query = query.order_by(Listing.price.asc())
    elif sortare == 'pret_desc':
        query = query.order_by(Listing.price.desc())
    elif sortare == 'km_cresc':
        query = query.order_by(Listing.mileage.asc())
    elif sortare == 'an_desc':
        query = query.order_by(Listing.year.desc())
    elif sortare == 'an_cresc':
        query = query.order_by(Listing.year.asc())

    rezultate = query.all()
    return render_template('rezultate.html', anunturi = rezultate, user = current_user)


@app.route('/anunt/<int:id>')
def detalii_anunt(id):
    anunt = Listing.query.get_or_404(id)
    return render_template('detalii.html', anunt = anunt, user = current_user)


@app.route('/sterge/<int:id>')
@login_required
def sterge_anunt(id):
    anunt_de_sters = Listing.query.get_or_404(id)

    # Verificam daca anuntul apartine userului logat
    if anunt_de_sters.user_id != current_user.id:
        flash('Nu ai dreptul să ștergi acest anunț!', 'error')
        return redirect(url_for('profil'))

    # Stergem si fisierul fizic (poza)
    if anunt_de_sters.image_list:
        try:
            cale_poza = os.path.join(app.config['UPLOAD_FOLDER'], anunt_de_sters.image_list)
            if os.path.exists(cale_poza):
                os.remove(cale_poza)
        except:
            pass

    db.session.delete(anunt_de_sters)
    db.session.commit()

    flash('Anunțul a fost șters cu succes.', 'success')
    return redirect(url_for('profil'))


# --- RUTE AUTH (LOGIN / REGISTER) ---

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        parola = request.form.get('password')

        user = User.query.filter_by(email = email).first()

        if user and check_password_hash(user.password_hash, parola):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Email sau parola incorecte!', 'error')

    return render_template('login.html', user = current_user)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        nume = request.form.get('name')
        email = request.form.get('email')
        parola = request.form.get('password')

        # Validare simpla email
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            flash('Format email incorect!', 'error')
            return redirect(url_for('register'))

        user_existent = User.query.filter_by(email = email).first()
        if user_existent:
            flash('Acest email este deja folosit!', 'error')
            return redirect(url_for('register'))

        parola_hash = generate_password_hash(parola, method = 'pbkdf2:sha256')

        new_user = User(
            email = email,
            name = nume,
            password_hash = parola_hash
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Cont creat cu succes! Acum te poți autentifica.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', user = current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# --- RUTE USER (ADAUGA / PROFIL) ---

@app.route('/adauga', methods = ['GET', 'POST'])
@login_required
def adauga_anunt():
    if request.method == 'POST':
        try:
            titlu = request.form.get('titlu')
            pret = request.form.get('pret')
            an = request.form.get('an')
            km = request.form.get('km')
            descriere = request.form.get('descriere')
            telefon = request.form.get('telefon')
            cutie = request.form.get('cutie')
            motor_id = request.form.get('motor_id')

            nume_poza = None

            if 'poza' in request.files:
                file = request.files['poza']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    # Ne asiguram ca folderul exista
                    if not os.path.exists(app.config['UPLOAD_FOLDER']):
                        os.makedirs(app.config['UPLOAD_FOLDER'])

                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    nume_poza = filename

            new_listing = Listing(
                title = titlu,
                price = int(pret),
                year = int(an),
                mileage = int(km),
                description = descriere,
                phone = telefon,
                gearbox_type = cutie,
                image_list = nume_poza,
                engine_id = int(motor_id),
                user_id = current_user.id
            )

            db.session.add(new_listing)
            db.session.commit()

            flash('Anunțul a fost adăugat cu succes!', 'success')
            return redirect(url_for('profil'))

        except Exception as e:
            flash(f'A apărut o eroare: {str(e)}', 'error')
            return redirect(url_for('adauga_anunt'))

    motoare_disponibile = Engine.query.all()
    return render_template('adauga.html', motoare = motoare_disponibile, user = current_user)


@app.route('/profil')
@login_required
def profil():
    anunturile_mele = Listing.query.filter_by(user_id = current_user.id).all()
    return render_template('profil.html', anunturi = anunturile_mele, user = current_user)


# --- PORNIRE APLICATIE ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)