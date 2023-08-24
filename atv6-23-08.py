class Motor:
    def ligar(self):
        print("Motor ligado")

    def desligar(self):
        print("Motor desligado")

class Asa:
    def __init__(self, lado):
        self.lado = lado

    def dobrar(self):
        print(f"Asa do lado {self.lado} dobrada")

class Aviao:
    def __init__(self):
        self.motor = Motor()
        self.asa_esquerda = Asa("esquerdo")
        self.asa_direita = Asa("direito")  

    def ligar(self):
        print("Avião ligado")
        self.motor.ligar()

    def desligar(self):
        print("Avião desligado")
        self.motor.desligar()

    def dobrar_asas(self):
        self.asa_esquerda.dobrar()
        self.asa_direita.dobrar()

meu_aviao = Aviao()
meu_aviao.ligar()
meu_aviao.dobrar_asas()
meu_aviao.desligar()
