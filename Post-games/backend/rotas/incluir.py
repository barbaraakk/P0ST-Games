from backend.geral.config import *
from backend.modelo.jogo import *

@app.route("/incluir/<string:classe>", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        # cria a pessoa
        nova = Jogo(**dados)
        # realiza a persistência da nova pessoa
        db.session.add(nova)
        db.session.commit()
        # tudo certo :-) resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes": str(e)})