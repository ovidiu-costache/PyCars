from app import app
from database import db
from models import Make, Model, Engine, Listing

def seed():
    with app.app_context():
        db.session.query(Listing).delete()
        db.session.query(Engine).delete()
        db.session.query(Model).delete()
        db.session.query(Make).delete()

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

        octavia = Model.query.filter_by(name="Octavia").first()
        if octavia:
            # Octavia 4
            eng_oct_1 = Engine(name="2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_2 = Engine(name="2.0 TDI", power_hp = 115, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_3 = Engine(name="2.0 TDI", power_hp = 200, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_4 = Engine(name="2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_5 = Engine(name="1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_6 = Engine(name="1.5 TSI mHEV", power_hp = 150, displacement_cc = 1498, fuel_type = "Mild Hybrid", euro_norm = "Euro 6", model = octavia)
            eng_oct_7 = Engine(name="1.0 TSI", power_hp = 110, displacement_cc = 999, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_8 = Engine(name="1.4 TSI iV", power_hp = 204, displacement_cc = 1395, fuel_type = "Hybrid", euro_norm = "Euro 6", model = octavia)

            # Octavia 3
            eng_oct_9 = Engine(name="2.0 TDI", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_10 = Engine(name="2.0 TDI", power_hp = 184, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_11 = Engine(name="2.0 TSI", power_hp = 220, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_12 = Engine(name="2.0 TSI", power_hp = 230, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_13 = Engine(name="2.0 TSI", power_hp = 245, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_14 = Engine(name="2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_15 = Engine(name="2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_16 = Engine(name="1.6 TDI", power_hp = 115, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_17 = Engine(name="1.6 TDI", power_hp = 110, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = octavia)
            eng_oct_18 = Engine(name="1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_19 = Engine(name="1.8 TSI", power_hp = 180, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_20 = Engine(name="1.4 TSI", power_hp = 150, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 6", model = octavia)
            eng_oct_21 = Engine(name="1.4 TSI", power_hp = 140, displacement_cc = 1395, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_22 = Engine(name="1.2 TSI", power_hp = 105, displacement_cc = 1197, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)

            # Octavia 2
            eng_oct_23 = Engine(name="2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_24 = Engine(name="2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_25 = Engine(name="1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = octavia)
            eng_oct_26 = Engine(name="2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_27 = Engine(name="1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_28 = Engine(name="1.4 TSI", power_hp = 122, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = octavia)
            eng_oct_29 = Engine(name="2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_30 = Engine(name="2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_31 = Engine(name="1.9 TDI", power_hp = 105, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_32 = Engine(name="2.0 TSI", power_hp = 200, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_33 = Engine(name="1.6 FSI", power_hp = 115, displacement_cc = 1598, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_34 = Engine(name="1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_35 = Engine(name="1.4 MPI", power_hp = 75, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)

            # Octavia 1
            eng_oct_36 = Engine(name="1.9 TDI", power_hp = 90, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_37 = Engine(name="1.9 TDI", power_hp = 110, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_38 = Engine(name="1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 4", model = octavia)
            eng_oct_39 = Engine(name="1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = octavia)
            eng_oct_40 = Engine(name="1.8 T", power_hp = 180, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_41 = Engine(name="1.8 T", power_hp = 150, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)
            eng_oct_42 = Engine(name="1.6 MPI", power_hp = 102, displacement_cc = 1595, fuel_type = "Benzina", euro_norm = "Euro 4", model = octavia)

            db.session.add_all([
                eng_oct_1, eng_oct_2, eng_oct_3, eng_oct_4, eng_oct_5, eng_oct_6, eng_oct_7, eng_oct_8,
                eng_oct_9, eng_oct_10, eng_oct_11, eng_oct_12, eng_oct_13, eng_oct_14, eng_oct_15, eng_oct_16,
                eng_oct_17, eng_oct_18, eng_oct_19, eng_oct_20, eng_oct_21, eng_oct_22, eng_oct_23, eng_oct_24,
                eng_oct_25, eng_oct_26, eng_oct_27, eng_oct_28, eng_oct_29, eng_oct_30, eng_oct_31, eng_oct_32,
                eng_oct_33, eng_oct_34, eng_oct_35, eng_oct_36, eng_oct_37, eng_oct_38, eng_oct_39, eng_oct_40,
                eng_oct_41, eng_oct_42
            ])

        superb = Model.query.filter_by(name="Superb").first()
        if superb:
            # Superb 3 and Superb 4
            eng_sup_1 = Engine(name="2.0 TDI", power_hp = 150, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_2 = Engine(name="2.0 TDI", power_hp = 190, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_3 = Engine(name="2.0 TDI Evo", power_hp = 200, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_4 = Engine(name="2.0 TSI 4x4", power_hp = 280, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_5 = Engine(name="2.0 TSI 4x4", power_hp = 272, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_6 = Engine(name="1.5 TSI", power_hp = 150, displacement_cc = 1498, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)
            eng_sup_7 = Engine(name="1.4 TSI iV", power_hp = 218, displacement_cc = 1395, fuel_type = "Hybrid", euro_norm = "Euro 6", model = superb)
            eng_sup_8 = Engine(name="1.6 TDI", power_hp = 120, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 6", model = superb)
            eng_sup_9 = Engine(name="2.0 TSI", power_hp = 220, displacement_cc = 1984, fuel_type = "Benzina", euro_norm = "Euro 6", model = superb)

            # Superb 2
            eng_sup_10 = Engine(name="2.0 TDI", power_hp = 170, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_11 = Engine(name="2.0 TDI", power_hp = 140, displacement_cc = 1968, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_12 = Engine(name="3.6 FSI V6", power_hp = 260, displacement_cc = 3597, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)
            eng_sup_13 = Engine(name="1.8 TSI", power_hp = 160, displacement_cc = 1798, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)
            eng_sup_14 = Engine(name="1.6 TDI", power_hp = 105, displacement_cc = 1598, fuel_type = "Diesel", euro_norm = "Euro 5", model = superb)
            eng_sup_15 = Engine(name="1.4 TSI", power_hp = 125, displacement_cc = 1390, fuel_type = "Benzina", euro_norm = "Euro 5", model = superb)

            # Superb 1
            eng_sup_16 = Engine(name = "1.9 TDI", power_hp = 131, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = superb)
            eng_sup_17 = Engine(name="2.5 TDI V6", power_hp = 163, displacement_cc = 2496, fuel_type = "Diesel", euro_norm = "Euro 4", model = superb)
            eng_sup_18 = Engine(name="1.8 T", power_hp = 150, displacement_cc = 1781, fuel_type = "Benzina", euro_norm = "Euro 4", model = superb)
            eng_sup_19 = Engine(name="2.8 V6", power_hp = 193, displacement_cc = 2771, fuel_type = "Benzina", euro_norm = "Euro 4", model = superb)
            eng_sup_20 = Engine(name="1.9 TDI", power_hp = 101, displacement_cc = 1896, fuel_type = "Diesel", euro_norm = "Euro 3", model = superb)

            db.session.add_all([
                eng_sup_1, eng_sup_2, eng_sup_3, eng_sup_4, eng_sup_5,
                eng_sup_6, eng_sup_7, eng_sup_8, eng_sup_9, eng_sup_10,
                eng_sup_11, eng_sup_12, eng_sup_13, eng_sup_14, eng_sup_15,
                eng_sup_16, eng_sup_17, eng_sup_18, eng_sup_19, eng_sup_20
            ])

        db.session.commit()

if __name__ == '__main__':
    seed()
