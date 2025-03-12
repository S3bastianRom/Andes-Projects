from flask_login import LoginManager
from flask import Flask
from app.model.usuario import Usuario
from app.config.config import Config
from app.config.db import db
from app.config.routes import register_routes
from app.config.auth import login_manager


app = Flask(__name__, template_folder="app/views")
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
register_routes(app)

with app.app_context():
    db.create_all()
    Usuario.create_test_users()

if __name__ == "__main__":
    app.run(debug=True)