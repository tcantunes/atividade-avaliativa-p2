class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito realizado. Saldo atual: {self._saldo}")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque realizado. Saldo atual: {self._saldo}")
        else:
            print("Saldo insuficiente. Saque não realizado.")

    def get_saldo(self):
        return self._saldo


conta = Conta(1000)

print(conta._saldo)  

conta.depositar(500) 
conta.sacar(200) 


print(conta.get_saldo())  
