from Animale import Animale


class Leone(Animale):

    def __init__(self, peso, nome, eta):
        self.peso = peso
        Animale.__init__(nome, eta)

    def info(self):
        return self.get_peso()

    def parla(self):
        return "Ruggisce"

    def muove(self):
        return "va come un fulmine"

    def mangia(self):
        return "divora"

    def beve(self):
        return "ingurgita"

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso
