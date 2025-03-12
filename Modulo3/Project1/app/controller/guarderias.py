from ..model.guarderias import Guarderia
from flask import Blueprint, render_template

guarderia_bp = Blueprint ("guarderia", __name__, url_prefix="/guarderias")

@guarderia_bp.route("/")
def root():
    guarderias = Guarderia.query.all()
    return render_template("index_guarderia.html", guarderias = guarderias)