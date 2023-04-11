import numpy as np 

dieimes_matriz = np.array([[2,3,1],[4,5,7]])

for i in range (dieimes_matriz.shape[0]):
 print(dieimes_matriz[i])

soma = 0

for linha in dieimes_matriz:

    for soma_matriz in linha:

        soma = soma + soma_matriz

print("A soma de todos os elementos da matriz é:", soma)
