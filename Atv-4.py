lista_de_compras = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar item à lista")
    print("2 - Remover item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair do programa")

    opcao = input("\n= ")

    if opcao == "1":
        item = input("\nDigite o nome do item para adicionar à lista de compras: ")
        lista_de_compras.append(item)
        print(f"{item} adicionado à lista.")

   
    elif opcao == "2":
        item = input("Digite o nome do item que deseja remover da lista de compras: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")

    
    elif opcao == "3":
        print("Itens na lista de compras:")
        for item in lista_de_compras:
            print(f"- {item}")

 
    elif opcao == "4":
        print("Saindo do programa.")
        break


    else:
        print("Opção inválida.")
