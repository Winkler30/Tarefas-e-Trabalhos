nome = input("\nQual o seu Nome? ")
altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))

print(f"\nSeu nome é: {nome}")

imc = peso / (altura * altura)
print('Resultado da Divisão:', imc)

if imc <= 18.5:
    print("\nSeu IMC é ABAIXO DO PESO.\n")

elif imc >= 18.5 and imc <= 24.9:
    print("\nSeu IMC é NORMAL.\n")    

elif imc >= 25 and imc <= 29.9:
    print("Seu IMC é SOBREPESO.\n")

else:
    print("Seu IMC é OBESIDADE.\n")