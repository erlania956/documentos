combustivel = float(input("qual quantidade de combustivel disponivel:"))
atm = input("a atmosfera é respiravel?")
traje = float(input("qual a sua integridade?"))
if combustivel >= 15 and (atm == "boa" or traje == 100):
    print("pouso autorizado")
else:
    print("nao autorizado")