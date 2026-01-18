from database import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password_hash = db.Column(db.String(200), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(20))

    # A user can have multiple listings
    listings = db.relationship('Listing', backref = 'owner', lazy = True)

class Make(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, unique = True)  # e.g., Skoda
    models = db.relationship('Model', backref = 'make', lazy = True)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)  # e.g., Octavia
    make_id = db.Column(db.Integer, db.ForeignKey('make.id'), nullable = False)
    engines = db.relationship('Engine', backref = 'model', lazy = True)

class Engine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)  # e.g., 2.0 TDI
    power_hp = db.Column(db.Integer)  # e.g., 150 HP
    displacement_cc = db.Column(db.Integer)  # e.g., 1968 cm3
    fuel_type = db.Column(db.String(30))  # e.g., Diesel
    euro_norm = db.Column(db.String(10))  # e.g., Euro 6
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable = False)
    listings = db.relationship('Listing', backref = 'engine', lazy = True)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    mileage = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text)
    phone = db.Column(db.String(20))  # Contact phone for this specific listing
    image_list = db.Column(db.String(500))  # Filename of the main image
    gearbox_type = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    # Relationships
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)