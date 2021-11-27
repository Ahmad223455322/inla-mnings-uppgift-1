from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ahmad123.@localhost/Test' 
db = SQLAlchemy(app)


class Skötare(db.Model):
        __tablename__ = "Skötare"
        ID= db.Column(db.Integer, primary_key=True)
        Namn= db.Column(db.String(30), unique=False, nullable=False)
        Animals = db.relationship('Animal', backref='Skötare', lazy=True)

class Animal(db.Model):
    __tablename__ = "Animal"
    ID= db.Column(db.Integer, primary_key=True)
    Typ=  db.Column(db.String(20), unique=False, nullable=False)
    Namn= db.Column(db.String(30), unique=False, nullable=False)
    Vikt=  db.Column(db.Integer, unique=False, nullable=True)
    Skotare_id=db.Column(db.Integer, db.ForeignKey('Skötare.ID'),nullable=False)
    

db.create_all()

while True:
    print("1. Skapa djur")
    print("2. lista alla")
    print("3. uppdatera")
    print("4. sök")
    print("11. Skapa Skötare")
    print("12. Lista skötare")

    sel =input("Val:")
    if sel == "1":
        a=Animal()
        a.Namn = input("Ange nman")
        a.Typ=input("ange typ")
        a.Vikt=input("ange vikt")
        for skot in Skötare.query.all():
            print(f"Id:{skot.ID} {skot.Namn}")
        a.Skotare_id = int(input("Ange ID för djurets Skötare:"))
        db.session.add(a)
        db.session.commit()

    if sel =="2":
        for a in Animal.query.all(): 
            print(f"{a.Typ} {a.Namn} ")

    
    if sel =="3":
        for a in Animal.query.all(): 
            print(f"{a.ID} {a.Namn} ")
        selectedId = int("ange id på djuret") 
        djurattuppdatera = Animal.query.filter_by(ID=selectedId).first()
        djurattuppdatera.Namn = input("Ange nytt namn:") 
        djurattuppdatera.Typ = input("Ange nytt typ:") 
        db.session.commit()
    
    
    
    if sel == "11":
       s = Skötare()
       s.Namn = input("Ange namn:")
       db.session.add(s)
       db.session.commit()  
    
    if sel == "4":
        sök = input("Sök efter:")
        print("Sökresultat")
        for m in Animal.query.filter(Animal.Namn.contains(sök)).all():
            print(f"{m.ID} {m.Namn}")
        print("Slut sök")

          

    

 
