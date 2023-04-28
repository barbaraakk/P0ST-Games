from geral.config import *
from rotas.listar import *
from modelo.jogo import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True)
