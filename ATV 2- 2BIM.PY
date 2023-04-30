import numpy as np

class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores

    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])

    def imprime_jogadores(self):
        jogadores_array = np.array(self.jogadores)
        print("Jogadores do time", self.nome)
        print(np.array2string(jogadores_array, separator=', '))

time1 = Time('Time A', [['Charles', 10], ['Gustavo', 5], ['Suel', 8]])

nome_jogador = input("Digite o nome do novo jogador: ")
camisa_jogador = int(input("Digite o número da camisa do novo jogador: "))
time1.adiciona_jogador(nome_jogador, camisa_jogador)

time1.imprime_jogadores()
