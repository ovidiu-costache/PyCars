from database import db 

class Make(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, unique = True) # ex: Skoda

    # A make has more models
    models = db.relationship('Model', backref = 'make', lazy = True)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False) # ex: Octavia

    make_id = db.Column(db.Integer, db.ForeignKey('make.id'), nullable = False)

    # A model has more types of engines
    engines = db.relationship('Engine', backref = 'model', lazy = True)

class Engine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False) # ex: 2.0 TDI
    power_hp = db.Column(db.Integer) # ex: 150 HP
    displacement_cc = db.Column(db.Integer) # ex: 1968 cm3
    fuel_type = db.Column(db.String(30)) # ex: Diesel
    euro_norm = db.Column(db.String(10)) # ex: Euro 6

    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable = False)

    # An engine could be seen in more announcements
    listings = db.relationship('Listing', backref = 'engine', lazy = True)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer, nullable = False)
    mileage = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text)
    phone = db.Column(db.String(20))
    image_list = db.Column(db.String(500)) # ex: poza1.png

    gearbox_type = db.Column(db.String(20)) # ex: Automata

    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'), nullable = False)