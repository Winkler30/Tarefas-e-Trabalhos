class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        self.saldo -= valor + taxa

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para o saque.")

conta_poupanca = ContaPoupanca("João", 1000)
conta_poupanca.sacar(200)
print(f"Saldo da conta poupança: R${conta_poupanca.saldo:.2f}")

conta_corrente = ContaCorrente("Maria", 1500, 500)
conta_corrente.sacar(2000)
print(f"Saldo da conta corrente: R${conta_corrente.saldo:.2f}")

conta_corrente.sacar(1000)
print(f"Saldo da conta corrente: R${conta_corrente.saldo:.2f}")
