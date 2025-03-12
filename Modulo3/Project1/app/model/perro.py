from ..config.db import db

class Perro(db.Model):
    __tablename__ ='perro'
    #PK
    id = db.Column(db.Integer, primary_key = True, nullable = False ,autoincrement = True)
    #Columns
    nombre = db.Column (db.String(500))
    raza  = db.Column (db.String(500))
    edad = db.Column (db.Integer)
    peso = db.Column (db.Float)
    #FKs
    #id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderia.id'))
    id_cuidador = db.Column (db.Integer, db.ForeignKey('cuidadores.id'))