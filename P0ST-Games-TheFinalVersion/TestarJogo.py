from geral.config import *
from modelo.jogo import Jogo

def run():
    print("TESTE DO JOGO")
    
    p1 = Jogo(titulo = "Forza",ano = "2001", genero = "Corrida", desenvolvedora = "EA", distribuidora = "Xbox")
    p2 = Jogo(titulo = "Sonic",ano = "2007", genero = "Tiro", desenvolvedora = "Sony", distribuidora = "Playstation")        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1, p2)