from sqlalchemy.orm import relationship
from ..config.db import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.String(500), primary_key=True)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum("Copa", "Malteada", name="tipo_producto"), nullable=False)
    tipo_vaso = db.Column(db.String(100), nullable=True)
    volumen = db.Column(db.Float, nullable=True)

    producto_ingredientes = relationship("Producto_Ingrediente", back_populates="producto")