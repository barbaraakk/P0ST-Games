from backend.geral.config import *
from backend.modelo.jogo import *

@app.route("/listar/<string:classe>")
def listar(classe):
    # obter os dados da classe informada
    dados = None
    if classe == "Jogo":
        dados = db.session.query(Jogo).all()
    
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})