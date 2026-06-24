
idade =int(input("digite a sua idade"))
tem_titulo = (input("possui titulo de eleitor"))

if idade >= 16 and tem_titulo =="sim":
    print("pode votar")
else:
    print("não pode votar")
