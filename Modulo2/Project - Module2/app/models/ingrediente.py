from sqlalchemy import Column, String, Float, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from ..config.db import db

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column(db.String(500), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo = db.Column(db.Enum("base", "complemento", name="tipo_ingrediente"), nullable=False)
    sabor = db.Column(db.String(100), nullable=True)


    ingrediente_productos = relationship("Producto_Ingrediente", back_populates="ingrediente")