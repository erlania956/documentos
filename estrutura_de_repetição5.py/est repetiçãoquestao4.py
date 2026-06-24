cont = 0
senha = input("digite a sua senha")
while True:
    if senha == "luna":
        print("seja bem vindo")
        break
    else:
        cont = cont + 1
        if cont < 3:
            print("acesso negado, voce tem:", 3 - cont, "tentativas")   
            senha = input("tente novamente")  
        else:
            print("bloqueado, acabaram as tentativas :/ ")
            break
print("fim") 