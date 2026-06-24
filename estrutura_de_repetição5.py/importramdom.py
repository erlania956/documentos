import random
numero_secreto = random.randint(1, 10)
print("bem vindo ao jogo de adivinhação!")
print("estou pensando em um numero entre 1 e 10. Tente adivinhar!")
acertou = False
while not acertou:
    # solicita um palpite do usuario
    palpite = int(input("Digite o seu palpite: "))
        # verifica se o palpite está correto
    if palpite < numero_secreto:
        print(" o numero é maior. Tente novamente.")
    elif palpite > numero_secreto:
        print(" o numero é menor. Tente novamente.")
    else:
        print("parabéns! você acertou o numero!.")
        acertou = True