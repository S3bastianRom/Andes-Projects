from app.config.auth import login_manager
from app.model.usuario import Usuario
from app.utils.decorators import admin_required, user_required
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import check_password_hash

login_bp = Blueprint ("login", __name__, url_prefix="/login")

@login_manager.user_loader
def load_user(user_id:int):
    return Usuario.query.get(int(user_id))


@login_bp.route("/")
def login():
    return render_template ('login.html')

@login_bp.route('/admin')
@admin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@login_bp.route('/user')
@user_required
def user_dashboard():
    return render_template('user_dashboard.html', user = current_user)



@login_bp.route("/auth")
def auth ():
    username = request.args.get("username")
    password = request.args.get("password")

    user = Usuario.query.filter_by (username = username, password = password).first()

    if user:
        login_user(user)
        flash ('Inicio de sesio completo', 'success')

        if user.es_admin:
            return redirect(url_for('login.admin_dashboard'))
        else:
            return redirect(url_for('login.user_dashboard'))
    
    else:
        flash('Credenciales incorrectas, revisa', 'danger')
        return render_template('login.html')

@login_bp.route("/auth/profile")
@login_required
def  auth_profile ():
    return f"Bienvenido, {current_user.username}"


@login_bp.route("/logout")
def logout():
    logout_user()
    return render_template ('login.html')