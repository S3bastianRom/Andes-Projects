from flask import Flask, render_template
from views.controller import Controller

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home(): 
    controller = Controller()
    perro = controller.retornar_perros()
    return render_template("index.html", perro=perro)

if __name__ == "__main__":
    app.run(debug=True)