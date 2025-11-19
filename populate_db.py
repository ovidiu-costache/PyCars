from app import app
from database import db
from models import Make, Model, Engine, Listing

def seed():
    with app.app_context():
        # Sterg datele vechi in oridne inversa pt a nu da crash
        db.session.query(Listing).delete()
        db.session.query(Engine).delete()
        db.session.query(Model).delete()
        db.session.query(Make).delete()

        skoda = Make(name="Skoda")
        db.session.add(skoda)
        models_skoda = ["Octavia", "Superb", "Kodiaq", "Scala", "Fabia", "Karoq", "Kamiq"]
        for m in models_skoda:
            db.session.add(Model(name=m, make=skoda))

        vw = Make(name="Volkswagen")
        db.session.add(vw)
        models_vw = ["Passat", "Golf", "Touareg", "Tiguan", "Arteon", "Polo", "T-Roc", "T-Cross", "Taigo", "Jetta", "Bora", "Caddy", "Passat CC", "Touran", "Sharan"]
        for m in models_vw:
            db.session.add(Model(name=m, make=vw))

        bmw = Make(name="BMW")
        db.session.add(bmw)
        models_bmw = ["Seria 1", "Seria 2", "Seria 3", "Seria 4", "Seria 5", "Seria 6", "Seria 7", "Seria 8", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "X1", "X2", "X3", "X4", "X5", "X6", "X7"]
        for m in models_bmw:
            db.session.add(Model(name=m, make=bmw))

        audi = Make(name="Audi")
        db.session.add(audi)
        models_audi = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "RS2", "RS3", "RS4", "RS5", "RS6", "RS7", "TT", "TT S"]
        for m in models_audi:
            db.session.add(Model(name=m, make=audi))

        reno = Make(name="Renault")
        db.session.add(reno)
        models_reno = ["Megane", "Talisman", "Clio", "Kadjar", "Captur", "Arkana", "Laguna", "Koleos", "Symbol", "Scenic", "Rafale", "Austral", "Master"]
        for m in models_reno:
            db.session.add(Model(name=m, make=reno))

        merc = Make(name="Mercedes")
        db.session.add(merc)
        models_merc = ["A-Class", "B-Class", "C-Class", "E-Class", "S-Class", "G-Class", "CLA", "CLE", "CLK", "CLS", "GLA", "GLB", "GLC", "GLE", "GLK", "GLS", "ML", "Sprinter", "Vito", "V-Class", "AMG GT"]
        for m in models_merc:
            db.session.add(Model(name=m, make=merc))

        dacia = Make(name="Dacia")
        db.session.add(dacia)
        models_dacia = ["Logan", "Duster", "Sandero", "Bigster", "Docker", "Jogger", "Lodgy", "Spring"]
        for m in models_dacia:
            db.session.add(Model(name=m, make=dacia))
            
        alfa = Make(name="Alfa Romeo")
        db.session.add(alfa)
        models_alfa = ["Giulia", "Giullietta", "Stelvio", "159"]
        for m in models_alfa:
            db.session.add(Model(name=m, make=dacia))

        db.session.commit()
        print("Baza de date updatata")

if __name__ == '__main__':
    seed()
