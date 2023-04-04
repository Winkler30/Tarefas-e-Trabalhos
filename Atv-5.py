numeros = [] 

print("\nDigite 5 numeros inteiros aleatórios para termos a soma no final\n")
for i in range(5):
    num = int(input(f"Digite o {i+1}"+ " número: " ))
    numeros.append(num)

soma = 0 

for num in numeros:
    soma += num

print(f"\nA soma dos números digitados é: {soma}\n")
