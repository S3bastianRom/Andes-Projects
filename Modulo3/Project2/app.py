from flask import Flask, jsonify, render_template
import json
from app.boa_constrictor import Boa_Constrictor
from app.huron import Huron
from app.gato import Gato
from app.perro import Perro

animales = {
    "gato": Gato("Gato", 4.5, 3),
    "perro": Perro("Perro", 10.0, 5),
    "huron": Huron("Hurón", 2.0, 3, "Canadá", 0.1),
    "boa": Boa_Constrictor("Boa", 10.0, 5, "Brasil", 0.2)
}

app = Flask(__name__)

@app.route('/')
def index():
    return "Cambia la URL a /sonido/Animal  [Recuerda que Hay Perro, Gato, Boa y huron]"

@app.route('/sonido/<animal>', methods=['GET'])
def obtener_sonido(animal):
    animal_obj = animales.get(animal.lower())
    if animal_obj:
        response = {"animal": animal, "sonido": animal_obj.hacer_sonido()}
        return app.response_class(
            response=json.dumps(response, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    return jsonify({"error": "Animal no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)