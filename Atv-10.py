def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print(f"A média dos números na lista {lista_numeros} é {media:.2f}")
