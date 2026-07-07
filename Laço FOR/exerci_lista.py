convidados = []
while True:
    print("""=========Menu=========)
        1 - Adicionar convidado
        2 - Listar convidados
        3 - consultar convidados
        4 - remover convidado
        5 - Quantidade de convidados
        6 - Editar convidado
        0 - Sair\n""")
    opção = int(input("digite a opção desejada: "))

    if opção == 1:
        #Adicionar convidado
        convidados.append(input("digite o nome do convidado: "))

    elif opção == 2:
        #listar convidados
        print("lista de convidados:")
        for i in convidados:
            print(i)

    elif opção == 3:
        nome = input("digite o nome do candidado a ser consultado: ")
        if nome in convidados:
            print(f"{nome} está na lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")

    elif opção == 4:
        nome = input("digite o nome a ser removido: ")
        if nome in convidados:
            convidados.remove(nome)
            print(f"{nome} removido da lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")
    
    elif opção == 5:
        print(f"quantidade de convidados:{len(convidados)}\n")

    elif opção == 6:
        nome_antigo = input("digite o nome do candidato a ser editado: ")
        if nome_antigo in convidados:
            nome_novo = input("digite o nome do candidato : ")
            index = convidados.index(nome_antigo)
            convidados[index] = nome_novo
            print(f"{nome_antigo} foi atualizado para {nome_novo}.\n")
        else:
            print(f"{nome_antigo} não está na lista de convidados.\n")
    
    elif opção == 0:
        print("saindo do programa...")
        break
    else:
        print("opção inválida. tente novamente.\n")


            
    

         
        
              
        