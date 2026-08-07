import sqlite3

BANCO = "banco/clientes.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE,
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

    conexao.commit()
    conexao.close()