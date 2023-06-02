class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


class Papagaio(Animal):
    def falar(self):
        return "Oi Oi!"


def fazer_som(animal):
    print(animal.falar())


cachorro = Cachorro()
gato = Gato()
papagaio = Papagaio()

fazer_som(cachorro) 
fazer_som(gato)  
fazer_som(papagaio)  
