import sqlite3

# Conectar e criar a tabela
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    Idade INTEGER,
    Curso TEXT
)''')
conexao.commit()

# 1. CREATE
def inserir_Aluno():
    print("\nCadastrar Aluno")
    nome = input("nome: ")
    idade = int(input("idade: "))
    curso = input("Curso: ")
curso.execute()
nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
curso = input("Qual seu curso: ")
inserir_dados(nome, idade, curso)

