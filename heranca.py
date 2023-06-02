class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerou!")
    
    def frear(self):
        print("Freou!")


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Abrindo a porta do carro.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        print("Empinando!")


carro = Carro("Ford", "Fiesta", "Azul")
moto = Moto("Honda", "CBR", 600)

print(carro.marca)  
print(moto.modelo)  

carro.acelerar()  
moto.frear()  


carro.abrir_porta() 
moto.empinar()  
