opcao = int(input("1 p/ ponte, 2p/ tunel, escolha:"))
if opcao == 1:
    carro = input("o carro é blindado? ")
    ponte = input("ponte ok? ")
    if carro == "sim" and ponte =="sim":
        print("FUGA OK") 
    else:  
        print("morte")
elif opcao == 2:
    marcara = input("tem marcara? ")
    cartao = input("tem cartao? ")
    if marcara= "sim" and ponte =="sim":
