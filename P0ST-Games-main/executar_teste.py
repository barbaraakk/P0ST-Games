from geral.config import *
from TestarJogo import run

# inserindo a aplicação em um contexto :-/
with app.app_context():
    run()