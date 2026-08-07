import sqlite3

def conectar():
    return sqlite3.connect("clientes.db")


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        rg TEXT,
        nascimento TEXT,
        telefone TEXT,
        whatsapp TEXT,
        email TEXT,
        endereco TEXT,
        numero TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        cep TEXT,
        clube TEXT,
        numero_cr TEXT,
        validade_cr TEXT,
        observacoes TEXT
    )
    """)

    conn.commit()
    conn.close()

# 1. CREATE
def inserir_Cliente():
    print("\nCadastrar cliente")
    nome = input("Nome: ")
    CPF = int(input("CPF: "))
    RG = int(input("RG: "))
    Endereço = input("ENDEREÇO: ")
    telefone = input("telefone: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (nome, CPF, RG, Endereco, telefone) VALUES (?, ?, ?, ?, ?)", (nome, CPF, RG, Endereço, telefone))
    conn.commit()
    print("Cliente cadastrado com sucesso!")

# 2. READ (Listar)
def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    print("\nLista de clientes")
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]} | RG: {cliente[3]} | Endereço: {cliente[4]} | Telefone: {cliente[5]}")

# 2.1 READ (Pesquisar)
def pesquisar_cliente():
    print("\nPesquisar Cliente")
    print("1. Buscar por ID")
    print("2. Buscar por Nome")
    conn = conectar()
    cursor = conn.cursor()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_busca = int(input("Digite o ID: "))

        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_busca,))
        cliente = cursor.fetchone()

        if cliente:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
CPF: {cliente[2]}
RG: {cliente[3]}
Endereço: {cliente[4]}
telefone: {cliente[5]}
""")
        else:
            print("Cliente não encontrado.")

    elif opcao == "2":
        nome_busca = input("Digite o nome: ")

        cursor.execute(
            "SELECT * FROM clientes WHERE nome LIKE ?",
            (f"%{nome_busca}%",)
        )

        resultados = cursor.fetchall()

        if resultados:
            for cliente in resultados:
                print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
CPF: {cliente[2]}
RG: {cliente[3]}
Endereço: {cliente[4]}
Telefone: {cliente[5]}
""")
        else:
            print("Nenhum cliente encontrado.")

    else:
        print("Opção inválida.")

# 3. UPDATE
def atualizar_cliente():
    print("\nAtualizar cliente")
    id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
    conn = conectar()
    cursor = conn.cursor() 
    novo_nome = input("Novo Nome: ")
    novo_CPF = int(input("Novo CPF: "))
    novo_RG = int(input("Nova RG: "))
    novo_Endereço = input("Novo Endereço: ")
    novo_telefone = input("Novo telefone: ")
    
    cursor.execute("UPDATE Clientes SET Nome = ?, CPF = ?, RG = ?,  Endereço = ?,  Telefone = ? WHERE ID = ?", (novo_nome, novo_CPF, nova_RG, novo_Endereço, novo_telefone, id_aluno))
    conexao.commit()
    print("Dados atualizados com sucesso!")

# 4. DELETE
def deletar_cliente():
    print("\nDeletar Aluno")
    id_cliente = int(input("Digite o ID do cliente que deseja remover: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE ID = ?", (id_cliente,))
    conn.commit()
    print("Cliente removido com sucesso!")


# criar tabelas
criar_tabelas()
while True:
    print("\nSISTEMA DE CLIENTES")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Pesquisar")
    print("4. Atualizar")
    print("5. Deletar")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        inserir_Cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        pesquisar_cliente()
    elif opcao == "4":
        atualizar_cliente()
    elif opcao == "5":
        deletar_cliente()
    elif opcao == "0":
        print("Sistema encerrado.")
        break

