#EDIT && EXIT

import os

lista = []
os.system("cls")

while True:
    print("Selecione a opção")
    opcao = input("[i]inserir [a]apagar [l]listar [e]editar [s]sair :")

    if opcao == "i":
        os.system("cls")
        valor = input("Digite algum valor: ")
        lista.append(valor)
        print("Valor inserido com sucesso!!!")
        print("------------------------------")

    elif opcao == "a":
        os.system("cls")
        apagar = input("Qual valor deseja apagar: ")
        
        try:
            lista.remove(apagar)
            print("Valor deletado com sucesso!!!")
            print("------------------------------")
        except ValueError:
            print("Valor não encontrado")
            print("--------------------")

    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")
        else:
            for i, listageral in enumerate(lista):
                print("-------------------------")
                print(i, listageral)
        print("----------------------------------")

    elif opcao == "e":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para editar")
        else:
            try:
                editar_indice = int(input("Qual índice que deseja alterar: ")) 
                print("------------------------------")
                editar = input("Escreva o conteúdo novo: ")

                lista[editar_indice] = editar
            except (ValueError, IndexError):
                print("Valor não encontrado ou índice inválido.")
        print("---------------------------------------------------------")

    elif opcao == "s":
        os.system("cls")
        lista.clear()
        print("Sistema finalizado")
        break
    else:
        os.system("cls")
        print("Por favor, escolha i, a, l, e, s")
