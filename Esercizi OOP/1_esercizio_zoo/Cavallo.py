from Animale import Animale


class Cavallo(Animale):

    def __init__(self, mantello, nome, eta):
        self.mantello = mantello
        Animale.__init__(nome, eta)

    def info(self):
        return self.get_mantello()

    def parla(self):
        return "nitrisce"

    def muove(self):
        return "galoppa"

    def mangia(self):
        return "mangia"

    def beve(self):
        return "si abbevera"

    def get_mantello(self):
        return self.mantello

    def set_mantello(self, mantello):
        self.mantello = mantello
