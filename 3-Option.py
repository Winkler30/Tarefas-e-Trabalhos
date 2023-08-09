# 1 - Opção

def verificar_paridade(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 10
if verificar_paridade(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


# 2 - Opção

def calcular_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media

numeros = [5, 10, 15, 20, 25]
media_calculada = calcular_media(numeros)
print(f"A média dos números é: {media_calculada:.2f}")


# 3 - Opção

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit:.2f}°F")

