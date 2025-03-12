from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.es_admin:
            flash("Access denied. Admins only!", "danger")
            return redirect(url_for('login.user_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in first.", "warning")
            return redirect(url_for('login'))
        if current_user.es_admin:
            flash("Admins cannot access this page.", "danger")
            return redirect(url_for('login.admin_dashboard'))
        return f(*args, **kwargs)
    return decorated_function
