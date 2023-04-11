def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade, distancia, litros_usados):
    print(f"Velocidade média: {velocidade:.2f} km/h")
    print(f"Tempo gasto: {tempo:.2f} horas")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Litros utilizados: {litros_usados:.2f}")

tempo_gasto, velo_media = ler_valores()
distancia_percorrida = calcular_distancia(tempo_gasto, velo_media)
litros_utilizados = calcular_litros(distancia_percorrida)
apresentar_resultado(tempo_gasto, velo_media, distancia_percorrida, litros_utilizados)
