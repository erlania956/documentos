cont = 0
senha = input("digite a sua senha")
while True:
    if senha == "luna":
        print("seja bem vindo")
        break
    else:
        cont = cont + 1
        if cont < 3:
            print("acesso negado")   
            senha = input("tente novamente")  
        else:
            print("bloqueado")
            break
print("fim")         