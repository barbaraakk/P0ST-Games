from geral.config import *
from TestarJogo import *

# inserindo a aplicação em um contexto :-/
with app.app_context():
    TestarJogo.run()