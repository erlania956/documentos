from banco import conectar


def inserir_cliente():

    conexao = conectar()
    cursor = conexao.cursor()

    print("\n=== Cadastro de Cliente ===")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    nascimento = input("Nascimento: ")
    telefone = input("Telefone: ")
    whatsapp = input("WhatsApp: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    clube = input("Clube de Tiro: ")
    numero_cr = input("Número do CR: ")
    validade_cr = input("Validade do CR: ")
    observacoes = input("Observações: ")

    cursor.execute("""
    INSERT INTO clientes(
        nome,
        cpf,
        rg,
        nascimento,
        telefone,
        whatsapp,
        email,
        endereco,
        numero,
        bairro,
        cidade,
        estado,
        cep,
        clube,
        numero_cr,
        validade_cr,
        observacoes
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        cpf,
        rg,
        nascimento,
        telefone,
        whatsapp,
        email,
        endereco,
        numero,
        bairro,
        cidade,
        estado,
        cep,
        clube,
        numero_cr,
        validade_cr,
        observacoes
    ))

    conexao.commit()
    conexao.close()

    print("\nCliente cadastrado com sucesso!")