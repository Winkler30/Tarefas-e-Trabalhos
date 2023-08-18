class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor
        
motor_gasolina = Motor("Gasolina", 700)

meu_carro = Carro(motor_gasolina)

print("Tipo de motor:", meu_carro.motor.tipo) 
print("Potência do motor:", meu_carro.motor.potencia)
