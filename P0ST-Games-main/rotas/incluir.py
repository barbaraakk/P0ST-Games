from geral.config import *
from modelo.jogo import *

@app.route("/", methods=['POST'])
def incluir():
    dados = request.get_json()
    # cria o jogo
    nova = Jogo(**dados)
    # realiza a persistência do novo jogo
    db.session.add(nova)
    db.session.commit()
    return render_template('index.html')