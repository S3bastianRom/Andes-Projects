from flask import Blueprint, render_template, flash, redirect, url_for
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria

index_bp = Blueprint ("index", __name__, url_prefix= "/index")

#Index
@index_bp.route("/")
def index():
    return render_template("home.html")

#Menu de comida
@index_bp.route("/menu")
def menu():
    productos = Producto.query.all()
    return render_template("menu.html", productos = productos)




