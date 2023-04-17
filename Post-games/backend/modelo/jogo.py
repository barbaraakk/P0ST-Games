from backend.geral.config import *

class Jogo(db.Model):
    # atributos do jogo
    id = db.Column(db.Integer, primary_key=True)
    ano_lacamento = db.Column(db.Text)
    genero = db.Column(db.Text)
    desenvolvedora = db.Column(db.Text)
    distribuidora = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.titulo + "[id="+str(self.id)+ "], " +\
            self.ano_lacamento + ", " + self.genero + ", " + self.desenvolvedora + ", " + self.distribuidora
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano de lançamento": self.ano_lacamento,
            "genero": self.genero,
            "desenvolvedora": self.desenvolvedora,
            "distribuidora": self.distribuidora
        }