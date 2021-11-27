# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ahmad123.@localhost/Falsk' 
# db = SQLAlchemy(app)


# class Employee(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     namn=db.Column(db.String(30), unique=False, nullable=False)
#     ålder= db.Column(db.Integer, unique=False, nullable=True)
#     anstälningdatum = db.Column(db.DateTime, unique=False, nullable=True)


# db.create_all()


# while True:
#     print("1. Skapa ")
#     print("2. söka på namn")
#     print("3. uppdatera")

#     sel =input("Val:")
#     if sel == "1":
#         a=Employee()
#         a.namn = input("Ange nman")
#         a.ålder=input("ange ålder")
#         a.anstälningdatum=input("antälning datum")
#         db.session.add(a)
#         db.session.commit()

    
#     if sel == "2":
#         sök = input("Sök efter:")
#         print("Sökresultat")
#         for m in Employee.query.filter(Employee.namn.contains(sök)).all():
#             print(f"{m.id} {m.namn}")
#         print("Slut sök")

          
    


#     if sel == "3":
#         for a in Employee.query.all(): 
#             print(f"{a.id} {a.namn} ")
#         selectedId = int(input("ange id på anställd"))
#         anstälduppdatera = Employee.query.filter_by(id=selectedId).first()
#         anstälduppdatera.namn = input("Ange nytt namn:") 
#         anstälduppdatera.ålder = input("Ange nytt ålder:") 
#         db.session.commit()
    
        


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ahmad123.@localhost/Musik' 
db = SQLAlchemy(app)


class Artist(db.Model):
    __tablename__ = "Artist"
    id= db.Column(db.Integer, primary_key=True)
    namn=db.Column(db.String(30), unique=False, nullable=False)
    Födelseår= db.Column(db.Integer, unique=False, nullable=True)
    Albumer = db.relationship('Album', backref='Artist', lazy=True)


class Album(db.Model):
        __tablename__ = "Album"
        id= db.Column(db.Integer, primary_key=True)
        Namn= db.Column(db.String(30), unique=False, nullable=False)
        årtal= db.Column(db.Integer, unique=False, nullable=True)
        Artist_id=db.Column(db.Integer, db.ForeignKey('Artist.id'),nullable=False)
        Låtar = db.relationship('Låt', backref='Album', lazy=True)
        


class Låt(db.Model):
        __tablename__ = "Låt"
        id= db.Column(db.Integer, primary_key=True)
        Namn= db.Column(db.String(30), unique=False, nullable=False)
        längd= db.Column(db.Integer, unique=False, nullable=True)
        Album_id=db.Column(db.Integer, db.ForeignKey('Album.id'),nullable=False)


db.create_all()



while True:
    print("1. Skapa ")
    print("2. söka på namn")
    print("3. uppdatera")

    sel =input("Val:")
    if sel == "1":
        a=Artist()
        a.namn = input("Ange nman")
        a.Födelseår=input("ange ålder")
        db.session.add(a)
        db.session.commit()




       