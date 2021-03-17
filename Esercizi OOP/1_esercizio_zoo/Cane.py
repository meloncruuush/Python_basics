from Animale import Animale


class Cane(Animale):

    def __init__(self, razza, nome, eta):
        self.razza = razza
        Animale.__init__(nome, eta)

    def info(self):
        return self.get_razza()

    def parla(self):
        return "abbaia"

    def muove(self):
        return "corre"

    def mangia(self):
        return "mangia"

    def beve(self):
        return "beve"

    def get_razza(self):
        return self.razza

    def set_razza(self, razza):
        self.razza = razza
