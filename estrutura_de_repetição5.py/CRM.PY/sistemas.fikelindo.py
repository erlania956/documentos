clientes = {
    "12345678901":{"nome": "Ana Silva", "Idade": 28, "Compras": [120.50, 89.900,45.00], "categoria": "vip"},
    "98765432100":{"nome": "Bruno Costa", "Idade": 34, "Compras": [350.00, 500.00], "categoria": "premium"},
    "45678912344":{"nome": "Carla Souza", "Idade": 22, "Compras": [50.00], "categoria": "Regular"},
    "78912345655":{"nome": "Diego Lima", "Idade": 41, "Compras": [15.00, 30.00, 25.50, 40.00], "categoria": "Regular"},
}   
def cadastrar_cliente():
    #captura o CPF para usar como chave principal)
    cpf_chave = input("Digite o CPF do cliente: ")
    #Cria um dicionario para os dados do cliente
    novo_cliente = {}
    novo_cliente["nome"] = input("Digite o nome do cliente: ")
    novo_cliente["idade"] = int(input("Digite a idade do cliente: "))
    novo_cliente["compras"] = []
    novo_cliente["categoria"] = "Regular"
    #Associa CPF aos dados do cliente no banco global
    clientes[cpf_chave] = novo_cliente
    print(f"cliente {novo_cliente["nome"]}cadastrado com sucesso!")


def listar_clientes():
    if not clientes:
        print("nenhum cliente cadastrado.")