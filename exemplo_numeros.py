# Exercícios sem CSV, utilizar arquivo txt
# Ex. 1: Criar função `escrever_arquivo_numeros` para criar um arquivo que armazena números
#   Criar o arquivo numeros.txt
#   Escrevendo os números 9, 5, 12, 21, 22, 90 quebrando a linha após cada número
def escrever_arquivo_numeros_txt():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("9\n")
        arquivo.write("5\n")
        arquivo.write("12\n")
        arquivo.write("21\n")
        arquivo.write("22\n")
        arquivo.write("90\n")
        print("Arquivo 'numeros.txt' criado com sucesso")

# Ex. 2: Criar função `ler_arquivo_numeros` para apresentar os números armazenados no arquivo
def ler_arquivo_numeros_txt():
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # ler o arquivo por completo armazenando na variável conteudo (str)
        conteudo = arquivo.read()
    print("Conteudo do arquivo 'numeros.txt':")
    print(conteudo)

# Ex. 3: Criar função `somar_numeros` para apresentar a somar dos números armazenados (ler arquivo)


# Ex. 4: Criar função `calcular_media` para apresentar calcular a média dos números armazenados (ler arquivo)
# Ex. 5: Criar função `descobrir_menor_numero` para apresentar o menor número armazenado (ler arquivo)
# Ex. 5: Criar função `descobrir_maior_numero` para apresentar o maior número armazenado (ler arquivo)


if __name__ == "__main__":
    ler_arquivo_numeros_txt()