def ler_temp():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    return celsius

def converter_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrar_resultado(fahrenheit):
    print("A temperatura em graus Fahrenheit é:", fahrenheit)

def ler_temp2():
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    return fahrenheit

def converter_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def mostrar_resultado(celsius):
    print("A temperatura em graus Fahrenheit é:", celsius)

temp_celsius = ler_temp()
temp_fahrenheit = converter_para_fahrenheit(temp_celsius)
mostrar_resultado(temp_fahrenheit)

temp_fahrenheit = ler_temp2()
temp_celsius = converter_para_celsius(temp_fahrenheit)
mostrar_resultado(temp_celsius)

