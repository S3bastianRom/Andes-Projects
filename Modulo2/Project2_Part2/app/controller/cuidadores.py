from flask import Blueprint, render_template, request
from ..config.db import db
from ..model.cuidadores import Cuidadores
from ..model.perro import Perro

cuidadores_bp = Blueprint ("cuidadores", __name__, url_prefix="/cuidadores")

@cuidadores_bp.route("/")
def root():
    cuidador = Cuidadores.query.all()
    return render_template("index_cuidadores.html", cuidadores = cuidador)

@cuidadores_bp.route("/<int:id>")
def get_one_takecarer (id):
    rows = Cuidadores.query.get_or_404(id)
    return render_template("carer.html", cuidadores = rows)

@cuidadores_bp.route("/update/<int:id>", methods=["GET"])
def assign_small(id):
    cuidador = Cuidadores.query.get(id)
    perros_pequenos = Perro.query.filter(Perro.peso < 3).all()
    for perro in perros_pequenos:
        perro.id_cuidador = cuidador.id
    db.session.commit()

    return f"Perros pequeños asignados exitosamente a {cuidador.nombre}"