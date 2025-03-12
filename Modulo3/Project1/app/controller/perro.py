from app.model.perro import Perro
from app.utils.decorators import admin_required, user_required

from flask_login import login_required
from flask import Blueprint, render_template, flash

perros_bp = Blueprint ("perro", __name__, url_prefix="/perro")


@perros_bp.route("/")
@login_required
@admin_required
def root():
    perritos = Perro.query.all()
    flash ('Estos son los perros', 'success')
    return render_template("index_perro.html", perritos = perritos)

@perros_bp.route("/<string:nombre>")
@login_required
@user_required
def get_perros_qty(nombre):
    perro = Perro.query.filter_by(nombre=nombre).all()
    number = len (perro)
    return render_template("lassie.html", nombre=nombre, perros=number)