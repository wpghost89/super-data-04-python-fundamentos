# exemplo_leitura_escrita_arquivos.py

# Modos de abertura de arquivos com open():
#
# r  -> leitura (read). O arquivo deve existir.
# w  -> escrita (write). Cria o arquivo ou sobrescreve o conteúdo existente.
# a  -> anexar (append). Cria o arquivo ou adiciona conteúdo ao final.
# x  -> criação exclusiva. Cria um novo arquivo e gera erro se ele já existir.
#
# Modificadores:
# t  -> modo texto (padrão).
# b  -> modo binário (ex.: imagens, PDFs).
# +  -> permite leitura e escrita.
#
# Exemplos:
# open("arquivo.txt", "r")   # leitura
# open("arquivo.txt", "w")   # escrita/sobrescrita
# open("arquivo.txt", "a")   # adicionar ao final
# open("arquivo.txt", "r+")  # leitura e escrita
# open("arquivo.txt", "rb")  # leitura binária

from pathlib import Path
from datetime import date
from typing import Union

def criar_arquivo_txt():
    # encoding =
    with open("mensagens.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá mundo Guinter\n")
        arquivo.write("O céu está lindo\n")
        arquivo.write("Hoje não choveu")
        print("Arquivo 'mensagens.txt' criado com sucesso")

def ler_arquivo_txt():
    with open("mensagens.txt", "r", encoding="utf-8") as arquivo:
        # ler o arquivo por completo armazenando na variável conteudo (str)
        conteudo = arquivo.read()
    print("Conteudo do arquivo 'mensagens.txt':")
    print(conteudo)

def adicionar_linha_arquivo_txt():
    with open("mensagens.txt", "a", encoding="utf-8") as arquivo:
        mensagem = input("Digite uma mensagem: ")
        arquivo.write(f"\n{mensagem}\n")
    print("Arquivo 'mensagens.txt' modificado com sucesso")

def ler_linhas_arquivo_txt():
    # criar um vetor e jogar para dentro do vetor cada uma das linhas
    linhas_arquivo: list[srt] = []
    with open("mensagens.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.replace("\n", "")
            linhas_arquivo.append(linha_limpa)
        return linhas_arquivo


def criar_arquivo_csv():
    personagem = input("Digite o nome do personagem: ")
    quantidade_missoes = int(input("Digite e quantidade de missões da noite: "))

    # Guarda a data atual
    data_hoje = date.today()

    # Define o caminho do arquivo CSV
    caminho = Path("personagens.csv")

    # Verifica se o arquivo personagens.csv já existe
    if caminho.exists():
        # Informa qua o arquivo já existe
        print("Arquivo de missões existe")

        # Abre o arquivo em modo de adição
        with open("personagens.csv", "a", encoding="utf-8") as arquivo:
            # Escreve uma nova linha com os dados da missão
            arquivo.write(f"{data_hoje};{personagem};{quantidade_missoes}\n")
        # Informa que a missão foi registrada
        print("Missão registrada com sucesso")

    else:
        # Informa que o arquivo ainda não existe
        print("Não existe o arquivo de missão")

        # Informa que o arquivo será criado
        print("Criando arquivo de missão")

        # Abre o arquivo em modo de escrita
        with open("personagens.csv", "w", encoding="utf-8") as arquivo:
            # escreve o cabeçalho do arquivo CSV
            arquivo.write("data;personagem;quantidade\n")

            # Escreve a primeira linha com os dados da missão
            arquivo.write(f"{data_hoje};{personagem};{quantidade_missoes}\n")

        # Informa que o arquivo foi criado
        print("Arquivo de missões criado com sucesso!")


class Missao: 
    def __init__(self, data: str, personagem: str, quantidade: int):
        self.data = data
        self.personagem = personagem
        self.quantidade = quantidade

    def __repr__(self):
        return f"Missao(data={self.data}, personagem={self.personagem}, quantidade={self.quantidade})"
        

def obter_missoes() -> list[Missao]:
    missoes: list[Missao] = []

    with open("personagens.csv", "r", encoding="utf-8") as arquivo:
        indice = 0
        for linha in arquivo:
            if indice == 0:
                indice = indice + 1
                continue
            linha = linha.replace("\n", "")
            partes = linha.split(";")

            data = partes[0]
            personagem = partes[1]
            quantidade = int(partes[2])
            # data, personagem, quantidade = partes

            missao: Missao = Missao(data, personagem, quantidade)
            missoes.append(missao)

            print(data, personagem, quantidade)
            indice = indice + 1
        return missoes

def calcular_media_missoes(missoes: list[Missao]) -> float:
    soma: float =0
    # Percorrer cada uma das missoes
    for missao in missoes:
        soma = soma + missao.quantidade

    media: float = soma / len(missoes)
    return media
# ctrl + . = Importar UNION
def descobrir_maior_quantidadde_missoes(missoes: list[Missao]) -> Union[int, str]:
    maior_quantidade = 0
    personagem_maior_quantidade = ""
    for missao in missoes:
        if missao.quantidade > maior_quantidade:
            maior_quantidade = missao.quantidade
            personagem_maior_quantidade = missao.personagem
    return maior_quantidade, personagem_maior_quantidade


if __name__ == "__main__":
    missoes = obter_missoes()

    media: float = calcular_media_missoes(missoes)
    print("Média", media)

    maior_quantidade_missoes, personagem = descobrir_maior_quantidadde_missoes(missoes)
    print(personagem, "maior quantidade de missões: ", maior_quantidade_missoes)
    #linhas = ler_linhas_arquivo_txt()
    #print(linhas)
    #criar_arquivo_csv()