from sqlalchemy.orm import relationship
from ..config.db import db

class Producto_Ingrediente(db.Model):
    __tablename__ = "producto_Ingrediente"

    id = db.Column(db.String(500), primary_key=True, nullable= False)
    producto_id = db.Column(db.String(500), db.ForeignKey ('productos.id'), nullable= False)
    ingrediente_id =  db.Column (db.String(500), db.ForeignKey ('ingredientes.id'), nullable= False)

    producto = relationship("Producto", back_populates="producto_ingredientes")
    ingrediente = relationship("Ingrediente", back_populates="ingrediente_productos")