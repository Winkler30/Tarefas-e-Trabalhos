class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def Depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso.")
        self.Imprimir_saldo()

    def Sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
            self.Imprimir_saldo()
        else:
            print("Saldo insuficiente.")

    def Imprimir_saldo(self):
        print("O saldo atual da conta é de R$", self.saldo)

numero_conta = int(input("Digite o número da conta: "))
nome_titular = input("Digite o nome do titular da conta: ")
saldo = float(input("Digite o saldo inicial da conta: "))

conta = ContaBancaria(numero_conta, nome_titular, saldo)
conta.Depositar(float(input("Digite o valor a ser depositado: ")))
conta.Sacar(float(input("Digite o valor a ser sacado: ")))
