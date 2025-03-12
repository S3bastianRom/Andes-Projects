from ..controller.home_controller import home_blueprint
from ..controller.guarderias import guarderia_bp
from ..controller.cuidadores import cuidadores_bp
from ..controller.perro import perros_bp
from ..controller.login import login_bp

def register_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(guarderia_bp)
    app.register_blueprint(cuidadores_bp)
    app.register_blueprint(perros_bp)
    app.register_blueprint(login_bp)