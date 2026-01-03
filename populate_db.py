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

        ford = Make(name = "Ford")
        db.session.add(ford)
        models_ford = ["Focus", "Mondeo", "Fiesta", "Kuga", "Mustang", "Puma", "Transit"]
        for m in models_ford:
            db.session.add(Model(name = m, make = ford))

        honda = Make(name = "Honda")
        db.session.add(honda)
        models_honda = ["Accord", "Civic", "CR-V", "HR-V"]
        for m in models_honda:
            db.session.add(Model(name = m, make = honda))

        hyundai = Make(name = "Hyundai")
        db.session.add(hyundai)
        models_hyundai = ["Elantra", "i10", "i20", "i30", "i40", "IONIQ", "Kona", "Santa Fe", "Tucson"]
        for m in models_hyundai:
            db.session.add(Model(name = m, make = hyundai))

        mazda = Make(name = "Mazda")
        db.session.add(mazda)
        models_mazda = ["2", "3", "5", "6", "CX-3", "CX-30", "CX-5", "CX-60", "CX-7", "CX-80", "MX-5", "RX-8"]
        for m in models_mazda:
            db.session.add(Model(name = m, make = mazda))

        nissan = Make(name = "Nissan")
        db.session.add(nissan)
        models_nissan = ["Qashqai", "Juke", "X-TRAIL", "Patrol", "Micra", "GT-R"]
        for m in models_nissan:
            db.session.add(Model(name = m, make = nissan))

        opel = Make(name = "Opel")
        db.session.add(opel)
        models_opel = ["Antara", "Astra", "Insignia", "Corsa", "Crossland", "Grandland", "GrandlandX", "Mokka", "Vectra", "Vivaro", "Zafira"]
        for m in models_opel:
            db.session.add(Model(name = m, make = opel))

        seat = Make(name = "Seat")
        db.session.add(seat)
        models_seat = ["Leon", "Ibiza", "Alhambra", "Altea", "Arona", "Ateca", "Exeo", "Tarraco", "Toledo"]
        for m in models_seat:
            db.session.add(Model(name = m, make = seat))

        porsche = Make(name = "Porsche")
        db.session.add(porsche)
        models_porsche = ["Boxster", "Cayenne", "Cayenne Coupe", "Cayman", "Macan", "Panamera", "Taycan", "911", "911-TURBO-S"]
        for m in models_porsche:
            db.session.add(Model(name = m, make = porsche))

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

        focus = Model.query.filter_by(name = "Focus").first()
        if focus:
            # Focus 4
            eng_foc_1 = Engine(name = "1.0 EcoBoost", power_hp = 125, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = focus)
            eng_foc_2 = Engine(name = "1.5 EcoBlue", power_hp = 120, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = focus)
            eng_foc_3 = Engine(name = "1.0 EcoBoost mHEV", power_hp = 155, displacement_cc = 999, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = focus)

            # Focus 3
            eng_foc_4 = Engine(name = "1.6 TDCi", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = focus)
            eng_foc_5 = Engine(name = "1.0 EcoBoost", power_hp = 100, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 5", model = focus)
            eng_foc_6 = Engine(name = "1.5 TDCi", power_hp = 120, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = focus)
            eng_foc_7 = Engine(name = "1.6 Ti-VCT", power_hp = 105, displacement_cc = 1596, fuel_type = "Benzina", euro_norm = "Euro 5", model = focus)
            eng_foc_8 = Engine(name = "2.0 TDCi", power_hp = 140, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 5", model = focus)
            eng_foc_9 = Engine(name = "2.0 TDCi ST", power_hp = 185, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = focus)

            # Focus 2
            eng_foc_10 = Engine(name = "1.6 TDCi", power_hp = 90, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 4", model = focus)
            eng_foc_11 = Engine(name = "1.6 TDCi", power_hp = 109, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 4", model = focus)
            eng_foc_12 = Engine(name = "1.6 16V", power_hp = 100, displacement_cc = 1596, fuel_type = "Benzina", euro_norm = "Euro 4", model = focus)
            eng_foc_13 = Engine(name = "1.8 TDCi", power_hp = 115, displacement_cc = 1753, fuel_type = "Diesel", euro_norm = "Euro 4", model = focus)

            db.session.add_all([
                eng_foc_1, eng_foc_2, eng_foc_3, eng_foc_4, eng_foc_5,
                eng_foc_6, eng_foc_7, eng_foc_8, eng_foc_9, eng_foc_10,
                eng_foc_11, eng_foc_12, eng_foc_13
            ])

        mondeo = Model.query.filter_by(name = "Mondeo").first()
        if mondeo:
            # Mondeo 5
            eng_mon_1 = Engine(name = "2.0 TDCi", power_hp = 150, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = mondeo)
            eng_mon_2 = Engine(name = "2.0 TDCi", power_hp = 180, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = mondeo)
            eng_mon_3 = Engine(name = "2.0 Hybrid", power_hp = 187, displacement_cc = 1999, fuel_type = "Hybrid", euro_norm = "Euro 6", model = mondeo)
            eng_mon_4 = Engine(name = "1.5 EcoBoost", power_hp = 160, displacement_cc = 1499, fuel_type = "Benzina", euro_norm = "Euro 6", model = mondeo)

            # Mondeo 4
            eng_mon_5 = Engine(name = "2.0 TDCi", power_hp = 140, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 5", model = mondeo)
            eng_mon_6 = Engine(name = "1.6 TDCi", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = mondeo)
            eng_mon_7 = Engine(name = "2.0 TDCi", power_hp = 163, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 5", model = mondeo)
            eng_mon_8 = Engine(name = "1.8 TDCi", power_hp = 125, displacement_cc = 1753, fuel_type = "Diesel", euro_norm = "Euro 4", model = mondeo)

            db.session.add_all([eng_mon_1, eng_mon_2, eng_mon_3, eng_mon_4, eng_mon_5, eng_mon_6, eng_mon_7, eng_mon_8])

        fiesta = Model.query.filter_by(name = "Fiesta").first()
        if fiesta:
            eng_fie_1 = Engine(name = "1.0 EcoBoost", power_hp = 100, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fiesta)
            eng_fie_2 = Engine(name = "1.25 MPI", power_hp = 82, displacement_cc = 1242, fuel_type = "Benzina", euro_norm = "Euro 5", model = fiesta)
            eng_fie_3 = Engine(name = "1.5 TDCi", power_hp = 75, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = fiesta)
            eng_fie_4 = Engine(name = "1.4 TDCi", power_hp = 68, displacement_cc = 1399, fuel_type = "Diesel", euro_norm = "Euro 4", model = fiesta)
            eng_fie_5 = Engine(name = "1.0 MPI", power_hp = 80, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = fiesta)
            eng_fie_6 = Engine(name = "1.5 EcoBoost ST", power_hp = 200, displacement_cc = 1497, fuel_type = "Benzina", euro_norm = "Euro 6", model = fiesta)

            db.session.add_all([eng_fie_1, eng_fie_2, eng_fie_3, eng_fie_4, eng_fie_5, eng_fie_6])

        kuga = Model.query.filter_by(name = "Kuga").first()
        if kuga:
            # Kuga 3
            eng_kug_1 = Engine(name = "2.5 PHEV", power_hp = 225, displacement_cc = 2488, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = kuga)
            eng_kug_2 = Engine(name = "1.5 EcoBoost", power_hp = 150, displacement_cc = 1499, fuel_type = "Benzina", euro_norm = "Euro 6", model = kuga)
            eng_kug_3 = Engine(name = "2.0 EcoBlue mHEV", power_hp = 150, displacement_cc = 1995, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = kuga)

            # Kuga 2
            eng_kug_4 = Engine(name = "2.0 TDCi 4x4", power_hp = 150, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = kuga)
            eng_kug_5 = Engine(name = "2.0 TDCi 4x4", power_hp = 180, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = kuga)
            eng_kug_6 = Engine(name = "2.0 TDCi", power_hp = 140, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 5", model = kuga)

            # Kuga 1
            eng_kug_7 = Engine(name = "2.0 TDCi 4x4", power_hp = 136, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 4", model = kuga)

            db.session.add_all([eng_kug_1, eng_kug_2, eng_kug_3, eng_kug_4, eng_kug_5, eng_kug_6, eng_kug_7])

        puma = Model.query.filter_by(name = "Puma").first()
        if puma:
            eng_pum_1 = Engine(name = "1.0 EcoBoost mHEV", power_hp = 125, displacement_cc = 999, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = puma)
            eng_pum_2 = Engine(name = "1.0 EcoBoost mHEV", power_hp = 155, displacement_cc = 999, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = puma)
            eng_pum_3 = Engine(name = "1.5 EcoBoost ST", power_hp = 200, displacement_cc = 1497, fuel_type = "Benzina", euro_norm = "Euro 6", model = puma)
            eng_pum_4 = Engine(name = "1.0 EcoBoost", power_hp = 125, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = puma)

            db.session.add_all([eng_pum_1, eng_pum_2, eng_pum_3, eng_pum_4])

        mustang = Model.query.filter_by(name = "Mustang").first()
        if mustang:
            eng_mus_1 = Engine(name = "5.0 V8 GT", power_hp = 450, displacement_cc = 5038, fuel_type = "Benzina", euro_norm = "Euro 6", model = mustang)
            eng_mus_2 = Engine(name = "2.3 EcoBoost", power_hp = 317, displacement_cc = 2261, fuel_type = "Benzina", euro_norm = "Euro 6", model = mustang)
            eng_mus_3 = Engine(name = "5.0 V8 Mach 1", power_hp = 460, displacement_cc = 5038, fuel_type = "Benzina", euro_norm = "Euro 6", model = mustang)

            db.session.add_all([eng_mus_1, eng_mus_2, eng_mus_3])

        transit = Model.query.filter_by(name = "Transit").first()
        if transit:
            eng_tra_1 = Engine(name = "2.0 EcoBlue", power_hp = 130, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = transit)
            eng_tra_2 = Engine(name = "2.0 EcoBlue", power_hp = 170, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = transit)
            eng_tra_3 = Engine(name = "2.2 TDCi", power_hp = 125, displacement_cc = 2198, fuel_type = "Diesel", euro_norm = "Euro 5", model = transit)
            eng_tra_4 = Engine(name = "2.2 TDCi", power_hp = 100, displacement_cc = 2198, fuel_type = "Diesel", euro_norm = "Euro 4", model = transit)
            eng_tra_5 = Engine(name = "2.4 TDCi", power_hp = 115, displacement_cc = 2402, fuel_type = "Diesel", euro_norm = "Euro 4", model = transit)

            db.session.add_all([eng_tra_1, eng_tra_2, eng_tra_3, eng_tra_4, eng_tra_5])

        accord = Model.query.filter_by(name = "Accord").first()
        if accord:
            # Accord 8
            eng_acc_1 = Engine(name = "2.0 i-VTEC", power_hp = 156, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 5", model = accord)
            eng_acc_2 = Engine(name = "2.2 i-DTEC", power_hp = 150, displacement_cc = 2199, fuel_type = "Diesel", euro_norm = "Euro 5", model = accord)
            eng_acc_3 = Engine(name = "2.2 i-DTEC Type-S", power_hp = 180, displacement_cc = 2199, fuel_type = "Diesel", euro_norm = "Euro 5", model = accord)
            eng_acc_4 = Engine(name = "2.4 i-VTEC", power_hp = 201, displacement_cc = 2354, fuel_type = "Benzina", euro_norm = "Euro 5", model = accord)

            # Accord 7
            eng_acc_5 = Engine(name = "2.0 i-VTEC", power_hp = 155, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 4", model = accord)
            eng_acc_6 = Engine(name = "2.2 i-CTDi", power_hp = 140, displacement_cc = 2204, fuel_type = "Diesel", euro_norm = "Euro 4", model = accord)

            db.session.add_all([eng_acc_1, eng_acc_2, eng_acc_3, eng_acc_4, eng_acc_5, eng_acc_6])

        civic = Model.query.filter_by(name = "Civic").first()
        if civic:
            # Civic 10
            eng_civ_1 = Engine(name = "1.5 VTEC Turbo", power_hp = 182, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = civic)
            eng_civ_2 = Engine(name = "1.0 VTEC Turbo", power_hp = 129, displacement_cc = 988, fuel_type = "Benzina", euro_norm = "Euro 6", model = civic)
            eng_civ_3 = Engine(name = "2.o Type R", power_hp = 320, displacement_cc = 1996, fuel_type = "Benzina", euro_norm = "Euro 6", model = civic)

            # Civic 9
            eng_civ_4 = Engine(name = "1.8 i-VTEC", power_hp = 142, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = civic)
            eng_civ_5 = Engine(name = "1.6 i-DTEC", power_hp = 120, displacement_cc = 1597, fuel_type = "Diesel", euro_norm = "Euro 5", model = civic)

            # Civic 8
            eng_civ_6 = Engine(name = "1.8 i-VTEC", power_hp = 140, displacement_cc = 1799, fuel_type = "Benzina", euro_norm = "Euro 4", model = civic)
            eng_civ_7 = Engine(name = "2.2 i-CTDi", power_hp = 140, displacement_cc = 2204, fuel_type = "Diesel", euro_norm = "Euro 4", model = civic)
            eng_civ_8 = Engine(name = "Type R (2.0)", power_hp = 201, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 4", model = civic)

            db.session.add_all([eng_civ_1, eng_civ_2, eng_civ_3, eng_civ_4, eng_civ_5, eng_civ_6, eng_civ_7, eng_civ_8])

        crv = Model.query.filter_by(name = "CR-V").first()
        if crv:
            # CR-V 5
            eng_crv_1 = Engine(name = "2.0 i-MMD Hybrid", power_hp = 184, displacement_cc = 1993, fuel_type = "Hybrid", euro_norm = "Euro 6", model = crv)
            eng_crv_2 = Engine(name = "1.5 VTEC Turbo", power_hp = 193, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = crv)

            # CR-V 4
            eng_crv_3 = Engine(name = "1.6 i-DTEC", power_hp = 160, displacement_cc = 1597, fuel_type = "Diesel", euro_norm = "Euro 6", model = crv)
            eng_crv_4 = Engine(name = "1.6 i-DTEC", power_hp = 120, displacement_cc = 1597, fuel_type = "Diesel", euro_norm = "Euro 5", model = crv)
            eng_crv_5 = Engine(name = "2.0 i-VTEC", power_hp = 155, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 5", model = crv)
            eng_crv_6 = Engine(name = "2.2 i-DTEC", power_hp = 150, displacement_cc = 2199, fuel_type = "Diesel", euro_norm = "Euro 5", model = crv)

            # CR-V 3
            eng_crv_7 = Engine(name = "2.0 i-VTEC", power_hp = 150, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 4", model = crv)
            eng_crv_8 = Engine(name = "2.2 i-CTDi", power_hp = 140, displacement_cc = 2204, fuel_type = "Diesel", euro_norm = "Euro 4", model = crv)

            db.session.add_all([eng_crv_1, eng_crv_2, eng_crv_3, eng_crv_4, eng_crv_5, eng_crv_6, eng_crv_7, eng_crv_8])

        hrv = Model.query.filter_by(name = "HR-V").first()
        if hrv:
            # HR-V 2
            eng_hrv_1 = Engine(name = "1.5 i-VTEC", power_hp = 130, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = hrv)
            eng_hrv_2 = Engine(name = "1.6 i-DTEC", power_hp = 120, displacement_cc = 1597, fuel_type = "Diesel", euro_norm = "Euro 6", model = hrv)
            eng_hrv_3 = Engine(name = "1.5 VTEC Turbo", power_hp = 182, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = hrv)

            # HR-V 1
            eng_hrv_4 = Engine(name = "1.6 i-VTEC", power_hp = 105, displacement_cc = 1590, fuel_type = "Benzina", euro_norm = "Euro 3", model = hrv)
            eng_hrv_5 = Engine(name = "1.6 i-VTEC V-TEC", power_hp = 124, displacement_cc = 1590, fuel_type = "Benzina", euro_norm = "Euro 3", model = hrv)

            db.session.add_all([eng_hrv_1, eng_hrv_2, eng_hrv_3, eng_hrv_4, eng_hrv_5])

        elantra = Model.query.filter_by(name = "Elantra").first()
        if elantra:
            # Elantra 7
            eng_ela_1 = Engine(name = "1.6 MPI", power_hp = 123, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 6", model = elantra)

            # Elantra 6
            eng_ela_2 = Engine(name = "1.6 MPI", power_hp = 128, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 6", model = elantra)
            eng_ela_3 = Engine(name = "1.6 CRDi", power_hp = 136, displacement_cc = 1582, fuel_type = "Diesel", euro_norm = "Euro 6", model = elantra)

            # Elantra 5
            eng_ela_4 = Engine(name = "1.6 MPI", power_hp = 132, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 5", model = elantra)
            eng_ela_5 = Engine(name = "1.8 MPI", power_hp = 150, displacement_cc = 1797, fuel_type = "Benzina", euro_norm = "Euro 5", model = elantra)

            db.session.add_all([eng_ela_1, eng_ela_2, eng_ela_3, eng_ela_4, eng_ela_5])

        i10 = Model.query.filter_by(name = "i10").first()
        if i10:
            eng_i10_1 = Engine(name = "1.0 MPI", power_hp = 67, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 6", model = i10)
            eng_i10_2 = Engine(name = "1.2 MPI", power_hp = 84, displacement_cc = 1248, fuel_type = "Benzina", euro_norm = "Euro 6", model = i10)
            eng_i10_3 = Engine(name = "1.0 T-GDi N-Line", power_hp = 100, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 6", model = i10)

            db.session.add_all([eng_i10_1, eng_i10_2, eng_i10_3])

        i20 = Model.query.filter_by(name = "i20").first()
        if i20:
            # i20 III
            eng_i20_1 = Engine(name = "1.0 T-GDi mHEV", power_hp = 100, displacement_cc = 998, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = i20)
            eng_i20_2 = Engine(name = "1.2 MPI", power_hp = 84, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = i20)

            # i20 II
            eng_i20_3 = Engine(name = "1.2 MPI", power_hp = 75, displacement_cc = 1248, fuel_type = "Benzina", euro_norm = "Euro 6", model = i20)
            eng_i20_4 = Engine(name = "1.1 CRDi", power_hp = 75, displacement_cc = 1120, fuel_type = "Diesel", euro_norm = "Euro 5", model = i20)
            eng_i20_5 = Engine(name = "1.4 CRDi", power_hp = 90, displacement_cc = 1396, fuel_type = "Diesel", euro_norm = "Euro 6", model = i20)

            db.session.add_all([eng_i20_1, eng_i20_2, eng_i20_3, eng_i20_4, eng_i20_5])

        i30 = Model.query.filter_by(name = "i30").first()
        if i30:
            # i30 III
            eng_i30_1 = Engine(name = "1.4 T-GDi", power_hp = 140, displacement_cc = 1353, fuel_type = "Benzina", euro_norm = "Euro 6", model = i30)
            eng_i30_2 = Engine(name = "1.5 T-GDi mHEV", power_hp = 160, displacement_cc = 1482, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = i30)
            eng_i30_3 = Engine(name = "1.6 CRDi", power_hp = 110, displacement_cc = 1582, fuel_type = "Diesel", euro_norm = "Euro 6", model = i30)
            eng_i30_4 = Engine(name = "2.0 T-GDi N", power_hp = 280, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = i30)

            # i30 II
            eng_i30_5 = Engine(name = "1.4 MPI", power_hp = 100, displacement_cc = 1396, fuel_type = "Benzina", euro_norm = "Euro 5", model = i30)
            eng_i30_6 = Engine(name = "1.6 CRDi", power_hp = 110, displacement_cc = 1582, fuel_type = "Diesel", euro_norm = "Euro 5", model = i30)
            eng_i30_7 = Engine(name = "1.6 GDi", power_hp = 135, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 5", model = i30)

            # i30 I
            eng_i30_8 = Engine(name = "1.4 MPI", power_hp = 110, displacement_cc = 1396, fuel_type = "Benzina", euro_norm = "Euro 4", model = i30)
            eng_i30_9 = Engine(name = "1.6 CRDi", power_hp = 90, displacement_cc = 1582, fuel_type = "Diesel", euro_norm = "Euro 4", model = i30)

            db.session.add_all([
                eng_i30_1, eng_i30_2, eng_i30_3, eng_i30_4, eng_i30_5, eng_i30_6, eng_i30_7, eng_i30_8, eng_i30_9])

        i40 = Model.query.filter_by(name = "i40").first()
        if i40:
            eng_i40_1 = Engine(name = "1.7 CRDi", power_hp = 136, displacement_cc = 1685, fuel_type = "Diesel", euro_norm = "Euro 5", model = i40)
            eng_i40_2 = Engine(name = "1.7 CRDi", power_hp = 115, displacement_cc = 1685, fuel_type = "Diesel", euro_norm = "Euro 5", model = i40)
            eng_i40_3 = Engine(name = "1.6 GDi", power_hp = 135, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 5", model = i40)
            eng_i40_4 = Engine(name = "2.0 GDi", power_hp = 177, displacement_cc = 1999, fuel_type = "Benzina", euro_norm = "Euro 5", model = i40)

            db.session.add_all([eng_i40_1, eng_i40_2, eng_i40_3, eng_i40_4])

        ioniq = Model.query.filter_by(name = "IONIQ").first()
        if ioniq:
            eng_ion_1 = Engine(name = "1.6 GDi Hybrid", power_hp = 141, displacement_cc = 1580, fuel_type = "Hybrid", euro_norm = "Euro 6", model = ioniq)
            eng_ion_2 = Engine(name = "1.6 GDi Plug-in", power_hp = 141, displacement_cc = 1580, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = ioniq)
            eng_ion_3 = Engine(name = "Electric 28kWh", power_hp = 120, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = ioniq)
            eng_ion_4 = Engine(name = "Electric 38kWh", power_hp = 136, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = ioniq)

            db.session.add_all([eng_ion_1, eng_ion_2, eng_ion_3, eng_ion_4])

        kona = Model.query.filter_by(name = "Kona").first()
        if kona:
            eng_kona_1 = Engine(name = "1.0 T-GDi", power_hp = 120, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 6", model = kona)
            eng_kona_2 = Engine(name = "1.6 T-GDi 4x4", power_hp = 177, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 6", model = kona)
            eng_kona_3 = Engine(name = "1.6 GDi Hybrid", power_hp = 141, displacement_cc = 1580, fuel_type = "Hybrid", euro_norm = "Euro 6", model = kona)
            eng_kona_4 = Engine(name = "Electric 64kWh", power_hp = 204, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = kona)
            eng_kona_5 = Engine(name = "Electric 39kWh", power_hp = 136, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = kona)

            db.session.add_all([eng_kona_1, eng_kona_2, eng_kona_3, eng_kona_4, eng_kona_5])

        santa = Model.query.filter_by(name = "Santa Fe").first()
        if santa:
            # Santa Fe 4 & 5
            eng_sf_1 = Engine(name = "2.2 CRDi", power_hp = 200, displacement_cc = 2199, fuel_type = "Diesel", euro_norm = "Euro 6", model = santa)
            eng_sf_2 = Engine(name = "1.6 T-GDi Hybrid", power_hp = 230, displacement_cc = 1598, fuel_type = "Hybrid", euro_norm = "Euro 6", model = santa)
            eng_sf_3 = Engine(name = "1.6 T-GDi PHEV", power_hp = 265, displacement_cc = 1598, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = santa)

            # Santa Fe 3
            eng_sf_4 = Engine(name = "2.2 CRDi", power_hp = 197, displacement_cc = 2199, fuel_type = "Diesel", euro_norm = "Euro 5", model = santa)
            eng_sf_5 = Engine(name = "2.0 CRDi", power_hp = 150, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = santa)

            # Santa Fe 2
            eng_sf_6 = Engine(name = "2.2 CRDi", power_hp = 155, displacement_cc = 2188, fuel_type = "Diesel", euro_norm = "Euro 4", model = santa)

            db.session.add_all([eng_sf_1, eng_sf_2, eng_sf_3, eng_sf_4, eng_sf_5, eng_sf_6])

        tucson = Model.query.filter_by(name = "Tucson").first()
        if tucson:
            # Tucson 4
            eng_tuc_1 = Engine(name = "1.6 T-GDi Hybrid", power_hp = 230, displacement_cc = 1598, fuel_type = "Hybrid", euro_norm = "Euro 6", model = tucson)
            eng_tuc_2 = Engine(name = "1.6 T-GDi", power_hp = 150, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 6", model = tucson)
            eng_tuc_3 = Engine(name = "1.6 T-GDi mHEV", power_hp = 180, displacement_cc = 1598, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = tucson)

            # Tucson 3
            eng_tuc_4 = Engine(name = "2.0 CRDi 4x4", power_hp = 185, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = tucson)
            eng_tuc_5 = Engine(name = "1.7 CRDi", power_hp = 115, displacement_cc = 1685, fuel_type = "Diesel", euro_norm = "Euro 6", model = tucson)
            eng_tuc_6 = Engine(name = "1.6 GDi", power_hp = 132, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 6", model = tucson)
            eng_tuc_7 = Engine(name = "1.6 T-GDi 4x4", power_hp = 177, displacement_cc = 1591, fuel_type = "Benzina", euro_norm = "Euro 6", model = tucson)

            # Tucson 1
            eng_tuc_8 = Engine(name = "2.0 CRDi", power_hp = 140, displacement_cc = 1991, fuel_type = "Diesel", euro_norm = "Euro 4", model = tucson)
            eng_tuc_9 = Engine(name = "2.0 CRDi", power_hp = 113, displacement_cc = 1991, fuel_type = "Diesel", euro_norm = "Euro 3", model = tucson)
            eng_tuc_10 = Engine(name = "2.0 GLS", power_hp = 141, displacement_cc = 1975, fuel_type = "Benzina", euro_norm = "Euro 4", model = tucson)

            db.session.add_all([
                eng_tuc_1, eng_tuc_2, eng_tuc_3, eng_tuc_4, eng_tuc_5,
                eng_tuc_6, eng_tuc_7, eng_tuc_8, eng_tuc_9, eng_tuc_10
            ])

        # Extra: make = mazda
        mazda3 = Model.query.filter_by(name = "3", make = mazda).first()
        if mazda3:
            # Mazda 3 BP
            eng_m3_1 = Engine(name = "2.0 SkyActiv-G", power_hp = 122, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda3)
            eng_m3_2 = Engine(name = "2.0 SkyActiv-X", power_hp = 180, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda3)

            # Mazda 3 BM/BN
            eng_m3_3 = Engine(name = "2.0 SkyActiv-G", power_hp = 120, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda3)
            eng_m3_4 = Engine(name = "2.0 SkyActiv-G", power_hp = 165, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda3)
            eng_m3_5 = Engine(name = "2.2 SkyActiv-D", power_hp = 150, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = mazda3)
            eng_m3_6 = Engine(name = "1.5 SkyActiv-D", power_hp = 105, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = mazda3)

            # Mazda 3 BL
            eng_m3_7 = Engine(name = "1.6 MZR", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 5", model = mazda3)
            eng_m3_8 = Engine(name = "1.6 MZ-CD", power_hp = 116, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = mazda3)
            eng_m3_9 = Engine(name = "2.2 MZR-CD", power_hp = 185, displacement_cc = 2184, fuel_type = "Diesel", euro_norm = "Euro 5", model = mazda3)

            db.session.add_all([eng_m3_1, eng_m3_2, eng_m3_3, eng_m3_4, eng_m3_5, eng_m3_6, eng_m3_7, eng_m3_8, eng_m3_9])

        mazda6 = Model.query.filter_by(name = "6", make = mazda).first()
        if mazda6:
            # Mazda 6 GJ/GL
            eng_m6_1 = Engine(name = "2.0 SkyActiv-G", power_hp = 165, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda6)
            eng_m6_2 = Engine(name = "2.0 SkyActiv-G", power_hp = 145, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda6)
            eng_m6_3 = Engine(name = "2.5 SkyActiv-G", power_hp = 192, displacement_cc = 2488, fuel_type = "Benzina", euro_norm = "Euro 6", model = mazda6)
            eng_m6_4 = Engine(name = "2.2 SkyActiv-D", power_hp = 175, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = mazda6)
            eng_m6_5 = Engine(name = "2.2 SkyActiv-D", power_hp = 150, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = mazda6)

            # Mazda 6 GH
            eng_m6_6 = Engine(name = "2.0 MZR", power_hp = 147, displacement_cc = 1999, fuel_type = "Benzina", euro_norm = "Euro 5", model = mazda6)
            eng_m6_7 = Engine(name = "2.2 MZR-CD", power_hp = 163, displacement_cc = 2184, fuel_type = "Diesel", euro_norm = "Euro 5", model = mazda6)
            eng_m6_8 = Engine(name = "2.0 MZR-CD", power_hp = 140, displacement_cc = 1998, fuel_type = "Diesel", euro_norm = "Euro 4", model = mazda6)

            db.session.add_all([eng_m6_1, eng_m6_2, eng_m6_3, eng_m6_4, eng_m6_5, eng_m6_6, eng_m6_7, eng_m6_8])

        mazda5 = Model.query.filter_by(name = "5", make = mazda).first()
        if mazda5:
            eng_m5_1 = Engine(name = "2.0 MZR", power_hp = 146, displacement_cc = 1999, fuel_type = "Benzina", euro_norm = "Euro 5", model = mazda5)
            eng_m5_2 = Engine(name = "1.6 MZ-CD", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = mazda5)
            eng_m5_3 = Engine(name = "1.8 MZR", power_hp = 115, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 4", model = mazda5)

            db.session.add_all([eng_m5_1, eng_m5_2, eng_m5_3])

        cx3 = Model.query.filter_by(name = "CX-3").first()
        if cx3:
            eng_cx3_1 = Engine(name = "2.0 SkyActiv-G", power_hp = 120, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = cx3)
            eng_cx3_2 = Engine(name = "2.0 SkyActiv-G AWD", power_hp = 150, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = cx3)
            eng_cx3_3 = Engine(name = "1.5 SkyActiv-D", power_hp = 105, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = cx3)

            db.session.add_all([eng_cx3_1, eng_cx3_2, eng_cx3_3])

        cx5 = Model.query.filter_by(name = "CX-5").first()
        if cx5:
            # CX-5 KF
            eng_cx5_1 = Engine(name = "2.5 SkyActiv-G", power_hp = 194, displacement_cc = 2488, fuel_type = "Benzina", euro_norm = "Euro 6", model = cx5)
            eng_cx5_2 = Engine(name = "2.0 SkyActiv-G", power_hp = 165, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = cx5)
            eng_cx5_3 = Engine(name = "2.2 SkyActiv-D", power_hp = 184, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = cx5)

            # CX-5 KE
            eng_cx5_4 = Engine(name = "2.2 SkyActiv-D", power_hp = 150, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = cx5)
            eng_cx5_5 = Engine(name = "2.2 SkyActiv-D AWD", power_hp = 175, displacement_cc = 2191, fuel_type = "Diesel", euro_norm = "Euro 6", model = cx5)
            eng_cx5_6 = Engine(name = "2.0 SkyActiv-G AWD", power_hp = 160, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = cx5)

            db.session.add_all([eng_cx5_1, eng_cx5_2, eng_cx5_3, eng_cx5_4, eng_cx5_5, eng_cx5_6])

        cx7 = Model.query.filter_by(name = "CX-7").first()
        if cx7:
            eng_cx7_1 = Engine(name = "2.3 DISI Turbo", power_hp = 260, displacement_cc = 2261, fuel_type = "Benzina", euro_norm = "Euro 4", model = cx7)
            eng_cx7_2 = Engine(name = "2.2 MZR-CD", power_hp = 173, displacement_cc = 2184, fuel_type = "Diesel", euro_norm = "Euro 5", model = cx7)

            db.session.add_all([eng_cx7_1, eng_cx7_2])

        cx80 = Model.query.filter_by(name = "CX-80").first()
        if cx80:
            eng_cx80_1 = Engine(name = "2.5 e-SkyActiv PHEV", power_hp = 327, displacement_cc = 2488, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = cx80)
            eng_cx80_2 = Engine(name = "3.3 e-SkyActiv D", power_hp = 254, displacement_cc = 3283, fuel_type = "Diesel Mild Hybrid", euro_norm = "Euro 6", model = cx80)

            db.session.add_all([eng_cx80_1, eng_cx80_2])

        mx5 = Model.query.filter(Model.name.in_(["MX-5"])).first()
        if mx5:
            # ND
            eng_mx5_1 = Engine(name = "1.5 SkyActiv-G", power_hp = 131, displacement_cc = 1496, fuel_type = "Benzina", euro_norm = "Euro 6", model = mx5)
            eng_mx5_2 = Engine(name = "2.0 SkyActiv-G", power_hp = 184, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mx5)
            eng_mx5_3 = Engine(name = "2.0 SkyActiv-G", power_hp = 160, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 6", model = mx5)

            # NC
            eng_mx5_4 = Engine(name = "1.8 MZR", power_hp = 126, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 4", model = mx5)
            eng_mx5_5 = Engine(name = "2.0 MZR", power_hp = 160, displacement_cc = 1999, fuel_type = "Benzina", euro_norm = "Euro 4", model = mx5)

            # NB
            eng_mx5_6 = Engine(name = "1.6 16V", power_hp = 110, displacement_cc = 1597, fuel_type = "Benzina", euro_norm = "Euro 3", model = mx5)
            eng_mx5_7 = Engine(name = "1.8 16V", power_hp = 140, displacement_cc = 1840, fuel_type = "Benzina", euro_norm = "Euro 3", model = mx5)

            db.session.add_all([eng_mx5_1, eng_mx5_2, eng_mx5_3, eng_mx5_4, eng_mx5_5, eng_mx5_6, eng_mx5_7])

        rx8 = Model.query.filter_by(name = "RX-8").first()
        if rx8:
            # Standard Power
            eng_rx8_1 = Engine(name = "1.3 Renesis", power_hp = 192, displacement_cc = 1308, fuel_type = "Benzina", euro_norm = "Euro 4", model = rx8)

            # High Power
            eng_rx8_2 = Engine(name = "1.3 Renesis HP", power_hp = 231, displacement_cc = 1308, fuel_type = "Benzina", euro_norm = "Euro 4", model = rx8)

            # Facelift
            eng_rx8_3 = Engine(name = "1.3 Renesis R3", power_hp = 231, displacement_cc = 1308, fuel_type = "Benzina", euro_norm = "Euro 4", model = rx8)

            db.session.add_all([eng_rx8_1, eng_rx8_2, eng_rx8_3])

        qashqai = Model.query.filter_by(name = "Qashqai").first()
        if qashqai:
            # Qashqai 3
            eng_qas_1 = Engine(name = "1.3 DIG-T mHEV", power_hp = 140, displacement_cc = 1332, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = qashqai)
            eng_qas_2 = Engine(name = "1.3 DIG-T mHEV 4WD", power_hp = 158, displacement_cc = 1332, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = qashqai)
            eng_qas_3 = Engine(name = "1.5 e-Power", power_hp = 190, displacement_cc = 1497, fuel_type = "Hybrid", euro_norm = "Euro 6", model = qashqai)

            # Qashqai 2
            eng_qas_4 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 6", model = qashqai)
            eng_qas_5 = Engine(name = "1.6 dCi", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = qashqai)
            eng_qas_6 = Engine(name = "1.6 dCi 4WD", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = qashqai)
            eng_qas_7 = Engine(name = "1.2 DIG-T", power_hp = 115, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = qashqai)
            eng_qas_8 = Engine(name = "1.6 DIG-T", power_hp = 163, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = qashqai)

            # Qashqai 1
            eng_qas_9 = Engine(name = "1.5 dCi", power_hp = 106, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 4", model = qashqai)
            eng_qas_10 = Engine(name = "2.0 dCi 4WD", power_hp = 150, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = qashqai)
            eng_qas_11 = Engine(name = "1.6 MPI", power_hp = 114, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = qashqai)
            eng_qas_12 = Engine(name = "2.0 MPI 4WD", power_hp = 140, displacement_cc = 1997, fuel_type = "Benzina", euro_norm = "Euro 4", model = qashqai)

            db.session.add_all([
                eng_qas_1, eng_qas_2, eng_qas_3, eng_qas_4, eng_qas_5,
                eng_qas_6, eng_qas_7, eng_qas_8, eng_qas_9, eng_qas_10,
                eng_qas_11, eng_qas_12
            ])

        juke = Model.query.filter_by(name = "Juke").first()
        if juke:
            # Juke
            eng_juk_1 = Engine(name = "1.0 DIG-T", power_hp = 117, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = juke)
            eng_juk_2 = Engine(name = "1.6 Hybrid", power_hp = 143, displacement_cc = 1598, fuel_type = "Hybrid", euro_norm = "Euro 6", model = juke)

            # Juke 1
            eng_juk_3 = Engine(name = "1.6 MPI", power_hp = 117, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 5", model = juke)
            eng_juk_4 = Engine(name = "1.5 dCi", power_hp = 110, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 5", model = juke)
            eng_juk_5 = Engine(name = "1.6 DIG-T 4WD", power_hp = 190, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 5", model = juke)
            eng_juk_6 = Engine(name = "1.6 DIG-T Nismo RS", power_hp = 218, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = juke)

            db.session.add_all([eng_juk_1, eng_juk_2, eng_juk_3, eng_juk_4, eng_juk_5, eng_juk_6])

        xtrail = Model.query.filter_by(name = "X-TRAIL").first()
        if xtrail:
            # X-Trail T33
            eng_xt_7 = Engine(name = "1.5 e-Power e-4ORCE", power_hp = 213, displacement_cc = 1497, fuel_type = "Hybrid", euro_norm = "Euro 6", model = xtrail)

            # X-Trail T32
            eng_xt_1 = Engine(name = "1.6 dCi 4WD", power_hp = 130, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = xtrail)
            eng_xt_2 = Engine(name = "2.0 dCi 4WD", power_hp = 177, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = xtrail)
            eng_xt_3 = Engine(name = "1.6 DIG-T", power_hp = 163, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = xtrail)

            # X-Trail T31
            eng_xt_4 = Engine(name = "2.0 dCi 4WD", power_hp = 150, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = xtrail)
            eng_xt_5 = Engine(name = "2.0 dCi 4WD", power_hp = 173, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 5", model = xtrail)

            # X-Trail T30
            eng_xt_6 = Engine(name = "2.2 dCi 4WD", power_hp = 136, displacement_cc = 2184, fuel_type = "Diesel", euro_norm = "Euro 3", model = xtrail)

            db.session.add_all([eng_xt_1, eng_xt_2, eng_xt_3, eng_xt_4, eng_xt_5, eng_xt_6, eng_xt_7])

        patrol = Model.query.filter_by(name = "Patrol").first()
        if patrol:
            # Y61
            eng_pat_1 = Engine(name = "3.0 Di Turbo", power_hp = 160, displacement_cc = 2953, fuel_type = "Diesel", euro_norm = "Euro 3", model = patrol)
            eng_pat_2 = Engine(name = "2.8 TD", power_hp = 129, displacement_cc = 2826, fuel_type = "Diesel", euro_norm = "Euro 2", model = patrol)

            # Y60
            eng_pat_3 = Engine(name = "2.8 TD", power_hp = 116, displacement_cc = 2826, fuel_type = "Diesel", euro_norm = "Euro 1", model = patrol)

            db.session.add_all([eng_pat_1, eng_pat_2, eng_pat_3])

        micra = Model.query.filter_by(name = "Micra").first()
        if micra:
            # K14
            eng_mic_1 = Engine(name = "0.9 IG-T", power_hp = 90, displacement_cc = 898, fuel_type = "Benzina", euro_norm = "Euro 6", model = micra)
            eng_mic_2 = Engine(name = "1.0 IG-T", power_hp = 100, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = micra)

            # K13
            eng_mic_3 = Engine(name = "1.2 DIG-S", power_hp = 98, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 5", model = micra)
            eng_mic_4 = Engine(name = "1.2 MPI", power_hp = 80, displacement_cc = 1198, fuel_type = "Benzina", euro_norm = "Euro 5", model = micra)

            # K12
            eng_mic_5 = Engine(name = "1.2 MPI", power_hp = 80, displacement_cc = 1240, fuel_type = "Benzina", euro_norm = "Euro 4", model = micra)
            eng_mic_6 = Engine(name = "1.4 MPI", power_hp = 88, displacement_cc = 1386, fuel_type = "Benzina", euro_norm = "Euro 4", model = micra)
            eng_mic_7 = Engine(name = "1.5 dCi", power_hp = 82, displacement_cc = 1461, fuel_type = "Diesel", euro_norm = "Euro 4", model = micra)

            db.session.add_all([eng_mic_1, eng_mic_2, eng_mic_3, eng_mic_4, eng_mic_5, eng_mic_6, eng_mic_7])

        gtr = Model.query.filter_by(name = "GT-R").first()
        if gtr:
            eng_gtr_1 = Engine(name = "3.8 V6 Twin-Turbo", power_hp = 570, displacement_cc = 3799, fuel_type = "Benzina", euro_norm = "Euro 6", model = gtr)
            eng_gtr_2 = Engine(name = "3.8 V6 Twin-Turbo", power_hp = 550, displacement_cc = 3799, fuel_type = "Benzina", euro_norm = "Euro 5", model = gtr)
            eng_gtr_3 = Engine(name = "3.8 V6 Twin-Turbo", power_hp = 485, displacement_cc = 3799, fuel_type = "Benzina", euro_norm = "Euro 4", model = gtr)
            eng_gtr_4 = Engine(name = "3.8 V6 Nismo", power_hp = 600, displacement_cc = 3799, fuel_type = "Benzina", euro_norm = "Euro 6", model = gtr)

            db.session.add_all([eng_gtr_1, eng_gtr_2, eng_gtr_3, eng_gtr_4])

        astra = Model.query.filter_by(name = "Astra").first()
        if astra:
            # Astra K
            eng_ast_1 = Engine(name = "1.6 CDTi", power_hp = 136, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = astra)
            eng_ast_2 = Engine(name = "1.6 CDTi", power_hp = 110, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = astra)
            eng_ast_3 = Engine(name = "1.4 Turbo", power_hp = 150, displacement_cc = 1399, fuel_type = "Benzina", euro_norm = "Euro 6", model = astra)
            eng_ast_4 = Engine(name = "1.0 Turbo", power_hp = 105, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = astra)

            # Astra J
            eng_ast_5 = Engine(name = "1.7 CDTi", power_hp = 110, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 5", model = astra)
            eng_ast_6 = Engine(name = "1.7 CDTi", power_hp = 125, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 5", model = astra)
            eng_ast_7 = Engine(name = "2.0 CDTi", power_hp = 160, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 5", model = astra)
            eng_ast_8 = Engine(name = "1.4 Turbo", power_hp = 140, displacement_cc = 1364, fuel_type = "Benzina", euro_norm = "Euro 5", model = astra)
            eng_ast_9 = Engine(name = "1.6 MPI", power_hp = 115, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 5", model = astra)

            # Astra H
            eng_ast_10 = Engine(name = "1.7 CDTi", power_hp = 101, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 4", model = astra)
            eng_ast_11 = Engine(name = "1.9 CDTi", power_hp = 120, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = astra)
            eng_ast_12 = Engine(name = "1.9 CDTi", power_hp = 150, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = astra)
            eng_ast_13 = Engine(name = "1.6 Twinport", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = astra)

            # Astra G
            eng_ast_14 = Engine(name = "1.7 DTi", power_hp = 75, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 3", model = astra)
            eng_ast_15 = Engine(name = "1.7 CDTi", power_hp = 80, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 4", model = astra)
            eng_ast_16 = Engine(name = "1.6 16V", power_hp = 101, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = astra)
            eng_ast_17 = Engine(name = "1.4 16V", power_hp = 90, displacement_cc = 1389, fuel_type = "Benzina", euro_norm = "Euro 4", model = astra)
            eng_ast_18 = Engine(name = "1.2 16V", power_hp = 75, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 4", model = astra)
            eng_ast_19 = Engine(name = "2.0 DTi", power_hp = 101, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 3", model = astra)
            eng_ast_20 = Engine(name = "1.6 8V", power_hp = 84, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = astra)

            db.session.add_all([
                eng_ast_1, eng_ast_2, eng_ast_3, eng_ast_4, eng_ast_5,
                eng_ast_6, eng_ast_7, eng_ast_8, eng_ast_9, eng_ast_10,
                eng_ast_11, eng_ast_12, eng_ast_13, eng_ast_14, eng_ast_15,
                eng_ast_16, eng_ast_17, eng_ast_18, eng_ast_19, eng_ast_20,
            ])

        insignia = Model.query.filter_by(name = "Insignia").first()
        if insignia:
            # Insignia B
            eng_ins_1 = Engine(name = "2.0 CDTi", power_hp = 170, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 6", model = insignia)
            eng_ins_2 = Engine(name = "1.6 CDTi", power_hp = 136, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = insignia)
            eng_ins_3 = Engine(name = "1.5 Turbo", power_hp = 165, displacement_cc = 1490, fuel_type = "Benzina", euro_norm = "Euro 6", model = insignia)

            # Insignia A
            eng_ins_4 = Engine(name = "2.0 CDTi", power_hp = 130, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 5", model = insignia)
            eng_ins_5 = Engine(name = "2.0 CDTi", power_hp = 160, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 5", model = insignia)
            eng_ins_6 = Engine(name = "2.0 CDTi BiTurbo", power_hp = 195, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 5", model = insignia)
            eng_ins_7 = Engine(name = "1.8 MPI", power_hp = 140, displacement_cc = 1796, fuel_type = "Benzina", euro_norm = "Euro 5", model = insignia)
            eng_ins_8 = Engine(name = "2.0 Turbo 4x4", power_hp = 220, displacement_cc = 1998, fuel_type = "Benzina", euro_norm = "Euro 5", model = insignia)

            db.session.add_all([eng_ins_1, eng_ins_2, eng_ins_3, eng_ins_4, eng_ins_5, eng_ins_6, eng_ins_7, eng_ins_8])

        corsa = Model.query.filter_by(name = "Corsa").first()
        if corsa:
            # Corsa F
            eng_cor_1 = Engine(name = "1.2 Turbo", power_hp = 100, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 6", model = corsa)
            eng_cor_2 = Engine(name = "1.5 Diesel", power_hp = 102, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = corsa)
            eng_cor_3 = Engine(name = "Corsa-e", power_hp = 136, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = corsa)

            # Corsa E
            eng_cor_4 = Engine(name = "1.4 MPI", power_hp = 90, displacement_cc = 1398, fuel_type = "Benzina", euro_norm = "Euro 6", model = corsa)
            eng_cor_5 = Engine(name = "1.3 CDTi", power_hp = 75, displacement_cc = 1248, fuel_type = "Diesel", euro_norm = "Euro 6", model = corsa)

            # Corsa D
            eng_cor_6 = Engine(name = "1.2 MPI", power_hp = 80, displacement_cc = 1229, fuel_type = "Benzina", euro_norm = "Euro 4", model = corsa)
            eng_cor_7 = Engine(name = "1.3 CDTi", power_hp = 75, displacement_cc = 1248, fuel_type = "Diesel", euro_norm = "Euro 4", model = corsa)
            eng_cor_8 = Engine(name = "1.3 CDTi", power_hp = 90, displacement_cc = 1248, fuel_type = "Diesel", euro_norm = "Euro 4", model = corsa)

            db.session.add_all([eng_cor_1, eng_cor_2, eng_cor_3, eng_cor_4, eng_cor_5, eng_cor_6, eng_cor_7, eng_cor_8])

        crossland = Model.query.filter_by(name = "Crossland").first()
        if crossland:
            eng_cro_1 = Engine(name = "1.2 Turbo", power_hp = 110, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 6", model = crossland)
            eng_cro_2 = Engine(name = "1.2 Turbo", power_hp = 130, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 6", model = crossland)
            eng_cro_3 = Engine(name = "1.6 CDTi", power_hp = 99, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 6", model = crossland)
            eng_cro_4 = Engine(name = "1.5 Diesel", power_hp = 110, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = crossland)

            db.session.add_all([eng_cro_1, eng_cro_2, eng_cro_3, eng_cro_4])

        grandland = Model.query.filter(Model.name.in_(["Grandland", "GrandlandX"])).first()
        if grandland:
            eng_gra_1 = Engine(name = "1.2 Turbo", power_hp = 130, displacement_cc = 1199, fuel_type = "Benzina", euro_norm = "Euro 6", model = grandland)
            eng_gra_2 = Engine(name = "1.5 Diesel", power_hp = 130, displacement_cc = 1499, fuel_type = "Diesel", euro_norm = "Euro 6", model = grandland)
            eng_gra_3 = Engine(name = "1.6 Diesel", power_hp = 120, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 6", model = grandland)
            eng_gra_4 = Engine(name = "2.0 Diesel", power_hp = 177, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 6", model = grandland)
            eng_gra_5 = Engine(name = "1.6 Hybrid4", power_hp = 300, displacement_cc = 1598, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = grandland)

            db.session.add_all([eng_gra_1, eng_gra_2, eng_gra_3, eng_gra_4, eng_gra_5])

        vectra = Model.query.filter_by(name = "Vectra").first()
        if vectra:
            # Vectra C
            eng_vec_1 = Engine(name = "1.9 CDTi", power_hp = 120, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = vectra)
            eng_vec_2 = Engine(name = "1.9 CDTi", power_hp = 150, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = vectra)
            eng_vec_3 = Engine(name = "2.0 DTi", power_hp = 101, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 3", model = vectra)
            eng_vec_4 = Engine(name = "2.2 DTi", power_hp = 125, displacement_cc = 2171, fuel_type = "Diesel", euro_norm = "Euro 3", model = vectra)
            eng_vec_5 = Engine(name = "1.8 MPI", power_hp = 122, displacement_cc = 1796, fuel_type = "Benzina", euro_norm = "Euro 4", model = vectra)
            eng_vec_6 = Engine(name = "1.8 MPI", power_hp = 140, displacement_cc = 1796, fuel_type = "Benzina", euro_norm = "Euro 4", model = vectra)

            db.session.add_all([eng_vec_1, eng_vec_2, eng_vec_3, eng_vec_4, eng_vec_5, eng_vec_6])

        zafira = Model.query.filter_by(name = "Zafira").first()
        if zafira:
            # Zafira C
            eng_zaf_1 = Engine(name = "2.0 CDTi", power_hp = 165, displacement_cc = 1956, fuel_type = "Diesel", euro_norm = "Euro 5", model = zafira)
            eng_zaf_2 = Engine(name = "1.6 CDTi", power_hp = 136, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = zafira)

            # Zafira B
            eng_zaf_3 = Engine(name = "1.9 CDTi", power_hp = 120, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = zafira)
            eng_zaf_4 = Engine(name = "1.9 CDTi", power_hp = 150, displacement_cc = 1910, fuel_type = "Diesel", euro_norm = "Euro 4", model = zafira)
            eng_zaf_5 = Engine(name = "1.7 CDTi", power_hp = 110, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 4", model = zafira)
            eng_zaf_6 = Engine(name = "1.7 CDTi", power_hp = 125, displacement_cc = 1686, fuel_type = "Diesel", euro_norm = "Euro 4", model = zafira)
            eng_zaf_7 = Engine(name = "1.8 MPI", power_hp = 140, displacement_cc = 1796, fuel_type = "Benzina", euro_norm = "Euro 4", model = zafira)

            db.session.add_all([eng_zaf_1, eng_zaf_2, eng_zaf_3, eng_zaf_4, eng_zaf_5, eng_zaf_6, eng_zaf_7])

        leon = Model.query.filter_by(name = "Leon").first()
        if leon:
            # Leon 4
            eng_leo_1 = Engine(name = "1.5 eTSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = leon)
            eng_leo_2 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = leon)
            eng_leo_3 = Engine(name = "1.5 TSI", power_hp = 130, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = leon)

            # Leon 3
            eng_leo_4 = Engine(name = "2.0 TDI FR", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = leon)
            eng_leo_5 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = leon)
            eng_leo_6 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = leon)
            eng_leo_7 = Engine(name = "1.4 TSI", power_hp = 125, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 6", model = leon)
            eng_leo_8 = Engine(name = "1.4 TSI", power_hp = 140, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = leon)
            eng_leo_9 = Engine(name = "2.0 TSI Cupra", power_hp = 280, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = leon)
            eng_leo_10 = Engine(name = "2.0 TSI Cupra", power_hp = 300, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = leon)

            # Leon 2
            eng_leo_11 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = leon)
            eng_leo_12 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = leon)
            eng_leo_13 = Engine(name = "2.0 TDI FR", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = leon)
            eng_leo_14 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = leon)
            eng_leo_15 = Engine(name = "2.0 TFSI Cupra", power_hp = 240, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = leon)

            # Leon 1
            eng_leo_16 = Engine(name = "1.9 TDI", power_hp = 90, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = leon)
            eng_leo_17 = Engine(name = "1.9 TDI", power_hp = 110, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = leon)
            eng_leo_18 = Engine(name = "1.9 TDI", power_hp = 150, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = leon)

            db.session.add_all([
                eng_leo_1, eng_leo_2, eng_leo_3, eng_leo_4, eng_leo_5,
                eng_leo_6, eng_leo_7, eng_leo_8, eng_leo_9, eng_leo_10,
                eng_leo_11, eng_leo_12, eng_leo_13, eng_leo_14, eng_leo_15,
                eng_leo_16, eng_leo_17, eng_leo_18
            ])

        ibiza = Model.query.filter_by(name = "Ibiza").first()
        if ibiza:
            # Ibiza 5
            eng_ibi_1 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = ibiza)
            eng_ibi_2 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = ibiza)
            eng_ibi_3 = Engine(name = "1.0 MPI", power_hp = 80, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = ibiza)

            # Ibiza 4
            eng_ibi_4 = Engine(name = "1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = ibiza)
            eng_ibi_5 = Engine(name = "1.4 MPI", power_hp = 85, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = ibiza)
            eng_ibi_6 = Engine(name = "1.2 TDI", power_hp = 75, displacement_cc = 1199, fuel_type = "Diesel", euro_norm = "Euro 5", model = ibiza)
            eng_ibi_7 = Engine(name = "1.6 TDI", power_hp = 90, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = ibiza)

            # Ibiza 3
            eng_ibi_8 = Engine(name = "1.4 TDI", power_hp = 70, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 4", model = ibiza)
            eng_ibi_9 = Engine(name = "1.4 TDI", power_hp = 80, displacement_cc = 1422, fuel_type = "Diesel", euro_norm = "Euro 4", model = ibiza)
            eng_ibi_10 = Engine(name = "1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = ibiza)
            eng_ibi_11 = Engine(name = "1.4 16V", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = ibiza)

            db.session.add_all([
                eng_ibi_1, eng_ibi_2, eng_ibi_3, eng_ibi_4, eng_ibi_5,
                eng_ibi_6, eng_ibi_7, eng_ibi_8, eng_ibi_9, eng_ibi_10, eng_ibi_11
            ])

        ateca = Model.query.filter_by(name = "Ateca").first()
        if ateca:
            eng_ate_1 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = ateca)
            eng_ate_2 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = ateca)
            eng_ate_3 = Engine(name = "2.0 TDI 4Drive", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = ateca)
            eng_ate_4 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = ateca)
            eng_ate_5 = Engine(name = "2.0 TSI Cupra", power_hp = 300, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = ateca)

            db.session.add_all([eng_ate_1, eng_ate_2, eng_ate_3, eng_ate_4, eng_ate_5])

        arona = Model.query.filter_by(name = "Arona").first()
        if arona:
            eng_aro_1 = Engine(name = "1.0 TSI", power_hp = 95, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = arona)
            eng_aro_2 = Engine(name = "1.0 TSI", power_hp = 115, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = arona)
            eng_aro_3 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = arona)
            eng_aro_4 = Engine(name = "1.6 TDI", power_hp = 95, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = arona)

            db.session.add_all([eng_aro_1, eng_aro_2, eng_aro_3, eng_aro_4])

        alhambra = Model.query.filter_by(name = "Alhambra").first()
        if alhambra:
            # 7N
            eng_alh_1 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = alhambra)
            eng_alh_2 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = alhambra)
            eng_alh_3 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = alhambra)

            # 7M
            eng_alh_4 = Engine(name = "1.9 TDI", power_hp = 116, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = alhambra)
            eng_alh_5 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = alhambra)

            db.session.add_all([eng_alh_1, eng_alh_2, eng_alh_3, eng_alh_4, eng_alh_5])

        altea = Model.query.filter_by(name = "Altea").first()
        if altea:
            eng_alt_1 = Engine(name = "1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = altea)
            eng_alt_2 = Engine(name = "2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = altea)
            eng_alt_3 = Engine(name = "1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = altea)
            eng_alt_4 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = altea)

            db.session.add_all([eng_alt_1, eng_alt_2, eng_alt_3, eng_alt_4])

        exeo = Model.query.filter_by(name = "Exeo").first()
        if exeo:
            eng_exe_1 = Engine(name = "2.0 TDI", power_hp = 143, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = exeo)
            eng_exe_2 = Engine(name = "2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = exeo)
            eng_exe_3 = Engine(name = "1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = exeo)
            eng_exe_4 = Engine(name = "2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 5", model = exeo)

            db.session.add_all([eng_exe_1, eng_exe_2, eng_exe_3, eng_exe_4])

        tarraco = Model.query.filter_by(name = "Tarraco").first()
        if tarraco:
            eng_tar_1 = Engine(name = "2.0 TDI 4Drive", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = tarraco)
            eng_tar_2 = Engine(name = "2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = tarraco)
            eng_tar_3 = Engine(name = "1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = tarraco)
            eng_tar_4 = Engine(name = "2.0 TSI 4Drive", power_hp = 190, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = tarraco)

            db.session.add_all([eng_tar_1, eng_tar_2, eng_tar_3, eng_tar_4])

        toledo = Model.query.filter_by(name = "Toledo").first()
        if toledo:
            # Toledo 4
            eng_tol_1 = Engine(name = "1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = toledo)
            eng_tol_2 = Engine(name = "1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = toledo)
            eng_tol_3 = Engine(name = "1.2 TSI", power_hp = 86, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = toledo)

            # Toledo 2
            eng_tol_4 = Engine(name = "1.9 TDI", power_hp = 110, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = toledo)
            eng_tol_5 = Engine(name = "1.6 16V", power_hp = 105, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = toledo)

            db.session.add_all([eng_tol_1, eng_tol_2, eng_tol_3, eng_tol_4, eng_tol_5])

        p911 = Model.query.filter_by(name = "911").first()
        if p911:
            # 992
            eng_911_1 = Engine(name = "3.0 Carrera S", power_hp = 450, displacement_cc = 2981, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911)
            eng_911_2 = Engine(name = "3.0 Carrera 4S", power_hp = 450, displacement_cc = 2981, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911)
            eng_911_3 = Engine(name = "4.0 GT3", power_hp = 510, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911)

            # 991
            eng_911_4 = Engine(name = "3.8 Carrera S", power_hp = 400, displacement_cc = 3800, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911)
            eng_911_5 = Engine(name = "3.4 Carrera", power_hp = 350, displacement_cc = 3436, fuel_type = "Benzina", euro_norm = "Euro 5", model = p911)

            db.session.add_all([eng_911_1, eng_911_2, eng_911_3, eng_911_4, eng_911_5])

        p911ts = Model.query.filter_by(name = "911-TURBO-S").first()
        if p911ts:
            eng_ts_1 = Engine(name = "3.8 Twin-Turbo 992", power_hp = 650, displacement_cc = 3745, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911ts)
            eng_ts_2 = Engine(name = "3.8 Twin-Turbo 991", power_hp = 580, displacement_cc = 3800, fuel_type = "Benzina", euro_norm = "Euro 6", model = p911ts)

            db.session.add_all([eng_ts_1, eng_ts_2])

        cayenne = Model.query.filter_by(name = "Cayenne").first()
        if cayenne:
            # Cayenne 3
            eng_cay_1 = Engine(name = "3.0 V6", power_hp = 340, displacement_cc = 2995, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne)
            eng_cay_2 = Engine(name = "2.9 V6 S", power_hp = 440, displacement_cc = 2894, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne)
            eng_cay_3 = Engine(name = "4.0 V8 Turbo", power_hp = 550, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne)
            eng_cay_4 = Engine(name = "3.0 E-Hybrid", power_hp = 462, displacement_cc = 2995, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = cayenne)

            # Cayenne 2
            eng_cay_5 = Engine(name = "3.0 TDI V6", power_hp = 262, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = cayenne)
            eng_cay_6 = Engine(name = "3.0 TDI V6", power_hp = 245, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = cayenne)
            eng_cay_7 = Engine(name = "4.2 TDI V8 S", power_hp = 382, displacement_cc = 4134, fuel_type = "Diesel", euro_norm = "Euro 5", model = cayenne)

            db.session.add_all([eng_cay_1, eng_cay_2, eng_cay_3, eng_cay_4, eng_cay_5, eng_cay_6, eng_cay_7])

        cayenne_c = Model.query.filter_by(name = "Cayenne Coupe").first()
        if cayenne_c:
            eng_cayc_1 = Engine(name = "4.0 V8 Turbo GT", power_hp = 640, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne_c)
            eng_cayc_2 = Engine(name = "3.0 V6", power_hp = 340, displacement_cc = 2995, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne_c)
            eng_cayc_3 = Engine(name = "4.0 V8 GTS", power_hp = 460, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayenne_c)

            db.session.add_all([eng_cayc_1, eng_cayc_2, eng_cayc_3])

        macan = Model.query.filter_by(name = "Macan").first()
        if macan:
            # Facelift
            eng_mac_1 = Engine(name = "2.0 Turbo", power_hp = 265, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = macan)
            eng_mac_2 = Engine(name = "2.9 V6 GTS", power_hp = 440, displacement_cc = 2894, fuel_type = "Benzina", euro_norm = "Euro 6", model = macan)

            # Pre-Facelift
            eng_mac_3 = Engine(name = "3.0 S Diesel", power_hp = 258, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = macan)
            eng_mac_4 = Engine(name = "3.0 S Diesel", power_hp = 211, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 6", model = macan)
            eng_mac_5 = Engine(name = "2.0 Turbo", power_hp = 252, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = macan)

            db.session.add_all([eng_mac_1, eng_mac_2, eng_mac_3, eng_mac_4, eng_mac_5])

        panamera = Model.query.filter_by(name = "Panamera").first()
        if panamera:
            # Panamera 2
            eng_pan_1 = Engine(name = "4.0 V8 Turbo", power_hp = 550, displacement_cc = 3996, fuel_type = "Benzina", euro_norm = "Euro 6", model = panamera)
            eng_pan_2 = Engine(name = "2.9 V6 4S", power_hp = 440, displacement_cc = 2894, fuel_type = "Benzina", euro_norm = "Euro 6", model = panamera)
            eng_pan_3 = Engine(name = "4.0 V8 4S Diesel", power_hp = 422, displacement_cc = 3956, fuel_type = "Diesel", euro_norm = "Euro 6", model = panamera)
            eng_pan_4 = Engine(name = "2.9 V6 E-Hybrid", power_hp = 462, displacement_cc = 2894, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = panamera)

            # Panamera 1
            eng_pan_5 = Engine(name = "3.0 Diesel", power_hp = 250, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = panamera)
            eng_pan_6 = Engine(name = "3.0 Diesel", power_hp = 300, displacement_cc = 2967, fuel_type = "Diesel", euro_norm = "Euro 5", model = panamera)

            db.session.add_all([eng_pan_1, eng_pan_2, eng_pan_3, eng_pan_4, eng_pan_5, eng_pan_6])

        taycan = Model.query.filter_by(name = "Taycan").first()
        if taycan:
            eng_tay_1 = Engine(name = "Taycan 4S", power_hp = 530, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = taycan)
            eng_tay_2 = Engine(name = "Taycan Turbo", power_hp = 680, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = taycan)
            eng_tay_3 = Engine(name = "Taycan Turbo S", power_hp = 761, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = taycan)
            eng_tay_4 = Engine(name = "Taycan RWD", power_hp = 408, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = taycan)

            db.session.add_all([eng_tay_1, eng_tay_2, eng_tay_3, eng_tay_4])

        boxter = Model.query.filter_by(name = "Boxster").first()
        if boxter:
            # 718 Boxster
            eng_box_1 = Engine(name = "2.0 Turbo", power_hp = 300, displacement_cc = 1988, fuel_type = "Benzina", euro_norm = "Euro 6", model = boxter)
            eng_box_2 = Engine(name = "2.5 S Turbo", power_hp = 350, displacement_cc = 2497, fuel_type = "Benzina", euro_norm = "Euro 6", model = boxter)

            # 981 Boxster
            eng_box_3 = Engine(name = "2.7 Boxer", power_hp = 265, displacement_cc = 2706, fuel_type = "Benzina", euro_norm = "Euro 5", model = boxter)
            eng_box_4 = Engine(name = "3.4 S Boxer", power_hp = 315, displacement_cc = 3436, fuel_type = "Benzina", euro_norm = "Euro 5", model = boxter)

            db.session.add_all([eng_box_1, eng_box_2, eng_box_3, eng_box_4])

        cayman = Model.query.filter_by(name = "Cayman").first()
        if cayman:
            # 718 Cayman
            eng_cmn_1 = Engine(name = "2.0 Turbo", power_hp = 300, displacement_cc = 1988, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayman)
            eng_cmn_2 = Engine(name = "4.0 GT4", power_hp = 420, displacement_cc = 3995, fuel_type = "Benzina", euro_norm = "Euro 6", model = cayman)

            # 987 Cayman
            eng_cmn_3 = Engine(name = "2.7 Boxer", power_hp = 245, displacement_cc = 2687, fuel_type = "Benzina", euro_norm = "Euro 4", model = cayman)
            eng_cmn_4 = Engine(name = "3.4 S Boxer", power_hp = 295, displacement_cc = 3387, fuel_type = "Benzina", euro_norm = "Euro 4", model = cayman)

            db.session.add_all([eng_cmn_1, eng_cmn_2, eng_cmn_3, eng_cmn_4])

        avensis = Model.query.filter_by(name = "Avensis").first()
        if avensis:
            # Avensis T27
            eng_ave_1 = Engine(name = "1.8 Valvematic", power_hp = 147, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = avensis)
            eng_ave_2 = Engine(name = "2.0 D-4D", power_hp = 124, displacement_cc = 1998, fuel_type = "Diesel", euro_norm = "Euro 5", model = avensis)
            eng_ave_3 = Engine(name = "2.2 D-CAT", power_hp = 177, displacement_cc = 2231, fuel_type = "Diesel", euro_norm = "Euro 5", model = avensis)
            eng_ave_4 = Engine(name = "1.6 D-4D", power_hp = 112, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = avensis)
            eng_ave_5 = Engine(name = "2.0 D-4D", power_hp = 143, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 6", model = avensis)

            # Avensis T25
            eng_ave_6 = Engine(name = "2.0 D-4D", power_hp = 115, displacement_cc = 1995, fuel_type = "Diesel", euro_norm = "Euro 4", model = avensis)
            eng_ave_7 = Engine(name = "2.2 D-4D", power_hp = 150, displacement_cc = 2231, fuel_type = "Diesel", euro_norm = "Euro 4", model = avensis)
            eng_ave_8 = Engine(name = "1.8 VVT-i", power_hp = 130, displacement_cc = 1794, fuel_type = "Benzina", euro_norm = "Euro 4", model = avensis)

            db.session.add_all([eng_ave_1, eng_ave_2, eng_ave_3, eng_ave_4, eng_ave_5, eng_ave_6, eng_ave_7, eng_ave_8])

        aygo = Model.query.filter_by(name = "Aygo").first()
        if aygo:
            eng_ayg_1 = Engine(name = "1.0 VVT-i", power_hp = 72, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 6", model = aygo)
            eng_ayg_2 = Engine(name = "1.0 VVT-i", power_hp = 68, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 5", model = aygo)

            db.session.add_all([eng_ayg_1, eng_ayg_2])

        chr_model = Model.query.filter_by(name = "C-HR").first()
        if chr_model:
            eng_chr_1 = Engine(name = "1.8 Hybrid", power_hp = 122, displacement_cc = 1798, fuel_type = "Hybrid", euro_norm = "Euro 6", model = chr_model)
            eng_chr_2 = Engine(name = "2.0 Hybrid", power_hp = 184, displacement_cc = 1987, fuel_type = "Hybrid", euro_norm = "Euro 6", model = chr_model)
            eng_chr_3 = Engine(name = "1.2 Turbo", power_hp = 116, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 6", model = chr_model)

            # 2024+
            eng_chr_4 = Engine(name = "1.8 Hybrid", power_hp = 140, displacement_cc = 1798, fuel_type = "Hybrid", euro_norm = "Euro 6", model = chr_model)
            eng_chr_5 = Engine(name = "2.0 PHEV", power_hp = 223, displacement_cc = 1987, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = chr_model)

            db.session.add_all([eng_chr_1, eng_chr_2, eng_chr_3, eng_chr_4, eng_chr_5])

        camry = Model.query.filter_by(name = "Camry").first()
        if camry:
            eng_cam_1 = Engine(name = "2.5 Hybrid", power_hp = 218, displacement_cc = 2487, fuel_type = "Hybrid", euro_norm = "Euro 6", model = camry)

            db.session.add(eng_cam_1)

        corolla = Model.query.filter_by(name = "Corolla").first()
        if corolla:
            # Corolla E210
            eng_cor_1 = Engine(name = "1.8 Hybrid", power_hp = 122, displacement_cc = 1798, fuel_type = "Hybrid", euro_norm = "Euro 6", model = corolla)
            eng_cor_2 = Engine(name = "2.0 Hybrid", power_hp = 184, displacement_cc = 1987, fuel_type = "Hybrid", euro_norm = "Euro 6", model = corolla)
            eng_cor_3 = Engine(name = "1.8 Hybrid", power_hp = 140, displacement_cc = 1798, fuel_type = "Hybrid", euro_norm = "Euro 6", model = corolla)

            # Corolla E170/E180
            eng_cor_4 = Engine(name = "1.6 Valvematic", power_hp = 132, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 6", model = corolla)
            eng_cor_5 = Engine(name = "1.4 D-4D", power_hp = 90, displacement_cc = 1364, fuel_type = "Diesel", euro_norm = "Euro 5", model = corolla)

            # Corolla E150
            eng_cor_6 = Engine(name = "1.6 Dual VVT-i", power_hp = 124, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = corolla)
            eng_cor_7 = Engine(name = "2.0 D-4D", power_hp = 126, displacement_cc = 1998, fuel_type = "Diesel", euro_norm = "Euro 4", model = corolla)

            db.session.add_all([eng_cor_1, eng_cor_2, eng_cor_3, eng_cor_4, eng_cor_5, eng_cor_6, eng_cor_7])

        highlander = Model.query.filter_by(name = "Highlander").first()
        if highlander:
            eng_hig_1 = Engine(name = "2.5 Hybrid AWD", power_hp = 248, displacement_cc = 2487, fuel_type = "Hybrid", euro_norm = "Euro 6", model = highlander)

            db.session.add(eng_hig_1)

        hilux = Model.query.filter_by(name = "Hilux").first()
        if hilux:
            # Hilux VIII
            eng_hil_1 = Engine(name = "2.4 D-4D", power_hp = 150, displacement_cc = 2393, fuel_type = "Diesel", euro_norm = "Euro 6", model = hilux)
            eng_hil_2 = Engine(name = "2.8 D-4D", power_hp = 205, displacement_cc = 2755, fuel_type = "Diesel", euro_norm = "Euro 6", model = hilux)

            # Hilux VII
            eng_hil_3 = Engine(name = "2.5 D-4D", power_hp = 120, displacement_cc = 2494, fuel_type = "Diesel", euro_norm = "Euro 4", model = hilux)
            eng_hil_4 = Engine(name = "3.0 D-4D", power_hp = 170, displacement_cc = 2982, fuel_type = "Diesel", euro_norm = "Euro 4", model = hilux)

            db.session.add_all([eng_hil_1, eng_hil_2, eng_hil_3, eng_hil_4])

        rav4 = Model.query.filter_by(name = "RAV4").first()
        if rav4:
            # RAV4 V
            eng_rav_1 = Engine(name = "2.5 Hybrid AWD", power_hp = 222, displacement_cc = 2487, fuel_type = "Hybrid", euro_norm = "Euro 6", model = rav4)
            eng_rav_2 = Engine(name = "2.5 Hybrid FWD", power_hp = 218, displacement_cc = 2487, fuel_type = "Hybrid", euro_norm = "Euro 6", model = rav4)
            eng_rav_3 = Engine(name = "2.5 PHEV", power_hp = 306, displacement_cc = 2487, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = rav4)

            # RAV4 IV
            eng_rav_4 = Engine(name = "2.5 Hybrid", power_hp = 197, displacement_cc = 2494, fuel_type = "Hybrid", euro_norm = "Euro 6", model = rav4)
            eng_rav_5 = Engine(name = "2.0 D-4D", power_hp = 124, displacement_cc = 1998, fuel_type = "Diesel", euro_norm = "Euro 5", model = rav4)
            eng_rav_6 = Engine(name = "2.2 D-4D", power_hp = 150, displacement_cc = 2231, fuel_type = "Diesel", euro_norm = "Euro 5", model = rav4)

            # RAV4 III
            eng_rav_7 = Engine(name = "2.2 D-4D", power_hp = 136, displacement_cc = 2231, fuel_type = "Diesel", euro_norm = "Euro 4", model = rav4)
            eng_rav_8 = Engine(name = "2.2 D-CAT", power_hp = 177, displacement_cc = 2231, fuel_type = "Diesel", euro_norm = "Euro 4", model = rav4)

            db.session.add_all([eng_rav_1, eng_rav_2, eng_rav_3, eng_rav_4, eng_rav_5, eng_rav_6, eng_rav_7, eng_rav_8])

        yaris = Model.query.filter_by(name = "Yaris").first()
        if yaris:
            # Yaris XP210
            eng_yar_1 = Engine(name = "1.5 Hybrid", power_hp = 115, displacement_cc = 1490, fuel_type = "Hybrid", euro_norm = "Euro 6", model = yaris)
            eng_yar_2 = Engine(name = "1.5 Hybrid 130", power_hp = 130, displacement_cc = 1490, fuel_type = "Hybrid", euro_norm = "Euro 6", model = yaris)
            eng_yar_3 = Engine(name = "1.6 GR Turbo", power_hp = 260, displacement_cc = 1618, fuel_type = "Benzina", euro_norm = "Euro 6", model = yaris)

            # Yaris XP130
            eng_yar_4 = Engine(name = "1.5 Hybrid", power_hp = 100, displacement_cc = 1497, fuel_type = "Hybrid", euro_norm = "Euro 5", model = yaris)
            eng_yar_5 = Engine(name = "1.33 Dual VVT-i", power_hp = 99, displacement_cc = 1329, fuel_type = "Benzina", euro_norm = "Euro 5", model = yaris)
            eng_yar_6 = Engine(name = "1.4 D-4D", power_hp = 90, displacement_cc = 1364, fuel_type = "Diesel", euro_norm = "Euro 5", model = yaris)

            # Yaris XP90
            eng_yar_7 = Engine(name = "1.0 VVT-i", power_hp = 69, displacement_cc = 998, fuel_type = "Benzina", euro_norm = "Euro 4", model = yaris)
            eng_yar_8 = Engine(name = "1.3 VVT-i", power_hp = 87, displacement_cc = 1298, fuel_type = "Benzina", euro_norm = "Euro 4", model = yaris)

            db.session.add_all([eng_yar_1, eng_yar_2, eng_yar_3, eng_yar_4, eng_yar_5, eng_yar_6, eng_yar_7, eng_yar_8])

        land = Model.query.filter_by(name = "Land Cruiser").first()
        if land:
            # J150
            eng_land_1 = Engine(name = "2.8 D-4D", power_hp = 204, displacement_cc = 2755, fuel_type = "Diesel", euro_norm = "Euro 6", model = land)
            eng_land_2 = Engine(name = "2.8 D-4D", power_hp = 177, displacement_cc = 2755, fuel_type = "Diesel", euro_norm = "Euro 6", model = land)
            eng_land_3 = Engine(name = "3.0 D-4D", power_hp = 190, displacement_cc = 2982, fuel_type = "Diesel", euro_norm = "Euro 5", model = land)
            eng_land_4 = Engine(name = "3.0 D-4D", power_hp = 173, displacement_cc = 2982, fuel_type = "Diesel", euro_norm = "Euro 4", model = land)

            # J200
            eng_land_5 = Engine(name = "4.5 V8 D-4D", power_hp = 286, displacement_cc = 4461, fuel_type = "Diesel", euro_norm = "Euro 4", model = land)

            db.session.add_all([eng_land_1, eng_land_2, eng_land_3, eng_land_4, eng_land_5])

        s40 = Model.query.filter_by(name = "S40").first()
        if s40:
            eng_s40_1 = Engine(name = "1.6 D", power_hp = 110, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 4", model = s40)
            eng_s40_2 = Engine(name = "2.0 D", power_hp = 136, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 4", model = s40)
            eng_s40_3 = Engine(name = "2.4 D5", power_hp = 180, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = s40)
            eng_s40_4 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = s40)
            eng_s40_5 = Engine(name = "1.6 Benzina", power_hp = 100, displacement_cc = 1596, fuel_type = "Benzina", euro_norm = "Euro 4", model = s40)

            db.session.add_all([eng_s40_1, eng_s40_2, eng_s40_3, eng_s40_4, eng_s40_5])

        v50 = Model.query.filter_by(name = "V50").first()
        if v50:
            eng_v50_1 = Engine(name = "1.6 D", power_hp = 110, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 4", model = v50)
            eng_v50_2 = Engine(name = "2.0 D", power_hp = 136, displacement_cc = 1997, fuel_type = "Diesel", euro_norm = "Euro 4", model = v50)
            eng_v50_3 = Engine(name = "2.4 D5", power_hp = 180, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = v50)
            eng_v50_4 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = v50)
            eng_v50_5 = Engine(name = "1.6 Benzina", power_hp = 100, displacement_cc = 1596, fuel_type = "Benzina", euro_norm = "Euro 4", model = v50)

            db.session.add_all([eng_v50_1, eng_v50_2, eng_v50_3, eng_v50_4, eng_v50_5])

        s60 = Model.query.filter_by(name = "S60").first()
        if s60:
            # Gen 3
            eng_s60_1 = Engine(name = "2.0 B4 Mild-Hybrid", power_hp = 197, displacement_cc = 1969, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = s60)
            eng_s60_2 = Engine(name = "2.0 T8 Recharge", power_hp = 390, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = s60)
            eng_s60_3 = Engine(name = "2.0 D4", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = s60)

            # Gen 2
            eng_s60_4 = Engine(name = "2.0 D3", power_hp = 163, displacement_cc = 1984, fuel_type = "Diesel", euro_norm = "Euro 5", model = s60)
            eng_s60_5 = Engine(name = "2.4 D5", power_hp = 215, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = s60)
            eng_s60_6 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = s60)

            # Gen 1
            eng_s60_7 = Engine(name = "2.4 D5", power_hp = 163, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 3", model = s60)
            eng_s60_8 = Engine(name = "2.4 D5", power_hp = 185, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 4", model = s60)
            eng_s60_9 = Engine(name = "2.4 Benzina", power_hp = 170, displacement_cc = 2435, fuel_type = "Benzina", euro_norm = "Euro 4", model = s60)

            db.session.add_all([eng_s60_1, eng_s60_2, eng_s60_3, eng_s60_4, eng_s60_5,
                eng_s60_6, eng_s60_7, eng_s60_8, eng_s60_9
            ])

        v60 = Model.query.filter_by(name = "V60").first()
        if v60:
            eng_v60_1 = Engine(name = "2.0 B4 Mild-Hybrid", power_hp = 197, displacement_cc = 1969, fuel_type = "Diesel Mild Hybrid", euro_norm = "Euro 6", model = v60)
            eng_v60_2 = Engine(name = "2.0 T8 Recharge", power_hp = 390, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = v60)
            eng_v60_3 = Engine(name = "2.0 D4", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = v60)
            eng_v60_4 = Engine(name = "2.0 D3", power_hp = 163, displacement_cc = 1984, fuel_type = "Diesel", euro_norm = "Euro 5", model = v60)
            eng_v60_5 = Engine(name = "2.4 D5 Plug-in Hybrid", power_hp = 215, displacement_cc = 2400, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 5", model = v60)
            eng_v60_6 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = v60)

            db.session.add_all([eng_v60_1, eng_v60_2, eng_v60_3, eng_v60_4, eng_v60_5, eng_v60_6])

        s80 = Model.query.filter_by(name = "S80").first()
        if s80:
            eng_s80_1 = Engine(name = "2.4 D5", power_hp = 185, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = s80)
            eng_s80_2 = Engine(name = "2.4 D5", power_hp = 205, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = s80)
            eng_s80_3 = Engine(name = "2.0 D3", power_hp = 163, displacement_cc = 1984, fuel_type = "Diesel", euro_norm = "Euro 5", model = s80)
            eng_s80_4 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = s80)
            eng_s80_5 = Engine(name = "4.4 V8 AWD", power_hp = 315, displacement_cc = 4414, fuel_type = "Benzina", euro_norm = "Euro 4", model = s80)

            db.session.add_all([eng_s80_1, eng_s80_2, eng_s80_3, eng_s80_4, eng_s80_5])

        s90 = Model.query.filter_by(name = "S90").first()
        if s90:
            eng_s90_1 = Engine(name = "2.0 D4", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = s90)
            eng_s90_2 = Engine(name = "2.0 D5 PowerPulse AWD", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = s90)
            eng_s90_3 = Engine(name = "2.0 T8 Twin Engine", power_hp = 390, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = s90)
            eng_s90_4 = Engine(name = "2.0 B5 Mild-Hybrid", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel Mild Hybrid", euro_norm = "Euro 6", model = s90)

            db.session.add_all([eng_s90_1, eng_s90_2, eng_s90_3, eng_s90_4])

        v90 = Model.query.filter_by(name = "V90").first()
        if v90:
            eng_v90_1 = Engine(name = "2.0 D4", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = v90)
            eng_v90_2 = Engine(name = "2.0 D5 PowerPulse AWD", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = v90)
            eng_v90_3 = Engine(name = "2.0 T8 Twin Engine", power_hp = 390, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = v90)
            eng_v90_4 = Engine(name = "2.0 B5 Mild-Hybrid", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel Mild Hybrid", euro_norm = "Euro 6", model = v90)

            db.session.add_all([eng_v90_1, eng_v90_2, eng_v90_3, eng_v90_4])

        v40 = Model.query.filter_by(name = "V40").first()
        if v40:
            eng_v40_1 = Engine(name = "2.0 D2", power_hp = 120, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = v40)
            eng_v40_2 = Engine(name = "1.6 D2", power_hp = 115, displacement_cc = 1560, fuel_type = "Diesel", euro_norm = "Euro 5", model = v40)
            eng_v40_3 = Engine(name = "2.0 D3", power_hp = 150, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = v40)
            eng_v40_4 = Engine(name = "1.5 T3", power_hp = 152, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = v40)
            eng_v40_5 = Engine(name = "1.9 DI", power_hp = 115, displacement_cc = 1870, fuel_type = "Diesel", euro_norm = "Euro 3", model = v40)

            db.session.add_all([eng_v40_1, eng_v40_2, eng_v40_3, eng_v40_4, eng_v40_5])

        v70 = Model.query.filter_by(name = "V70").first()
        if v70:
            eng_v70_1 = Engine(name = "2.4 D5", power_hp = 185, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = v70)
            eng_v70_2 = Engine(name = "2.4 D5", power_hp = 215, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = v70)
            eng_v70_3 = Engine(name = "2.0 D3", power_hp = 163, displacement_cc = 1984, fuel_type = "Diesel", euro_norm = "Euro 5", model = v70)
            eng_v70_4 = Engine(name = "2.4 D5", power_hp = 163, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 3", model = v70)

            db.session.add_all([eng_v70_1, eng_v70_2, eng_v70_3, eng_v70_4])

        xc70 = Model.query.filter_by(name = "XC70").first()
        if xc70:
            eng_xc70_1 = Engine(name = "2.4 D5 AWD", power_hp = 185, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = xc70)
            eng_xc70_2 = Engine(name = "2.4 D5 AWD", power_hp = 215, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = xc70)
            eng_xc70_3 = Engine(name = "2.4 D4 AWD", power_hp = 181, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 6", model = xc70)
            eng_xc70_4 = Engine(name = "2.4 D5 AWD", power_hp = 163, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 3", model = xc70)

            db.session.add_all([eng_xc70_1, eng_xc70_2, eng_xc70_3, eng_xc70_4])

        xc40 = Model.query.filter_by(name = "XC40").first()
        if xc40:
            eng_xc40_1 = Engine(name = "2.0 D3 AWD", power_hp = 150, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = xc40)
            eng_xc40_2 = Engine(name = "2.0 D4 AWD", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = xc40)
            eng_xc40_3 = Engine(name = "1.5 T3", power_hp = 163, displacement_cc = 1477, fuel_type = "Benzina", euro_norm = "Euro 6", model = xc40)
            eng_xc40_4 = Engine(name = "P8 Recharge", power_hp = 408, displacement_cc = 0, fuel_type = "Electric", euro_norm = "Zero", model = xc40)

            db.session.add_all([eng_xc40_1, eng_xc40_2, eng_xc40_3, eng_xc40_4])

        xc60 = Model.query.filter_by(name = "XC60").first()
        if xc60:
            # Gen 2
            eng_xc60_1 = Engine(name = "2.0 B4 AWD", power_hp = 197, displacement_cc = 1969, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = xc60)
            eng_xc60_2 = Engine(name = "2.0 T8 Recharge", power_hp = 390, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = xc60)
            eng_xc60_3 = Engine(name = "2.0 D4 AWD", power_hp = 190, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = xc60)

            # Gen 1
            eng_xc60_4 = Engine(name = "2.4 D5 AWD", power_hp = 215, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = xc60)
            eng_xc60_5 = Engine(name = "2.4 D5 AWD", power_hp = 205, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 5", model = xc60)
            eng_xc60_6 = Engine(name = "2.4 D5 AWD", power_hp = 185, displacement_cc = 2400, fuel_type = "Diesel", euro_norm = "Euro 4", model = xc60)
            eng_xc60_7 = Engine(name = "2.0 D3", power_hp = 163, displacement_cc = 1984, fuel_type = "Diesel", euro_norm = "Euro 5", model = xc60)

            db.session.add_all([eng_xc60_1, eng_xc60_2, eng_xc60_3, eng_xc60_4, eng_xc60_5, eng_xc60_6, eng_xc60_7])

        xc90 = Model.query.filter_by(name = "XC90").first()
        if xc90:
            # Gen 2
            eng_xc90_1 = Engine(name = "2.0 D5 AWD", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel", euro_norm = "Euro 6", model = xc90)
            eng_xc90_2 = Engine(name = "2.0 T8 Twin Engine", power_hp = 407, displacement_cc = 1969, fuel_type = "Hybrid Plug-in", euro_norm = "Euro 6", model = xc90)
            eng_xc90_3 = Engine(name = "2.0 B5 AWD", power_hp = 235, displacement_cc = 1969, fuel_type = "Diesel Mild Hybrid", euro_norm = "Euro 6", model = xc90)

            # Gen 1
            eng_xc90_4 = Engine(name = "2.4 D5 AWD", power_hp = 185, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 4", model = xc90)
            eng_xc90_5 = Engine(name = "2.4 D5 AWD", power_hp = 163, displacement_cc = 2401, fuel_type = "Diesel", euro_norm = "Euro 3", model = xc90)
            eng_xc90_6 = Engine(name = "2.9 T6 AWD", power_hp = 272, displacement_cc = 2922, fuel_type = "Benzina", euro_norm = "Euro 4", model = xc90)

            db.session.add_all([eng_xc90_1, eng_xc90_2, eng_xc90_3, eng_xc90_4, eng_xc90_5, eng_xc90_6])

        eng_oct = Engine.query.filter_by(name = "2.0 TDI", power_hp = 184).join(Model).filter( Model.name == "Octavia").first()
        if eng_oct:
            listing1 = Listing(
                title = "Skoda Octavia 2.0 TDI 4x4 DSG Style",
                year = 2019,
                mileage = 120000,
                price = 17100,
                description = "Acum 10000km au fost schimbate: placute si discuri fata spate, ulei cutie viteze, ulei grup spate, bucsa grup spate, anvelope allseason Hankook noi. Mici zgarieturi la exterior, fara accidente, istoric curat.",
                phone = "0729379058",
                gearbox_type = "Automata",
                image_list = 'skoda_octavia_3.png',
                engine = eng_oct,
                owner = admin_user
            )
            db.session.add(listing1)

        eng_dus = Engine.query.filter_by(name = "1.5 dCi 4x4").join(Model).filter(Model.name == "Duster").first()
        if eng_dus:
            listing2 = Listing(
                title = "Dacia Duster Blue dCi 115 Prestige",
                year = 2021,
                mileage = 66950,
                price = 15990,
                description = "Anvelope noi de iarna, stare perfecta de functionare.",
                phone = "0729379058",
                gearbox_type = "Manuala",
                image_list = 'dacia_duster.png',
                engine = eng_dus,
                owner = admin_user
            )
            db.session.add(listing2)

        eng_golf = Engine.query.filter_by(name = "1.6 TDI", power_hp = 105).join(Model).filter(Model.name == "Golf").first()
        if eng_golf:
            listing3 = Listing(
                title = "Volkswagen Golf 1.6 TDI DPF BlueMotion",
                year = 2011,
                mileage = 320000,
                price = 3500,
                description = "De noua din Romania, AC, geamuri electrice, navigatie mare.",
                phone = "0729379058",
                gearbox_type = "Manuala",
                image_list = 'vw_golf_6.png',
                engine = eng_golf,
                owner = admin_user
            )
            db.session.add(listing3)

        eng_volvo = Engine.query.filter_by(name = "2.0 D5 AWD", power_hp = 235).join(Model).filter(Model.name == "XC90").first()
        if eng_volvo:
            listing_volvo = Listing(
                title = "Volvo XC 90 B5 MHEV AWD R-Design",
                year = 2023,
                mileage = 89000,
                price = 49500,
                description = "Import Germania, masina nu prezinta defecte. Au fost schimbate discurile si placutele in urma cu 3000km. Ofer garantie.",
                phone = "0729379058",
                gearbox_type = "Automata",
                image_list = 'volvo_xc90.png',
                engine = eng_volvo,
                owner = admin_user
            )
            db.session.add(listing_volvo)

        eng_pass = Engine.query.filter_by(name = "2.0 TSI", power_hp = 280).join(Model).filter(Model.name == "Passat").first()
        if eng_pass:
            listing_passat = Listing(
                title = "Volkswagen Passat Variant 2.0 TSI DSG 4Motion Highline",
                year = 2016,
                mileage = 272000,
                price = 13990,
                description = "Echipare Highline, istoric in reprezentanta de noua. Sistemul 4x4 a fost refacut la Arad la 267000km cu piese originale si dispune de 7 luni garantie. VIN: WVWZZZ3CZGE155843.",
                phone = "0729379058",
                gearbox_type = "Automata",
                image_list = 'passat_benzina.png',
                engine = eng_pass,
                owner = admin_user
            )
            db.session.add(listing_passat)

        db.session.commit()

if __name__ == '__main__':
    seed()
