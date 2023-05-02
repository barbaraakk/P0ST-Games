from geral.config import *
from modelo.jogo import Jogo

def run():
    print("TESTE DO JOGO")
    
    p1 = Jogo(ano_lancamento = "20/11/2001", genero = "Corrida", desenvolvedora = "EA", distribuidora = "não sei")
    p2 = Jogo(ano_lancamento = "01/07/2020", genero = "Tiro", desenvolvedora = "Sony", distribuidora = "não sei 2")        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1, p2)