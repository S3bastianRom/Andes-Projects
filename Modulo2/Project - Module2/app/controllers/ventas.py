from flask import Blueprint, render_template, flash, redirect, url_for
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria

ventas_bp = Blueprint ("ventas", __name__, url_prefix= "/ventas")

#Modulo ventas 
@ventas_bp.route("/")
def ventas():
    productos = Producto.query.all()
    return render_template("ventas.html", productos = productos)


@ventas_bp.route("/vender/<string:nombre>")
def vender(nombre):
    heladeria = Heladeria.query.first()

    try:
        heladeria.vender(nombre)
        db.session.commit()
        flash("¡Vendido!", "success")
    except ValueError as e:
        db.session.rollback()
        flash(f"¡Oh no! Nos hemos quedado sin {str(e)}", "danger")

    return redirect(url_for("ventas.ventas"))


@ventas_bp.route("/mejor_producto")
def mejor_producto ():
    heladeria = Heladeria.query.first()

    try:
        mejor = heladeria.obtener_mejor_producto()
        flash(f"El producto más rentable es: {mejor}", "success")
    except ValueError as e:
        flash(str(e), "danger")

    return redirect(url_for("index.ventas"))