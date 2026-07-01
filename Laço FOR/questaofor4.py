numero = int(input("qual fatorial voce deseja? "))
resultado = 1
for i in range(1, numero + 1):
    resultado *= i
print(f" o fatorial de {numero} é {resultado}")
