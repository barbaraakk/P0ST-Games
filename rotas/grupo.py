from geral.config import *
from modelo.jogo import *

@app.route("/grupo")
def grupo():
    return render_template('grupo.html')