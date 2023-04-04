numeros = [] 

print("\nDigite 5 numeros inteiros aleatórios para termos a soma no final\n")
for i in range(1,6):
    num = int(input(f"Digite o {i}"+ " número: " ))
    numeros.append(num)

soma = 0 

for num in numeros:
    soma += num

print(f"\nA soma dos números digitados é: {soma}\n")
