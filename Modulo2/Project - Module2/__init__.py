from flask import Flask
from app.config.config import Config
from app.config.db import db
from app.models.producto import Producto
from app.models.ingrediente import Ingrediente
from app.models.producto_ingrediente import Producto_Ingrediente


app = Flask(__name__, template_folder="app/views")
app.config.from_object(Config)
db.init_app(app)