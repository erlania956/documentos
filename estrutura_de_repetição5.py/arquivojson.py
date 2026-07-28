import json
lista
Animal = {
    "Nome do animal":"thor",
    "espécie": "Canina",
    "idade": "3", 
}
with open("Animal.json", "w") as arquivo:
    json.dump(Animal, arquivo, indent=4)
              
def Cadastrar_animal():
    #Captura o nome para usar como chave principal)
    nome_chave = input("Digite o nome do animal: ")
    #Cria um dicionário para os dados do animal
    novo_animal = {}
    novo_animal["nome"] = input("Digite o nome do animal: ")
    novo_animal["especie"] = input("Digite a especie do animal: ")
    novo_animal["idade"] = float(input("Digite a idade do animal? (em anos)"))
        #Associa nome aos Dados do animal
    animais[nome_chave] = novo_animal
    print(f"animal {novo_animal['nome']} cadastrado com sucesso!")
