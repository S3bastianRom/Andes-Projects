from ..config.db import db

class Cuidadores(db.Model):
    __tablename__ ='cuidadores'
    #PK
    id = db.Column(db.Integer, primary_key = True, nullable = False ,autoincrement = True)
    nombre = db.Column (db.String(500))
    telefono = db.Column (db.String(500))
    #FK
    #id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderia.id'))