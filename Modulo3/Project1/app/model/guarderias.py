from ..config.db import db

class Guarderia(db.Model):
    __tablename__ ='guarderias'
    #PK
    id = db.Column(db.Integer, primary_key = True, nullable = False ,autoincrement = True)
    nombre = db.Column (db.String(500))
    direccion  = db.Column (db.String(500))
    telefono = db.Column (db.String(500))
