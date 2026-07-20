def contar_vogais_no_arquivo():
    nome_arquivo = input("Digite o nome do arquivo texto:")
    vogais = input("Digite o caracter a ser buscado no arquivo: ")
    total_caracter = 0
    try:
        with open(nome_arquivo, 'r' , encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for caractere in conteudo:
                if caractere in vogais:
                    caracter += 1
        print(f"O arquivo possui {caracter} vogais.")
    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado. Verifique o nome.")
    contar_caracter_arquivo()
        
    