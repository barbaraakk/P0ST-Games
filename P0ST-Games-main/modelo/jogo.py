from geral.config import *

class Jogo(db.Model):
    # atributos do jogo
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text)
    ano_lancamento = db.Column(db.Text)
    genero = db.Column(db.Text)
    desenvolvedora = db.Column(db.Text)
    distribuidora = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.titulo + "[id="+str(self.id)+ "], " +\
            self.ano_lancamento + ", " + self.genero + ", " + self.desenvolvedora + ", " + self.distribuidora
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano de lançamento": self.ano_lancamento,
            "genero": self.genero,
            "desenvolvedora": self.desenvolvedora,
            "distribuidora": self.distribuidora
        }