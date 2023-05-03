from geral.config import *
from rotas.listar import *
from modelo.jogo import *

# rota padrão
@app.route("/")
def inicio():
    return render_template("index.html")

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True)