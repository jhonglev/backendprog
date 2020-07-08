from config import *

class Calcado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(254))
    tamanho = db.Column(db.String(254))
    cor = db.Column(db.String(254))

    def __str__(self):
        return str(self.id)+") "+ self.modelo + ", " +\
            self.tamanho + ", " + self.cor
    def json(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "tamanho": self.tamanho,
            "cor": self.cor
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    calc1 = Calcado(modelo = "Jordan", tamanho = "40", 
        cor = "Preto")
    calc2 = Calcado(modelo = "Chinelo", tamanho = "39", 
        cor = "Branco")        

    db.session.add(calc1)
    db.session.add(calc2)
    db.session.commit()

    print(calc2)

    print(calc2.json())