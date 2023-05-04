from geral.config import *
from rotas.listar import *
from rotas.incluir import *
from modelo.jogo import *

# rota padrão
@app.route("/")
def inicio():
    return "oi, comece aqui: <a href=/home>home</a>"#render_template("index.html")

@app.route("/home")
def home():
    return render_template("index2.html")


@app.route("/novo_listar")
def novo_listar():
    return render_template("listar.html")

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True, host="0.0.0.0")