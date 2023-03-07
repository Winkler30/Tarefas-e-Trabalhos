nome = input ("\n Qual o seu Nome ? ")
altura = float(input(' Digite sua Altura: '))
peso = float(input(' Digite seu Peso: '))

print(f"\nSeu nome é: {nome}")

divisao = peso / (altura * altura)
print('Resultado da Divisão:', divisao)

if peso <= 18.5:
    print("\nSeu IMC é ABAIXO DO PESO.\n")

if peso >= 18.5 and 24.9:
    print("\nSeu IMC é NORMAL.\n")    

elif peso <= 25 and 29.9:
    print("Seu IMC é SOBREPESO\n.")