from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Aprendiendo Flask"

@app.route('/informacion/<nombre>')
def informacion(nombre):
    return f"<h1>Pagina de {nombre}</h1>"

if __name__ == "__main__":
    app.run(debug=True)