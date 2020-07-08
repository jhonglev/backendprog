class Calçado:

    def __init__(self, modelo="", tamanho="", cor="", marca=""):
        self.modelo = modelo
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return " \n Modelo: " + self.modelo + ", \n Tamanho: " + \
        self.tamanho + ", \n Cor: " + self.cor + ", \n Marca: " + \
        self.marca


if __name__ == "__main__":

    jordan = Calçado()
    jordan.modelo = "Jordan"
    jordan.tamanho = "40"
    jordan.cor = "Preto"
    jordan.marca = "Jordan"

    chinelo = Calçado()
    chinelo.modelo = "Chinelo"
    chinelo.tamanho = "39"
    chinelo.cor = "Branco"
    chinelo.marca = "Havaianas"

    print(jordan,"\n", chinelo)
