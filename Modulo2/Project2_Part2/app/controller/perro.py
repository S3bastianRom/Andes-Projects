from ..config.db import execute_query
from ..model.perro import Perro
from flask import Blueprint, render_template
from sqlalchemy import text

perros_bp = Blueprint ("perro", __name__, url_prefix="/perro")

@perros_bp.route("/")
def root():
    perritos = Perro.query.all()
    return render_template("index_perro.html", perritos = perritos)

@perros_bp.route("/<string:nombre>")
def get_perros_qty(nombre):
    perro = Perro.query.filter_by(nombre=nombre).all()
    number = len (perro)
    return render_template("lassie.html", nombre=nombre, perros=number)