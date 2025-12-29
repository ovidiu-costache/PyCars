from app import app
from database import db
from models import Make, Model, Engine, Listing, User
from werkzeug.security import generate_password_hash

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        admin_user = User(
            email = "admin@pycars.ro",
            password_hash = generate_password_hash("admin123", method = 'pbkdf2:sha256'),
            name = "Admin PyCars",
            phone = "0729379058"
        )

        db.session.add(admin_user)
        db.session.commit()

        skoda = Make(name = "Skoda")
        db.session.add(skoda)
        models_skoda = ["Octavia", "Superb", "Kodiaq", "Scala", "Fabia", "Karoq", "Kamiq"]
        for m in models_skoda:
            db.session.add(Model(name = m, make = skoda))

        vw = Make(name = "Volkswagen")
        db.session.add(vw)
        models_vw = ["Passat", "Golf", "Touareg", "Tiguan", "Arteon", "Polo", "T-Roc", "T-Cross", "Taigo", "Jetta", "Bora", "Caddy", "Passat CC", "Touran", "Sharan"]
        for m in models_vw:
            db.session.add(Model(name = m, make = vw))

        bmw = Make(name = "BMW")
        db.session.add(bmw)
        models_bmw = ["Seria 1", "Seria 2", "Seria 3", "Seria 4", "Seria 5", "Seria 6", "Seria 7", "Seria 8", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "X1", "X2", "X3", "X4", "X5", "X6", "X7"]
        for m in models_bmw:
            db.session.add(Model(name = m, make = bmw))

        audi = Make(name = "Audi")
        db.session.add(audi)
        models_audi = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "RS2", "RS3", "RS4", "RS5", "RS6", "RS7", "TT", "TT S"]
        for m in models_audi:
            db.session.add(Model(name = m, make = audi))

        reno = Make(name = "Renault")
        db.session.add(reno)
        models_reno = ["Megane", "Talisman", "Clio", "Kadjar", "Captur", "Arkana", "Laguna", "Koleos", "Symbol", "Scenic", "Rafale", "Austral", "Master"]
        for m in models_reno:
            db.session.add(Model(name = m, make = reno))

        merc = Make(name = "Mercedes")
        db.session.add(merc)
        models_merc = ["A-Class", "B-Class", "C-Class", "E-Class", "S-Class", "G-Class", "CLA", "CLE", "CLK", "CLS", "GLA", "GLB", "GLC", "GLE", "GLK", "GLS", "ML", "Sprinter", "Vito", "V-Class", "AMG GT"]
        for m in models_merc:
            db.session.add(Model(name = m, make = merc))

        dacia = Make(name = "Dacia")
        db.session.add(dacia)
        models_dacia = ["Logan", "Duster", "Sandero", "Bigster", "Docker", "Jogger", "Lodgy", "Spring", "Solenza", "Supernova", "1310"]
        for m in models_dacia:
            db.session.add(Model(name = m, make = dacia))
            
        alfa = Make(name = "Alfa Romeo")
        db.session.add(alfa)
        models_alfa = ["Giulia", "Giullietta", "Stelvio", "159"]
        for m in models_alfa:
            db.session.add(Model(name = m, make = alfa))

        citroen = Make(name = "Citroen")
        db.session.add(citroen)
        models_citroen = ["C3", "C4", "C4 Cactus", "C5", "DS3", "DS4", "DS5"]
        for m in models_citroen:
            db.session.add(Model(name = m, make = citroen))

        ford = Make(name = "Ford")
        db.session.add(ford)
        models_ford = ["Focus", "Mondeo", "Fiesta", "Kuga", "C-MAX", "Mustang", "Puma", "Transit"]
        for m in models_ford:
            db.session.add(Model(name = m, make = ford))

        honda = Make(name = "Honda")
        db.session.add(honda)
        models_honda = ["Accord", "Civic", "CR-V", "HR-V"]
        for m in models_honda:
            db.session.add(Model(name = m, make = honda))

        hyundai = Make(name = "Hyundai")
        db.session.add(hyundai)
        models_hyundai = ["Elantra", "i10", "i20", "i30", "i40", "IONIQ", "Konda", "Santa Fe", "Tucson"]
        for m in models_hyundai:
            db.session.add(Model(name = m, make = hyundai))

        mazda = Make(name = "Mazda")
        db.session.add(mazda)
        models_mazda = ["2", "3", "5", "6", "CX-3", "CX-30", "CX-5", "CX-60", "CX-7", "CX-80", "MX-5", "Miata"]
        for m in models_mazda:
            db.session.add(Model(name = m, make = mazda))

        nissan = Make(name = "Nissan")
        db.session.add(nissan)
        models_nissan = ["Qashqai", "Juke", "X-TRAIL", "Patrol", "Micra", "GT-R"]
        for m in models_nissan:
            db.session.add(Model(name = m, make = nissan))

        opel = Make(name = "Opel")
        db.session.add(opel)
        models_opel = ["Antara", "Astra", "Insigna", "Corsa", "Crossland", "Grandland", "GrandlandX", "Mokka", "Vectra", "Vivaro", "Zafira"]
        for m in models_opel:
            db.session.add(Model(name = m, make = opel))

        seat = Make(name = "Seat")
        db.session.add(seat)
        models_seat = ["Leon", "Ibiza", "Alhambra", "Altea", "Arona", "Ateca", "Exeo", "Tarraco", "Toledo"]
        for m in models_seat:
            db.session.add(Model(name = m, make = seat))

        peugeot = Make(name = "Peugeot")
        db.session.add(peugeot)
        models_peugeot = ["207", "208", "2008", "301", "307", "308", "3008", "407", "408", "4007", "4008", "508", "5008", "Partner"]
        for m in models_peugeot:
            db.session.add(Model(name = m, make = peugeot))

        porsche = Make(name = "Porsche")
        db.session.add(porsche)
        models_porsche = ["Boxter", "Cayenne", "Cayenne Coupe", "Cayman", "Macan", "Panamera", "Taycan", "911", "911-TURBO-S"]
        for m in models_porsche:
            db.session.add(Model(name = m, make = porsche))

        suzuki = Make(name = "Suzuki")
        db.session.add(suzuki)
        models_suzuki = ["Grand Vitara", "Jimny", "Swace", "Swift", "S-Cross", "SX4", "Vitara"]
        for m in models_suzuki:
            db.session.add(Model(name = m, make = suzuki))

        toyota = Make(name = "Toyota")
        db.session.add(toyota)
        models_toyota = ["Avensis", "Aygo", "C-HR", "Camry", "Corolla", "Corolla Cross", "Highlander", "Hilux", "Land Cruiser", "Prius", "Proace", "RAV4", "Yaris", "Yaris Cross"]
        for m in models_toyota:
            db.session.add(Model(name = m, make = toyota))

        volvo = Make(name = "Volvo")
        db.session.add(volvo)
        models_volvo = ["S40", "S60", "S80", "S90", "V40", "V50", "V60", "V70", "V90", "XC40", "XC60", "XC70", "XC90"]
        for m in models_volvo:
            db.session.add(Model(name = m, make = volvo))

        db.session.commit()

        octavia = Model.query.filter_by(name = "Octavia").first()
        if octavia:
            # Octavia 4
            eng_oct_1 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_2 = Engine(name = "2.0 TDI", power_hp = 115, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_3 = Engine(name = "2.0 TDI", power_hp = 200, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_4 = Engine(name = "2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_5 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_6 = Engine(name = "1.5 TSI mHEV", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = octavia)
            eng_oct_7 = Engine(name = "1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_8 = Engine(name = "1.4 TSI iV", power_hp = 204, displacement_cc = 1395, fuel_type = "Hybrid", euro_norm = "Euro 6", model = octavia)

            # Octavia 3
            eng_oct_9 = Engine(name = "2.0 TDI", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_10 = Engine(name = "2.0 TDI", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_11 = Engine(name = "2.0 TSI", power_hp = 220, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_12 = Engine(name = "2.0 TSI", power_hp = 230, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_13 = Engine(name = "2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_14 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_15 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_16 = Engine(name = "1.6 TDI", power_hp = 115, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_17 = Engine(name = "1.6 TDI", power_hp = 110, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_18 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_19 = Engine(name = "1.8 TSI", power_hp = 180, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_20 = Engine(name = "1.4 TSI", power_hp = 150, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_21 = Engine(name = "1.4 TSI", power_hp = 140, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_22 = Engine(name = "1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)

            # Octavia 2
            eng_oct_23 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_24 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_25 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_26 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_27 = Engine(name = "1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_28 = Engine(name = "1.4 TSI", power_hp = 122, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_29 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_30 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_31 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_32 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_33 = Engine(name = "1.6 FSI", power_hp = 115, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_34 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_35 = Engine(name = "1.4 MPI", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)

            # Octavia 1
            eng_oct_36 = Engine(name = "1.9 TDI", power_hp = 90, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_37 = Engine(name = "1.9 TDI", power_hp = 110, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_38 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_39 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_40 = Engine(name = "1.8 T", power_hp = 180, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_41 = Engine(name = "1.8 T", power_hp = 150, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_42 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)

            db.session.add_all([
                eng_oct_1, eng_oct_2, eng_oct_3, eng_oct_4, eng_oct_5, eng_oct_6, eng_oct_7, eng_oct_8,
                eng_oct_9, eng_oct_10, eng_oct_11, eng_oct_12, eng_oct_13, eng_oct_14, eng_oct_15, eng_oct_16,
                eng_oct_17, eng_oct_18, eng_oct_19, eng_oct_20, eng_oct_21, eng_oct_22, eng_oct_23, eng_oct_24,
                eng_oct_25, eng_oct_26, eng_oct_27, eng_oct_28, eng_oct_29, eng_oct_30, eng_oct_31, eng_oct_32,
                eng_oct_33, eng_oct_34, eng_oct_35, eng_oct_36, eng_oct_37, eng_oct_38, eng_oct_39, eng_oct_40,
                eng_oct_41, eng_oct_42
            ])

        superb = Model.query.filter_by(name = "Superb").first()
        if superb:
            # Superb 3 and Superb 4
            eng_sup_1 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_2 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_3 = Engine(name = "2.0 TDI Evo", power_hp = 200, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_4 = Engine(name = "2.0 TSI 4x4", power_hp = 280, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_5 = Engine(name = "2.0 TSI 4x4", power_hp = 272, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_6 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_7 = Engine(name = "1.4 TSI iV", power_hp = 218, displacement_cc = 1395, fuel_type = "Hybrid", euro_norm = "Euro 6", model = superb)
            eng_sup_8 = Engine(name = "1.6 TDI", power_hp = 120, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_9 = Engine(name = "2.0 TSI", power_hp = 220, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)

            # Superb 2
            eng_sup_10 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_11 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_12 = Engine(name = "3.6 FSI V6", power_hp = 260, displacement_cc = 3597, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)
            eng_sup_13 = Engine(name = "1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)
            eng_sup_14 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_15 = Engine(name = "1.4 TSI", power_hp = 125, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)

            # Superb 1
            eng_sup_16 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = superb)
            eng_sup_17 = Engine(name = "2.5 TDI V6", power_hp = 163, displacement_cc = 2496, fuel_type = "Diesel", euro_norm = "Euro 4", model = superb)
            eng_sup_18 = Engine(name = "1.8 T", power_hp = 150, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = superb)
            eng_sup_19 = Engine(name = "2.8 V6", power_hp = 193, displacement_cc = 2771, fuel_type = "Benzina", euro_norm = "Euro 4", model = superb)
            eng_sup_20 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = superb)

            db.session.add_all([
                eng_sup_1, eng_sup_2, eng_sup_3, eng_sup_4, eng_sup_5,
                eng_sup_6, eng_sup_7, eng_sup_8, eng_sup_9, eng_sup_10,
                eng_sup_11, eng_sup_12, eng_sup_13, eng_sup_14, eng_sup_15,
                eng_sup_16, eng_sup_17, eng_sup_18, eng_sup_19, eng_sup_20
            ])

        kodiaq = Model.query.filter_by(name = "Kodiaq").first()
        if kodiaq:
            # Kodiaq 2
            eng_kod_1 = Engine(name = "1.5 TSI mHEV", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_2 = Engine(name = "2.0 TDI", power_hp = 193, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_3 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_4 = Engine(name = "1.5 TSI iV", power_hp = 204, displacement_cc = 1498, fuel_type = "Hybrid", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_5 = Engine(name = "2.0 TSI", power_hp = 204, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)

            # Kodiaq 1
            eng_kod_6 = Engine(name = "2.0 BiTDI", power_hp = 240, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_7 = Engine(name = "2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_8 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_9 = Engine(name = "2.0 TDI", power_hp = 200, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_10 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_11 = Engine(name = "2.0 TSI", power_hp = 190, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_12 = Engine(name = "2.0 TSI", power_hp = 180, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_13 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_14 = Engine(name = "1.4 TSI", power_hp = 150, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)
            eng_kod_15 = Engine(name = "1.4 TSI", power_hp = 125, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 6", model = kodiaq)

            db.session.add_all([
                eng_kod_1, eng_kod_2, eng_kod_3, eng_kod_4, eng_kod_5,
                eng_kod_6, eng_kod_7, eng_kod_8, eng_kod_9, eng_kod_10,
                eng_kod_11, eng_kod_12, eng_kod_13, eng_kod_14, eng_kod_15
            ])

        karoq = Model.query.filter_by(name = "Karoq").first()
        if karoq:
            # Facelift
            eng_kar_1 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = karoq)
            eng_kar_2 = Engine(name = "2.0 TSI", power_hp = 190, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = karoq)
            eng_kar_3 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = karoq)
            eng_kar_4 = Engine(name = "2.0 TDI", power_hp = 116, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = karoq)
            eng_kar_5 = Engine(name = "1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = karoq)

            # Non-Facelift
            eng_kar_6 = Engine(name = "1.6 TDI", power_hp = 115, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = karoq)
            eng_kar_7 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = karoq)
            eng_kar_8 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = karoq)
            eng_kar_9 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = karoq)

            db.session.add_all([
                eng_kar_1, eng_kar_2, eng_kar_3, eng_kar_4, eng_kar_5,
                eng_kar_6, eng_kar_7, eng_kar_8, eng_kar_9
            ])

        kamiq = Model.query.filter_by(name = "Kamiq").first()
        if kamiq:
            eng_kam_1 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = kamiq)
            eng_kam_2 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = kamiq)
            eng_kam_3 = Engine(name = "1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = kamiq)
            eng_kam_4 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = kamiq)
            eng_kam_5 = Engine(name = "1.6 TDI", power_hp = 115, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = kamiq)

            db.session.add_all([eng_kam_1, eng_kam_2, eng_kam_3, eng_kam_4, eng_kam_5])

        scala = Model.query.filter_by(name = "Scala").first()
        if scala:
            eng_sca_1 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = scala)
            eng_sca_2 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = scala)
            eng_sca_3 = Engine(name = "1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = scala)
            eng_sca_4 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = scala)
            eng_sca_5 = Engine(name = "1.6 TDI", power_hp = 115, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = scala)

            db.session.add_all([eng_sca_1, eng_sca_2, eng_sca_3, eng_sca_4, eng_sca_5])

        fabia = Model.query.filter_by(name = "Fabia").first()
        if fabia:
            # Fabia 4
            eng_fab_1 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_2 = Engine(name = "1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_3 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_4 = Engine(name = "1.0 MPI", power_hp = 80, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_5 = Engine(name = "1.0 MPI", power_hp = 65, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)

            # Fabia 3
            eng_fab_6 = Engine(name = "1.2 TSI", power_hp = 110, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_7 = Engine(name = "1.2 TSI", power_hp = 90, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)
            eng_fab_8 = Engine(name = "1.4 TDI", power_hp = 105, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 6", model = fabia)
            eng_fab_9 = Engine(name = "1.4 TDI", power_hp = 90, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 6", model = fabia)
            eng_fab_10 = Engine(name = "1.0 MPI", power_hp = 75, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fabia)

            # Fabia 2
            eng_fab_11 = Engine(name = "1.4 TSI", power_hp = 180, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = fabia)
            eng_fab_12 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = fabia)
            eng_fab_13 = Engine(name = "1.6 TDI", power_hp = 90, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = fabia)
            eng_fab_14 = Engine(name = "1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = fabia)
            eng_fab_15 = Engine(name = "1.2 TSI", power_hp = 86, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = fabia)
            eng_fab_16 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = fabia)
            eng_fab_17 = Engine(name = "1.4 MPI", power_hp = 86, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_18 = Engine(name = "1.2 HTP", power_hp = 70, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)

            # Fabia 1
            eng_fab_20 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = fabia)
            eng_fab_21 = Engine(name = "1.9 SDI", power_hp = 64, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = fabia)
            eng_fab_22 = Engine(name = "1.4 TDI", power_hp = 75, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 4", model = fabia)
            eng_fab_23 = Engine(name = "2.0 MPI", power_hp = 115, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_24 = Engine(name = "1.4 16V", power_hp = 100, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_25 = Engine(name = "1.4 16V", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_26 = Engine(name = "1.4 MPI", power_hp = 68, displacement_cc = 1397, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_27 = Engine(name = "1.4 MPI", power_hp = 60, displacement_cc = 1397, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_28 = Engine(name = "1.2 HTP", power_hp = 64, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)
            eng_fab_29 = Engine(name = "1.2 HTP", power_hp = 54, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 4", model = fabia)

            db.session.add_all([
                eng_fab_1, eng_fab_2, eng_fab_3, eng_fab_4, eng_fab_5,
                eng_fab_6, eng_fab_7, eng_fab_8, eng_fab_9, eng_fab_10,
                eng_fab_11, eng_fab_12, eng_fab_13, eng_fab_14, eng_fab_15,
                eng_fab_16, eng_fab_17, eng_fab_18, eng_fab_20,
                eng_fab_21, eng_fab_22, eng_fab_23, eng_fab_24, eng_fab_25,
                eng_fab_26, eng_fab_27, eng_fab_28, eng_fab_29
            ])

        passat = Model.query.filter_by(name = "Passat").first()
        if passat:
            # Passat B9
            eng_pass_1 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_2 = Engine(name = "2.0 TDI", power_hp = 193, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_3 = Engine(name = "1.5 eTSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = passat)
            eng_pass_4 = Engine(name = "1.5 TSI eHybrid", power_hp = 204, displacement_cc = 1498, fuel_type = "Hybrid", euro_norm = "Euro 6", model = passat)

            # Passat B8
            eng_pass_5 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_6 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_7 = Engine(name = "2.0 BiTDI", power_hp = 240, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_8 = Engine(name = "1.6 TDI", power_hp = 120, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = passat)
            eng_pass_9 = Engine(name = "1.4 TSI GTE", power_hp = 218, displacement_cc = 1395, fuel_type = "Hybrid", euro_norm = "Euro 6", model = passat)
            eng_pass_10 = Engine(name = "2.0 TSI", power_hp = 280, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = passat)
            eng_pass_11 = Engine(name = "1.8 TSI", power_hp = 180, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 6", model = passat)

            # Passat B7
            eng_pass_12 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = passat)
            eng_pass_13 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = passat)
            eng_pass_14 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = passat)
            eng_pass_15 = Engine(name = "1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = passat)
            eng_pass_16 = Engine(name = "2.0 TSI", power_hp = 211, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 5", model = passat)

            # Passat B6
            eng_pass_17 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = passat)
            eng_pass_18 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = passat)
            eng_pass_19 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = passat)
            eng_pass_20 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = passat)
            eng_pass_21 = Engine(name = "1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 4", model = passat)
            eng_pass_22 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = passat)

            # Passat B5.5
            eng_pass_23 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = passat)
            eng_pass_24 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = passat)
            eng_pass_25 = Engine(name = "2.5 TDI V6", power_hp = 163, displacement_cc = 2496, fuel_type = "Diesel", euro_norm = "Euro 4", model = passat)
            eng_pass_26 = Engine(name = "2.5 TDI V6", power_hp = 180, displacement_cc = 2496, fuel_type = "Diesel", euro_norm = "Euro 3", model = passat)
            eng_pass_27 = Engine(name = "1.8 T", power_hp = 150, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = passat)

            db.session.add_all([
                eng_pass_1, eng_pass_2, eng_pass_3, eng_pass_4, eng_pass_5,
                eng_pass_6, eng_pass_7, eng_pass_8, eng_pass_9, eng_pass_10,
                eng_pass_11, eng_pass_12, eng_pass_13, eng_pass_14, eng_pass_15,
                eng_pass_16, eng_pass_17, eng_pass_18, eng_pass_19, eng_pass_20,
                eng_pass_21, eng_pass_22, eng_pass_23, eng_pass_24, eng_pass_25,
                eng_pass_26, eng_pass_27
            ])

        golf = Model.query.filter_by(name = "Golf").first()
        if golf:
            # Golf 8
            eng_golf_1 = Engine(name = "1.5 eTSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = golf)
            eng_golf_2 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = golf)
            eng_golf_3 = Engine(name = "2.0 TDI", power_hp = 116, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = golf)
            eng_golf_4 = Engine(name = "2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = golf)
            eng_golf_5 = Engine(name = "1.0 eTSI", power_hp = 110, displacement_cc = 999, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = golf)

            # Golf 7
            eng_golf_6 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = golf)
            eng_golf_7 = Engine(name = "1.6 TDI", power_hp = 110, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = golf)
            eng_golf_8 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = golf)
            eng_golf_9 = Engine(name = "2.0 TDI", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = golf)
            eng_golf_10 = Engine(name = "1.4 TSI", power_hp = 122, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)
            eng_golf_11 = Engine(name = "1.4 TSI", power_hp = 140, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)
            eng_golf_12 = Engine(name = "1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)
            eng_golf_13 = Engine(name = "2.0 TSI", power_hp = 220, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = golf)

            # Golf 6
            eng_golf_14 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = golf)
            eng_golf_15 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = golf)
            eng_golf_16 = Engine(name = "2.0 TDI", power_hp = 110, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = golf)
            eng_golf_17 = Engine(name = "1.4 TSI", power_hp = 122, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)
            eng_golf_18 = Engine(name = "1.4 MPI", power_hp = 80, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)
            eng_golf_19 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 5", model = golf)

            # Golf 5
            eng_golf_20 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = golf)
            eng_golf_21 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = golf)
            eng_golf_22 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = golf)
            eng_golf_23 = Engine(name = "1.4 MPI", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = golf)
            eng_golf_24 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = golf)

            # Golf 4
            eng_golf_25 = Engine(name = "1.9 TDI", power_hp = 90, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = golf)
            eng_golf_26 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = golf)
            eng_golf_27 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = golf)
            eng_golf_28 = Engine(name = "1.9 TDI", power_hp = 150, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = golf)
            eng_golf_29 = Engine(name = "1.6 16V", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = golf)
            eng_golf_30 = Engine(name = "1.4 16V", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = golf)

            db.session.add_all([
                eng_golf_1, eng_golf_2, eng_golf_3, eng_golf_4, eng_golf_5,
                eng_golf_6, eng_golf_7, eng_golf_8, eng_golf_9, eng_golf_10,
                eng_golf_11, eng_golf_12, eng_golf_13, eng_golf_14, eng_golf_15,
                eng_golf_16, eng_golf_17, eng_golf_18, eng_golf_19, eng_golf_20,
                eng_golf_21, eng_golf_22, eng_golf_23, eng_golf_24, eng_golf_25,
                eng_golf_26, eng_golf_27, eng_golf_28, eng_golf_29, eng_golf_30
            ])

        tiguan = Model.query.filter_by(name = "Tiguan").first()
        if tiguan:
            # Tiguan 2
            eng_tig_1 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = tiguan)
            eng_tig_2 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = tiguan)
            eng_tig_3 = Engine(name = "2.0 BiTDI", power_hp = 240, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = tiguan)
            eng_tig_4 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = tiguan)
            eng_tig_5 = Engine(name = "2.0 TSI", power_hp = 190, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = tiguan)

            # Tiguan 1
            eng_tig_6 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = tiguan)
            eng_tig_7 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = tiguan)
            eng_tig_8 = Engine(name = "2.0 TDI", power_hp = 110, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = tiguan)
            eng_tig_9 = Engine(name = "1.4 TSI", power_hp = 150, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = tiguan)
            eng_tig_10 = Engine(name = "1.4 TSI", power_hp = 122, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = tiguan)
            eng_tig_11 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 5", model = tiguan)

            db.session.add_all([
                eng_tig_1, eng_tig_2, eng_tig_3, eng_tig_4, eng_tig_5,
                eng_tig_6, eng_tig_7, eng_tig_8, eng_tig_9, eng_tig_10,
                eng_tig_11
            ])

        touareg = Model.query.filter_by(name = "Touareg").first()
        if touareg:
            # Touareg 3
            eng_tou_1 = Engine(name = "3.0 TDI V6", power_hp = 286, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = touareg)
            eng_tou_2 = Engine(name = "3.0 TDI V6", power_hp = 231, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = touareg)

            # Touareg 2
            eng_tou_3 = Engine(name = "3.0 TDI V6", power_hp = 245, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = touareg)
            eng_tou_4 = Engine(name = "3.0 TDI V6", power_hp = 204, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = touareg)
            eng_tou_5 = Engine(name = "3.0 TDI V6", power_hp = 262, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = touareg)

            # Touareg 1
            eng_tou_6 = Engine(name = "2.5 TDI", power_hp = 174, displacement_cc = 2461, fuel_type = "Diesel", euro_norm = "Euro 4", model = touareg)
            eng_tou_7 = Engine(name = "3.0 TDI V6", power_hp = 224, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 4", model = touareg)
            eng_tou_8 = Engine(name = "5.0 TDI V10", power_hp = 313, displacement_cc = 4921, fuel_type = "Diesel", euro_norm = "Euro 3", model = touareg)

            db.session.add_all([
                eng_tou_1, eng_tou_2, eng_tou_3, eng_tou_4, eng_tou_5,
                eng_tou_6, eng_tou_7, eng_tou_8
            ])

        polo = Model.query.filter_by(name = "Polo").first()
        if polo:
            # Polo 6
            eng_pol_1 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = polo)
            eng_pol_2 = Engine(name = "1.0 MPI", power_hp = 80, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = polo)
            eng_pol_3 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = polo)

            # Polo 5
            eng_pol_4 = Engine(name = "1.2 TSI", power_hp = 90, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = polo)
            eng_pol_5 = Engine(name = "1.6 TDI", power_hp = 90, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = polo)
            eng_pol_6 = Engine(name = "1.2 TDI", power_hp = 75, displacement_cc = 1199, fuel_type = "Diesel", euro_norm = "Euro 5", model = polo)
            eng_pol_7 = Engine(name = "1.2 MPI", power_hp = 60, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 5", model = polo)
            eng_pol_8 = Engine(name = "1.4 MPI", power_hp = 85, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = polo)

            # Polo 4
            eng_pol_9 = Engine(name = "1.2 HTP", power_hp = 64, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 4", model = polo)
            eng_pol_10 = Engine(name = "1.4 TDI", power_hp = 70, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 4", model = polo)
            eng_pol_11 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = polo)
            eng_pol_12 = Engine(name = "1.4 MPI", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = polo)
            eng_pol_13 = Engine(name = "1.9 SDI", power_hp = 64, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = polo)

            db.session.add_all([
                eng_pol_1, eng_pol_2, eng_pol_3, eng_pol_4, eng_pol_5,
                eng_pol_6, eng_pol_7, eng_pol_8, eng_pol_9, eng_pol_10,
                eng_pol_11, eng_pol_12, eng_pol_13
            ])

        seria3 = Model.query.filter_by(name = "Seria 3").first()
        if seria3:
            # G20
            eng_bmw_1 = Engine(name = "320d", power_hp = 190, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria3)
            eng_bmw_2 = Engine(name = "330i", power_hp = 258, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = seria3)
            eng_bmw_3 = Engine(name = "318d", power_hp = 150, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria3)

            # F30
            eng_bmw_4 = Engine(name = "320d", power_hp = 184, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria3)
            eng_bmw_5 = Engine(name = "320d", power_hp = 190, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria3)
            eng_bmw_6 = Engine(name = "320d ED", power_hp = 163, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria3)
            eng_bmw_7 = Engine(name = "318d", power_hp = 143, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria3)
            eng_bmw_8 = Engine(name = "328i", power_hp = 245, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 6", model = seria3)

            # E90
            eng_bmw_9 = Engine(name = "320d", power_hp = 163, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria3)
            eng_bmw_10 = Engine(name = "320d", power_hp = 177, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria3)
            eng_bmw_11 = Engine(name = "318i", power_hp = 143, displacement_cc = 1995, fuel_type = "Benzina", euro_norm = "Euro 4", model = seria3)
            eng_bmw_12 = Engine(name = "320i", power_hp = 150, displacement_cc = 1995, fuel_type = "Benzina", euro_norm = "Euro 4", model = seria3)
            eng_bmw_13 = Engine(name = "330d", power_hp = 231, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria3)

            db.session.add_all([
                eng_bmw_1, eng_bmw_2, eng_bmw_3, eng_bmw_4, eng_bmw_5,
                eng_bmw_6, eng_bmw_7, eng_bmw_8, eng_bmw_9, eng_bmw_10,
                eng_bmw_11, eng_bmw_12, eng_bmw_13
            ])

        seria4 = Model.query.filter_by(name = "Seria 4").first()
        if seria4:
            # G22
            eng_bmw_14 = Engine(name = "420d", power_hp = 190, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria4)
            eng_bmw_15 = Engine(name = "430i", power_hp = 258, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = seria4)

            # F32
            eng_bmw_16 = Engine(name = "420d", power_hp = 184, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria4)
            eng_bmw_17 = Engine(name = "420d", power_hp = 190, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria4)
            eng_bmw_18 = Engine(name = "428i", power_hp = 245, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 6", model = seria4)
            eng_bmw_19 = Engine(name = "435d xDrive", power_hp = 313, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria4)

            db.session.add_all([eng_bmw_14, eng_bmw_15, eng_bmw_16, eng_bmw_17, eng_bmw_18, eng_bmw_19])

        seria5 = Model.query.filter_by(name = "Seria 5").first()
        if seria5:
            # G30
            eng_bmw_20 = Engine(name = "520d", power_hp = 190, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria5)
            eng_bmw_21 = Engine(name = "530d", power_hp = 265, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = seria5)

            # F10
            eng_bmw_22 = Engine(name = "520d", power_hp = 184, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria5)
            eng_bmw_23 = Engine(name = "525d", power_hp = 218, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria5)
            eng_bmw_24 = Engine(name = "530d", power_hp = 245, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria5)
            eng_bmw_25 = Engine(name = "535d", power_hp = 313, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria5)

            # E60
            eng_bmw_26 = Engine(name = "520d", power_hp = 163, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria5)
            eng_bmw_27 = Engine(name = "520d", power_hp = 177, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = seria5)
            eng_bmw_28 = Engine(name = "525d", power_hp = 177, displacement_cc = 2497, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria5)
            eng_bmw_29 = Engine(name = "530d", power_hp = 218, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria5)
            eng_bmw_30 = Engine(name = "530d", power_hp = 231, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria5)
            eng_bmw_31 = Engine(name = "535d", power_hp = 272, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = seria5)

            db.session.add_all([
                eng_bmw_20, eng_bmw_21, eng_bmw_22, eng_bmw_23, eng_bmw_24,
                eng_bmw_25, eng_bmw_26, eng_bmw_27, eng_bmw_28, eng_bmw_29,
                eng_bmw_30, eng_bmw_31
            ])

        x5 = Model.query.filter_by(name = "X5").first()
        if x5:
            # G05
            eng_bmw_32 = Engine(name = "xDrive30d", power_hp = 265, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x5)
            eng_bmw_33 = Engine(name = "xDrive40i", power_hp = 340, displacement_cc = 2998, fuel_type = "Benzina", euro_norm = "Euro 6", model = x5)

            # F15
            eng_bmw_34 = Engine(name = "xDrive30d", power_hp = 258, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x5)
            eng_bmw_35 = Engine(name = "xDrive40d", power_hp = 313, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x5)
            eng_bmw_36 = Engine(name = "M50d", power_hp = 381, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x5)

            # E70
            eng_bmw_37 = Engine(name = "3.0d", power_hp = 235, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = x5)
            eng_bmw_38 = Engine(name = "3.0sd", power_hp = 286, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = x5)
            eng_bmw_39 = Engine(name = "3.0si", power_hp = 272, displacement_cc = 2996, fuel_type = "Benzina", euro_norm = "Euro 4", model = x5)

            db.session.add_all([
                eng_bmw_32, eng_bmw_33, eng_bmw_34, eng_bmw_35, eng_bmw_36,
                eng_bmw_37, eng_bmw_38, eng_bmw_39
            ])

        x6 = Model.query.filter_by(name = "X6").first()
        if x6:
            # G06
            eng_bmw_40 = Engine(name = "xDrive30d", power_hp = 265, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x6)
            eng_bmw_41 = Engine(name = "xDrive40d", power_hp = 340, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x6)

            # F16
            eng_bmw_42 = Engine(name = "xDrive30d", power_hp = 258, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x6)
            eng_bmw_43 = Engine(name = "xDrive40d", power_hp = 313, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 6", model = x6)

            # E71
            eng_bmw_44 = Engine(name = "xDrive30d", power_hp = 235, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = x6)
            eng_bmw_45 = Engine(name = "xDrive35d", power_hp = 286, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 4", model = x6)
            eng_bmw_46 = Engine(name = "xDrive40d", power_hp = 306, displacement_cc = 2993, fuel_type = "Diesel", euro_norm = "Euro 5", model = x6)

            db.session.add_all([
                eng_bmw_40, eng_bmw_41, eng_bmw_42, eng_bmw_43, eng_bmw_44,
                eng_bmw_45, eng_bmw_46
            ])

        a3 = Model.query.filter_by(name = "A3").first()
        if a3:
            # 8V
            eng_a3_1 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = a3)
            eng_a3_2 = Engine(name = "1.6 TDI", power_hp = 110, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = a3)
            eng_a3_3 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a3)
            eng_a3_4 = Engine(name = "1.4 TFSI", power_hp = 122, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = a3)

            # 8P
            eng_a3_5 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = a3)
            eng_a3_6 = Engine(name = "2.0 TDI PD", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = a3)
            eng_a3_7 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = a3)

            db.session.add_all([eng_a3_1, eng_a3_2, eng_a3_3, eng_a3_4, eng_a3_5, eng_a3_6, eng_a3_7])

        a4 = Model.query.filter_by(name = "A4").first()
        if a4:
            # B9
            eng_a4_1 = Engine(name = "2.0 TDI Ultra", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a4)
            eng_a4_2 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a4)
            eng_a4_3 = Engine(name = "3.0 TDI V6", power_hp = 272, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = a4)

            # B8
            eng_a4_4 = Engine(name = "2.0 TDI", power_hp = 143, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a4)
            eng_a4_5 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a4)
            eng_a4_6 = Engine(name = "2.0 TDI", power_hp = 177, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a4)
            eng_a4_7 = Engine(name = "3.0 TDI Quattro", power_hp = 240, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = a4)
            eng_a4_8 = Engine(name = "1.8 TFSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = a4)

            # B7 & B6
            eng_a4_9 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = a4)
            eng_a4_10 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = a4)
            eng_a4_11 = Engine(name = "1.9 TDI", power_hp = 116, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = a4)

            db.session.add_all([
                eng_a4_1, eng_a4_2, eng_a4_3, eng_a4_4, eng_a4_5, eng_a4_6,
                eng_a4_7, eng_a4_8, eng_a4_9, eng_a4_10, eng_a4_11
            ])

        a5 = Model.query.filter_by(name = "A5").first()
        if a5:
            # F5
            eng_a5_1 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a5)
            eng_a5_2 = Engine(name = "2.0 TFSI", power_hp = 252, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = a5)

            # 8T
            eng_a5_3 = Engine(name = "3.0 TDI Quattro", power_hp = 240, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = a5)
            eng_a5_4 = Engine(name = "2.7 TDI", power_hp = 190, displacement_cc = 2698, fuel_type = "Diesel", euro_norm = "Euro 5", model = a5)
            eng_a5_5 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a5)
            eng_a5_6 = Engine(name = "2.0 TDI", power_hp = 177, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a5)

            db.session.add_all([eng_a5_1, eng_a5_2, eng_a5_3, eng_a5_4, eng_a5_5, eng_a5_6])

        a6 = Model.query.filter_by(name = "A6").first()
        if a6:
            # C8
            eng_a6_1 = Engine(name = "50 TDI (3.0 V6)", power_hp = 286, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = a6)
            eng_a6_2 = Engine(name = "40 TDI (2.0)", power_hp = 204, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a6)

            # C7
            eng_a6_3 = Engine(name = "2.0 TDI", power_hp = 177, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = a6)
            eng_a6_4 = Engine(name = "2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = a6)
            eng_a6_5 = Engine(name = "3.0 TDI Quattro", power_hp = 245, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = a6)
            eng_a6_6 = Engine(name = "3.0 BiTDI", power_hp = 313, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = a6)
            eng_a6_7 = Engine(name = "3.0 BiTDI Competition", power_hp = 326, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = a6)

            # C6
            eng_a6_8 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = a6)
            eng_a6_9 = Engine(name = "2.7 TDI", power_hp = 180, displacement_cc = 2698, fuel_type = "Diesel", euro_norm = "Euro 4", model = a6)
            eng_a6_10 = Engine(name = "3.0 TDI Quattro", power_hp = 224, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 4", model = a6)
            eng_a6_11 = Engine(name = "3.0 TDI Quattro", power_hp = 233, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 4", model = a6)

            db.session.add_all([
                eng_a6_1, eng_a6_2, eng_a6_3, eng_a6_4, eng_a6_5, eng_a6_6,
                eng_a6_7, eng_a6_8, eng_a6_9, eng_a6_10, eng_a6_11
            ])

        q5 = Model.query.filter_by(name = "Q5").first()
        if q5:
            # FY
            eng_q5_1 = Engine(name = "2.0 TDI Quattro", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = q5)

            # 8R
            eng_q5_2 = Engine(name = "2.0 TDI Quattro", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = q5)
            eng_q5_3 = Engine(name = "2.0 TDI Quattro", power_hp = 177, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = q5)
            eng_q5_4 = Engine(name = "3.0 TDI Quattro", power_hp = 240, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = q5)

            db.session.add_all([eng_q5_1, eng_q5_2, eng_q5_3, eng_q5_4])

        q7 = Model.query.filter_by(name = "Q7").first()
        if q7:
            # 4M
            eng_q7_1 = Engine(name = "50 TDI (3.0 TDI)", power_hp = 286, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = q7)
            eng_q7_2 = Engine(name = "3.0 TDI", power_hp = 272, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = q7)

            # 4L
            eng_q7_3 = Engine(name = "3.0 TDI V6", power_hp = 233, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 4", model = q7)
            eng_q7_4 = Engine(name = "3.0 TDI V6", power_hp = 240, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = q7)
            eng_q7_5 = Engine(name = "4.2 TDI V8", power_hp = 326, displacement_cc = 4134, fuel_type = "Diesel", euro_norm = "Euro 4", model = q7)

            db.session.add_all([eng_q7_1, eng_q7_2, eng_q7_3, eng_q7_4, eng_q7_5])

        q8 = Model.query.filter_by(name = "Q8").first()
        if q8:
            eng_q8_1 = Engine(name = "50 TDI Quattro", power_hp = 286, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = q8)
            eng_q8_2 = Engine(name = "55 TFSI", power_hp = 340, displacement_cc = 2995, fuel_type = "Benzina", euro_norm = "Euro 6", model = q8)
            eng_q8_3 = Engine(name = "RS Q8", power_hp = 600, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = q8)

            db.session.add_all([eng_q8_1, eng_q8_2, eng_q8_3])

        tt = Model.query.filter_by(name = "TT").first()
        if tt:
            # 8J
            eng_tt_1 = Engine(name = "2.0 TFSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = tt)
            eng_tt_2 = Engine(name = "2.0 TDI Quattro", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = tt)

            # 8N
            eng_tt_3 = Engine(name = "1.8 T", power_hp = 180, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = tt)
            eng_tt_4 = Engine(name = "1.8 T Quattro", power_hp = 225, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = tt)

            db.session.add_all([eng_tt_1, eng_tt_2, eng_tt_3, eng_tt_4])

        a_class = Model.query.filter_by(name = "A-Class").first()
        if a_class:
            # W176 & W177
            eng_merc_1 = Engine(name = "A 180 CDI", power_hp = 109, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = a_class)
            eng_merc_2 = Engine(name = "A 200 CDI", power_hp = 136, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = a_class)
            eng_merc_3 = Engine(name = "A 200 d", power_hp = 150, displacement_cc = 1950, fuel_type = "Diesel", euro_norm = "Euro 6", model = a_class)
            eng_merc_4 = Engine(name = "A 45 AMG", power_hp = 360, displacement_cc = 1991, fuel_type = "Benzina", euro_norm = "Euro 6", model = a_class)

            db.session.add_all([eng_merc_1, eng_merc_2, eng_merc_3, eng_merc_4])

        c_class = Model.query.filter_by(name = "C-Class").first()
        if c_class:
            # W205
            eng_merc_5 = Engine(name = "C 220 d", power_hp = 170, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = c_class)
            eng_merc_6 = Engine(name = "C 200 d", power_hp = 136, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = c_class)
            eng_merc_7 = Engine(name = "C 250 d", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = c_class)

            # W204
            eng_merc_8 = Engine(name = "C 200 CDI", power_hp = 136, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = c_class)
            eng_merc_9 = Engine(name = "C 220 CDI", power_hp = 170, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = c_class)
            eng_merc_10 = Engine(name = "C 220 CDI", power_hp = 170, displacement_cc = 2148, fuel_type = "Diesel", euro_norm = "Euro 4", model = c_class)
            eng_merc_11 = Engine(name = "C 320 CDI V6", power_hp = 224, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 4", model = c_class)

            db.session.add_all([eng_merc_5, eng_merc_6, eng_merc_7, eng_merc_8,eng_merc_9, eng_merc_10, eng_merc_11])

        e_class = Model.query.filter_by(name = "E-Class").first()
        if e_class:
            # W213
            eng_merc_12 = Engine(name = "E 220 d", power_hp = 194, displacement_cc = 1950, fuel_type = "Diesel", euro_norm = "Euro 6", model = e_class)
            eng_merc_13 = Engine(name = "E 350 d", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 6", model = e_class)

            # W212
            eng_merc_14 = Engine(name = "E 220 CDI", power_hp = 170, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = e_class)
            eng_merc_15 = Engine(name = "E 250 CDI", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = e_class)
            eng_merc_16 = Engine(name = "E 350 CDI V6", power_hp = 265, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 5", model = e_class)
            eng_merc_17 = Engine(name = "E 200 CDI", power_hp = 136, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = e_class)

            db.session.add_all([eng_merc_12, eng_merc_13, eng_merc_14, eng_merc_15,eng_merc_16, eng_merc_17])

        s_class = Model.query.filter_by(name = "S-Class").first()
        if s_class:
            # W222
            eng_merc_18 = Engine(name = "S 350", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 6", model = s_class)
            eng_merc_19 = Engine(name = "S 500", power_hp = 455, displacement_cc = 4663, fuel_type = "Benzina", euro_norm = "Euro 6", model = s_class)

            # W221
            eng_merc_20 = Engine(name = "S 320 CDI", power_hp = 235, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 4", model = s_class)
            eng_merc_21 = Engine(name = "S 350 CDI", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 5", model = s_class)

            db.session.add_all([eng_merc_18, eng_merc_19, eng_merc_20, eng_merc_21])

        cla = Model.query.filter_by(name = "CLA").first()
        if cla:
            eng_merc_22 = Engine(name = "CLA 200 CDI", power_hp = 136, displacement_cc = 1796, fuel_type = "Diesel", euro_norm = "Euro 5", model = cla)
            eng_merc_23 = Engine(name = "CLA 220 CDI", power_hp = 170, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = cla)
            eng_merc_24 = Engine(name = "CLA 180 d", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = cla)

            db.session.add_all([eng_merc_22, eng_merc_23, eng_merc_24])

        cle = Model.query.filter_by(name = "CLE").first()
        if cle:
            eng_merc_25 = Engine(name = "CLE 220 d", power_hp = 200, displacement_cc = 1993, fuel_type = "Diesel", euro_norm = "Euro 6", model = cle)
            eng_merc_26 = Engine(name = "CLE 300 4MATIC", power_hp = 258, displacement_cc = 1999, fuel_type = "Benzina", euro_norm = "Euro 6", model = cle)

            db.session.add_all([eng_merc_25, eng_merc_26])

        cls = Model.query.filter_by(name = "CLS").first()
        if cls:
            # C218
            eng_merc_27 = Engine(name = "CLS 350 CDI", power_hp = 265, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 5", model = cls)
            eng_merc_28 = Engine(name = "CLS 250 CDI", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 5", model = cls)

            # C219
            eng_merc_29 = Engine(name = "CLS 320 CDI", power_hp = 224, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 4", model = cls)

            db.session.add_all([eng_merc_27, eng_merc_28, eng_merc_29])

        g_class = Model.query.filter_by(name = "G-Class").first()
        if g_class:
            eng_merc_30 = Engine(name = "G 63 AMG", power_hp = 585, displacement_cc = 3982, fuel_type = "Benzina", euro_norm = "Euro 6", model = g_class)
            eng_merc_31 = Engine(name = "G 350 d", power_hp = 286, displacement_cc = 2925, fuel_type = "Diesel", euro_norm = "Euro 6", model = g_class)
            eng_merc_32 = Engine(name = "G 350 BlueTEC", power_hp = 211, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 5", model = g_class)

            db.session.add_all([eng_merc_30, eng_merc_31, eng_merc_32])

        gla = Model.query.filter_by(name = "GLA").first()
        if gla:
            eng_merc_33 = Engine(name = "GLA 200 CDI", power_hp = 136, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = gla)
            eng_merc_34 = Engine(name = "GLA 180 CDI", power_hp = 109, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = gla)

            db.session.add_all([eng_merc_33, eng_merc_34])

        glb = Model.query.filter_by(name = "GLB").first()
        if glb:
            eng_merc_35 = Engine(name = "GLB 200 d", power_hp = 150, displacement_cc = 1950, fuel_type = "Diesel", euro_norm = "Euro 6", model = glb)
            eng_merc_36 = Engine(name = "GLB 220 d 4MATIC", power_hp = 190, displacement_cc = 1950, fuel_type = "Diesel", euro_norm = "Euro 6", model = glb)

            db.session.add_all([eng_merc_35, eng_merc_36])

        glc = Model.query.filter_by(name = "GLC").first()
        if glc:
            eng_merc_37 = Engine(name = "GLC 220 d 4MATIC", power_hp = 170, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = glc)
            eng_merc_38 = Engine(name = "GLC 250 d 4MATIC", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = glc)
            eng_merc_39 = Engine(name = "GLC 300 Coupe", power_hp = 245, displacement_cc = 1991, fuel_type = "Benzina", euro_norm = "Euro 6", model = glc)

            db.session.add_all([eng_merc_37, eng_merc_38, eng_merc_39])

        gle = Model.query.filter_by(name = "GLE").first()
        if gle:
            # V167 & C167
            eng_gle_1 = Engine(name = "GLE 300 d 4MATIC", power_hp = 272, displacement_cc = 1993, fuel_type = "Diesel", euro_norm = "Euro 6", model = gle)
            eng_gle_2 = Engine(name = "GLE 350 de 4MATIC", power_hp = 320, displacement_cc = 1950, fuel_type = "Hybrid", euro_norm = "Euro 6", model = gle)
            eng_gle_3 = Engine(name = "GLE 400 d 4MATIC", power_hp = 330, displacement_cc = 2925, fuel_type = "Diesel", euro_norm = "Euro 6", model = gle)
            eng_gle_4 = Engine(name = "GLE 53 AMG", power_hp = 435, displacement_cc = 2999, fuel_type = "Benzina", euro_norm = "Euro 6", model = gle)

            # W166 & C292
            eng_gle_5 = Engine(name = "GLE 350 d 4MATIC", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 6", model = gle)
            eng_gle_6 = Engine(name = "GLE 250 d 4MATIC", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = gle)
            eng_gle_7 = Engine(name = "GLE 43 AMG", power_hp = 367, displacement_cc = 2996, fuel_type = "Benzina", euro_norm = "Euro 6", model = gle)
            eng_gle_8 = Engine(name = "GLE 63 S AMG", power_hp = 585, displacement_cc = 5461, fuel_type = "Benzina", euro_norm = "Euro 6", model = gle)

            db.session.add_all([eng_gle_1, eng_gle_2, eng_gle_3, eng_gle_4, eng_gle_5, eng_gle_6, eng_gle_7, eng_gle_8])

        gls = Model.query.filter_by(name = "GLS").first()
        if gls:
            eng_merc_40 = Engine(name = "GLS 350 d 4MATIC", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 6", model = gls)
            eng_merc_41 = Engine(name = "GLS 400 d 4MATIC", power_hp = 330, displacement_cc = 2925, fuel_type = "Diesel", euro_norm = "Euro 6", model = gls)

            db.session.add_all([eng_merc_40, eng_merc_41])

        ml = Model.query.filter_by(name = "ML").first()
        if ml:
            # W164 & W166
            eng_merc_42 = Engine(name = "ML 320 CDI", power_hp = 224, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 4", model = ml)
            eng_merc_43 = Engine(name = "ML 350 BlueTEC", power_hp = 258, displacement_cc = 2987, fuel_type = "Diesel", euro_norm = "Euro 6", model = ml)
            eng_merc_44 = Engine(name = "ML 250 BlueTEC", power_hp = 204, displacement_cc = 2143, fuel_type = "Diesel", euro_norm = "Euro 6", model = ml)

            db.session.add_all([eng_merc_42, eng_merc_43, eng_merc_44])

        megane = Model.query.filter_by(name = "Megane").first()
        if megane:
            # Megane 4
            eng_meg_1 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = megane)
            eng_meg_2 = Engine(name = "1.5 dCi", power_hp = 115, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = megane)
            eng_meg_3 = Engine(name = "1.6 dCi", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = megane)
            eng_meg_4 = Engine(name = "1.3 TCe", power_hp = 140, displacement_cc = 1332, fuel_type = "Benzina", euro_norm = "Euro 6", model = megane)
            eng_meg_5 = Engine(name = "1.2 TCe", power_hp = 130, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = megane)
            eng_meg_6 = Engine(name = "1.8 RS", power_hp = 280, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 6", model = megane)

            # Megane 3
            eng_meg_7 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = megane)
            eng_meg_8 = Engine(name = "1.5 dCi", power_hp = 90, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = megane)
            eng_meg_9 = Engine(name = "1.9 dCi", power_hp = 130, displacement_cc = 1870, fuel_type = "Diesel", euro_norm = "Euro 5", model = megane)
            eng_meg_10 = Engine(name = "1.6 16V", power_hp = 110, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 5", model = megane)
            eng_meg_11 = Engine(name = "2.0 RS", power_hp = 265, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 5", model = megane)

            # Megane 2
            eng_meg_12 = Engine(name = "1.5 dCi", power_hp = 85, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 4", model = megane)
            eng_meg_13 = Engine(name = "1.9 dCi", power_hp = 120, displacement_cc = 1870, fuel_type = "Diesel", euro_norm = "Euro 3", model = megane)
            eng_meg_14 = Engine(name = "1.6 16V", power_hp = 113, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = megane)

            db.session.add_all([
                eng_meg_1, eng_meg_2, eng_meg_3, eng_meg_4, eng_meg_5,
                eng_meg_6, eng_meg_7, eng_meg_8, eng_meg_9, eng_meg_10,
                eng_meg_11, eng_meg_12, eng_meg_13, eng_meg_14
            ])

        clio = Model.query.filter_by(name = "Clio").first()
        if clio:
            # Clio 5
            eng_clio_1 = Engine(name = "1.0 TCe", power_hp = 100, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = clio)
            eng_clio_2 = Engine(name = "1.5 dCi", power_hp = 85, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = clio)
            eng_clio_3 = Engine(name = "1.0 SCe", power_hp = 65, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = clio)

            # Clio 4
            eng_clio_4 = Engine(name = "1.5 dCi", power_hp = 90, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = clio)
            eng_clio_5 = Engine(name = "1.5 dCi", power_hp = 75, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = clio)
            eng_clio_6 = Engine(name = "0.9 TCe", power_hp = 90, displacement_cc = 898, fuel_type = "Benzina", euro_norm = "Euro 6", model = clio)
            eng_clio_7 = Engine(name = "1.2 16V", power_hp = 75, displacement_cc = 1149, fuel_type = "Benzina", euro_norm = "Euro 5", model = clio)
            eng_clio_8 = Engine(name = "1.6 RS", power_hp = 200, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = clio)

            # Clio 3
            eng_clio_9 = Engine(name = "1.5 dCi", power_hp = 85, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 4", model = clio)
            eng_clio_10 = Engine(name = "1.4 16V", power_hp = 98, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = clio)

            db.session.add_all([
                eng_clio_1, eng_clio_2, eng_clio_3, eng_clio_4, eng_clio_5,
                eng_clio_6, eng_clio_7, eng_clio_8, eng_clio_9, eng_clio_10
            ])

        talisman = Model.query.filter_by(name = "Talisman").first()
        if talisman:
            eng_tal_1 = Engine(name = "1.6 dCi", power_hp = 160, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = talisman)
            eng_tal_2 = Engine(name = "1.6 dCi", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = talisman)
            eng_tal_3 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = talisman)
            eng_tal_4 = Engine(name = "2.0 dCi", power_hp = 200, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = talisman)
            eng_tal_5 = Engine(name = "1.6 TCe", power_hp = 200, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = talisman)

            db.session.add_all([eng_tal_1, eng_tal_2, eng_tal_3, eng_tal_4, eng_tal_5])

        laguna = Model.query.filter_by(name = "Laguna").first()
        if laguna:
            # Laguna 3
            eng_lag_1 = Engine(name = "2.0 dCi", power_hp = 150, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = laguna)
            eng_lag_2 = Engine(name = "2.0 dCi", power_hp = 175, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = laguna)
            eng_lag_3 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = laguna)
            eng_lag_4 = Engine(name = "2.0 16V", power_hp = 140, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 5", model = laguna)

            # Laguna 2
            eng_lag_5 = Engine(name = "1.9 dCi", power_hp = 120, displacement_cc = 1870, fuel_type = "Diesel", euro_norm = "Euro 3", model = laguna)
            eng_lag_6 = Engine(name = "1.9 dCi", power_hp = 130, displacement_cc = 1870, fuel_type = "Diesel", euro_norm = "Euro 4", model = laguna)
            eng_lag_7 = Engine(name = "1.8 16V", power_hp = 120, displacement_cc = 1783, fuel_type = "Benzina", euro_norm = "Euro 3", model = laguna)

            db.session.add_all([eng_lag_1, eng_lag_2, eng_lag_3, eng_lag_4, eng_lag_5, eng_lag_6, eng_lag_7])

        kadjar = Model.query.filter_by(name = "Kadjar").first()
        if kadjar:
            eng_kadj_1 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = kadjar)
            eng_kadj_2 = Engine(name = "1.6 dCi", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = kadjar)
            eng_kadj_3 = Engine(name = "1.3 TCe", power_hp = 140, displacement_cc = 1332, fuel_type = "Benzina", euro_norm = "Euro 6", model = kadjar)
            eng_kadj_4 = Engine(name = "1.2 TCe", power_hp = 130, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = kadjar)

            db.session.add_all([eng_kadj_1, eng_kadj_2, eng_kadj_3, eng_kadj_4])

        logan = Model.query.filter_by(name = "Logan").first()
        if logan:
            # Logan 3
            eng_log_1 = Engine(name = "1.0 ECO-G", power_hp = 100, displacement_cc = 999, fuel_type = "GPL/CNG", euro_norm = "Euro 6", model = logan)
            eng_log_2 = Engine(name = "1.0 SCe", power_hp = 65, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = logan)

            # Logan 2
            eng_log_3 = Engine(name = "0.9 TCe", power_hp = 90, displacement_cc = 898, fuel_type = "Benzina", euro_norm = "Euro 5", model = logan)
            eng_log_4 = Engine(name = "1.5 dCi", power_hp = 90, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = logan)
            eng_log_5 = Engine(name = "1.5 dCi", power_hp = 75, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = logan)
            eng_log_6 = Engine(name = "1.2 16V", power_hp = 75, displacement_cc = 1149, fuel_type = "Benzina", euro_norm = "Euro 5", model = logan)

            # Logan 1
            eng_log_7 = Engine(name = "1.4 MPI", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = logan)
            eng_log_8 = Engine(name = "1.6 MPI", power_hp = 90, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = logan)
            eng_log_9 = Engine(name = "1.5 dCi", power_hp = 85, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 4", model = logan)
            eng_log_10 = Engine(name = "1.5 dCi", power_hp = 65, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 3", model = logan)
            eng_log_11 = Engine(name = "1.6 16V", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = logan)

            db.session.add_all([
                eng_log_1, eng_log_2, eng_log_3, eng_log_4, eng_log_5,
                eng_log_6, eng_log_7, eng_log_8, eng_log_9, eng_log_10, eng_log_11
            ])

        duster = Model.query.filter_by(name = "Duster").first()
        if duster:
            # Duster 2
            eng_dus_1 = Engine(name = "1.5 dCi 4x4", power_hp = 115, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = duster)
            eng_dus_2 = Engine(name = "1.3 TCe", power_hp = 130, displacement_cc = 1332, fuel_type = "Benzina", euro_norm = "Euro 6", model = duster)
            eng_dus_3 = Engine(name = "1.3 TCe 4x4", power_hp = 150, displacement_cc = 1332, fuel_type = "Benzina", euro_norm = "Euro 6", model = duster)

            # Duster 1
            eng_dus_4 = Engine(name = "1.5 dCi 4x4", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = duster)
            eng_dus_5 = Engine(name = "1.6 16V", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 5", model = duster)
            eng_dus_6 = Engine(name = "1.5 dCi", power_hp = 90, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = duster)

            db.session.add_all([eng_dus_1, eng_dus_2, eng_dus_3, eng_dus_4, eng_dus_5, eng_dus_6])

        sandero = Model.query.filter_by(name = "Sandero").first()
        if sandero:
            eng_san_1 = Engine(name = "0.9 TCe Stepway", power_hp = 90, displacement_cc = 898, fuel_type = "Benzina", euro_norm = "Euro 5", model = sandero)
            eng_san_2 = Engine(name = "1.5 dCi", power_hp = 75, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = sandero)
            eng_san_3 = Engine(name = "1.5 dCi", power_hp = 90, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = sandero)
            eng_san_4 = Engine(name = "1.0 ECO-G Stepway", power_hp = 100, displacement_cc = 999, fuel_type = "GPL/CNG", euro_norm = "Euro 6", model = sandero)

            db.session.add_all([eng_san_1, eng_san_2, eng_san_3, eng_san_4])

        spring = Model.query.filter_by(name = "Spring").first()
        if spring:
            eng_spr_1 = Engine(name = "Electric 45", power_hp = 45, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = spring)
            eng_spr_2 = Engine(name = "Electric 65", power_hp = 65, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = spring)

            db.session.add_all([eng_spr_1, eng_spr_2])

        jogger = Model.query.filter_by(name = "Jogger").first()
        if jogger:
            eng_jog_1 = Engine(name = "Hybrid 140", power_hp = 140, displacement_cc = 1598, fuel_type = "Hybrid", euro_norm = "Euro 6", model = jogger)
            eng_jog_2 = Engine(name = "ECO-G 100", power_hp = 100, displacement_cc = 999, fuel_type = "GPL/CNG", euro_norm = "Euro 6", model = jogger)
            eng_jog_3 = Engine(name = "TCe 110", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = jogger)

            db.session.add_all([eng_jog_1, eng_jog_2, eng_jog_3])

        bigster = Model.query.filter_by(name = "Bigster").first()
        if bigster:
            eng_big_1 = Engine(name = "Hybrid 155", power_hp = 155, displacement_cc = 1798, fuel_type = "Hybrid", euro_norm = "Euro 6", model = bigster)
            eng_big_2 = Engine(name = "TCe 140", power_hp = 140, displacement_cc = 1199, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = bigster)
            eng_big_3 = Engine(name = "ECO-G 140", power_hp = 140, displacement_cc = 1199, fuel_type = "GPL/CNG", euro_norm = "Euro 6", model = bigster)
            eng_big_4 = Engine(name = "TCe 130 4x4", power_hp = 130, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 6", model = bigster)

            db.session.add_all([eng_big_1, eng_big_2, eng_big_3, eng_big_4])

        db.session.commit()

        eng_oct = Engine.query.filter_by(name = "2.0 TDI", power_hp = 150).join(Model).filter( Model.name == "Octavia").first()
        if eng_oct:
            listing1 = Listing(
                title = "Skoda Octavia 2018 - Primul Proprietar",
                year = 2018,
                mileage = 145000,
                price = 12500,
                description = "Masina intretinuta, service la zi. Nu accept schimburi.",
                phone = "0729379058",
                gearbox_type = "Automata",
                engine = eng_oct,
                owner = admin_user
            )
            db.session.add(listing1)

        eng_dus = Engine.query.filter_by(name = "1.5 dCi 4x4").join(Model).filter(Model.name == "Duster").first()
        if eng_dus:
            listing2 = Listing(
                title = "Dacia Duster 4x4",
                year = 2020,
                mileage = 45000,
                price = 16900,
                description = "Cauciucuri noi, stare perfecta de functionare.",
                phone = "0729379058",
                gearbox_type = "Manuala",
                engine = eng_dus,
                owner = admin_user
            )
            db.session.add(listing2)

        db.session.commit()

if __name__ == '__main__':
    seed()
