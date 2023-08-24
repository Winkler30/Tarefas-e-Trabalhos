class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco

    def detalhes(self):
        return f"Cor: {self.cor}, Preço: R${self.preco:.2f}"

class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas

    def detalhes(self):
        veiculo_detalhes = super().detalhes()
        return f"{veiculo_detalhes}, Número de Portas: {self.numero_portas}"

class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo

    def detalhes(self):
        veiculo_detalhes = super().detalhes()
        return f"{veiculo_detalhes}, Tipo: {self.tipo}"

carro = Carro("Azul", 30000, 4)
print(carro.detalhes())

bicicleta = Bicicleta("Vermelha", 1500, "Montanha")
print(bicicleta.detalhes())
