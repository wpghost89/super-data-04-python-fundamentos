class Colaborador:
    #Colaborador
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias
        #cCalculando e armazenando dentro de um atributo do objeto
        self.ano_nascimento = 2026 - self.idade

#Função sem parametros
def exemplo_colaborador():
    #Instanciar (criar) um objeto da classe Colaborador
    #       Colaborador(nome, idade, peso, tem_ferias)
    antonio = Colaborador("Antonio", 38, 108, True)
    marcus = Colaborador("Marcus", 40, 80, False)

    #Calculando o ano de nascimento
    #antonio.nascimento = 2026 - antonio.idade1
    #marcus.nascimento = 2026 - marcus.idade

    print("Colaborador 1:", antonio.nome)
    print("Idade:", antonio.idade)
    print("Ano de Nascimento:", antonio.ano_nascimento)
    print("Peso:", antonio.peso)
    print("Tem férias:", antonio.tem_ferias, end="\n\n")

    
    print("Colaborador 2:", marcus.nome)
    print("Idade:", marcus.idade)
    print("Ano de Nascimento:", marcus.ano_nascimento)
    print("Peso:", marcus.peso)
    print("Tem férias:", marcus.tem_ferias, end="\n\n")

class Aluno:
    #metodo contrutor
    def __init__(self, nome: str, nota1: float, nota2: float, nota3: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        #self.media = (self.nota1 + self.nota2 + self.nota3) /3

    # str()texto, int(numero inteiros), float(numero real), bool(verdadeiro ou falso)
    # Função que retorna um float
    def calcular_media(self) -> float:
        media: float = (self.nota1 + self.nota2 + self.nota3) / 3
        return media
     
def exemplo_aluno():
    #Instanciando um objeto (Matheus) da classe aluno
    matheus: Aluno = Aluno("Matheus da Silva", 7, 4.5, 10)
    lukas: Aluno = Aluno("Lukas Pettry", 9.5, 9.8, 0)

    #matheus_media = (matheus.nota1 + matheus.nota2 + matheus.nota3) / 3
    matheus_media = matheus.calcular_media()
    #lukas_media = (lukas.nota1 + lukas.nota2 + lukas.nota3) / 3
    lukas_media = lukas.calcular_media()

    matheus_status = ""
    if matheus_media < 7:
        matheus_status = "Reprovado"
    else:
        matheus_status = "Aprovado"

    lukas_status = ""
    if lukas_media < 7:
        lukas_status = "Reprovado"
    else:
        lukas_status = "Aprovado"

    print("Aluno: ", matheus.nome)
    print(" Nota 1: ", matheus.nota1)
    print(" Nota 2: ", matheus.nota2)
    print(" Nota 3: ", matheus.nota3)
    print(" Média: ", matheus_media)
    print(" Status: ", matheus_status)

    print("Aluno: ", lukas.nome)
    print(" Nota 1: ", lukas.nota1)
    print(" Nota 2: ", lukas.nota2)
    print(" Nota 3: ", lukas.nota3)
    print(" Média: ", lukas_media)
    print(" Status: ", lukas_status)

class Brinquedo:
    def __init__(self, marca: str, nome: str , classificacao: int, preco: float):
        self.marca = marca
        self.nome = nome
        self.classificacao = classificacao
        self.preco = preco

def exemplo_brinquedo():
    hotweels: Brinquedo = Brinquedo("Hotwheels", "Porsche 911 Gt3 Rs" , 4, 154.34)
    boneca: Brinquedo = Brinquedo("Barbie", "Barbie Quero Ser Salva Vidas", 3, 224.49)

    proco_total_brinquedo: float = hotweels.preco + boneca.preco

    print("=== Brinquedo 1 ===")
    print(f"Marca: {hotweels.marca}")
    print(f"Nome: {hotweels.nome}")
    print(f"Classificação: {hotweels.classificacao}")
    print(f"Preço: {hotweels.preco:.2f}")

    print("=== Brinquedo 2 ===")
    print(f"Marca: {boneca.marca}")
    print(f"Nome: {boneca.nome}")
    print(f"Classificação: {boneca.classificacao}")
    print(f"Preço: {boneca.preco:.2f}")

    print(f"\nPreço total dos brinquedos: R$ {proco_total_brinquedo:2f}")

class Flor:
    def __init__(self, nome: str, cor: str):
        self.nome = nome
        self.cor = cor

def exemplo_flor():
    #Instanciando um objeto (Matheus) da classe aluno
    rosa: Flor = Flor("Rosa", "Vermelha")
    lirio: Flor = Flor("Lirio", "Branco")

    print("Flor: ", rosa.nome)
    print("Cor: ", rosa.cor, "\n")

    print("Flor: ", lirio.nome)
    print("Cor: ", lirio.cor, "\n")

class Livro:
    def __init__(self, titulo: str, autor: str, ano_publi: int, num_pagina: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.num_pagina = num_pagina

def exemplo_livro():
    #Instanciando um objeto (Matheus) da classe aluno
    herry: Livro = Livro("Harry Potter e o Enigma do Príncipe", "J.K. Rowling", 2005, 568)
    got: Livro = Livro("A Tormenta de Espadas", "George R. R. Martin.", 2000, 884)

    total_pag: int = herry.num_pagina + got.num_pagina

    print("=== Livro 1 ===")
    print("Titulo: ", herry.titulo)
    print("Autor: ", herry.autor)
    print("Ano piblicação: ", herry.ano_publi)
    print("Páginas: ", herry.num_pagina, "\n")

    print("=== Livro 2 ===")
    print("Titulo: ", got.titulo)
    print("Autor: ", got.autor)
    print("Ano piblicação: ", got.ano_publi)
    print("Páginas: ", got.num_pagina, "\n")

    print("Total páginas: ", total_pag,"\n")

class Pesquepague:
    def __init__(self, nome_peixe: str, peso: float, preco_kg: float):
        self.nome_peixe = nome_peixe
        self.peso = peso
        self.preco_kg = preco_kg

    def calcular_total_peixe(self) -> float:
            total_peixe: float = (self.peso * self.preco_kg)
            return total_peixe

def exemplo_pesquepague():
    #Instanciando um objeto (Matheus) da classe aluno
    peixe1: Pesquepague = Pesquepague("Tilapia", 2.5, 14.5)
    peixe2: Pesquepague = Pesquepague("Tucunaré", 5.25, 25)
    peixe3: Pesquepague = Pesquepague("Tambaqui", 8, 19.25)

    #preco_peixe1: float = peixe1.peso * peixe1.preco_kg
    peixe1_total_peixe = peixe1.calcular_total_peixe()
    #preco_peixe2: float = peixe2.peso * peixe2.preco_kg
    peixe2_total_peixe = peixe2.calcular_total_peixe()
    #preco_peixe3: float = peixe3.peso * peixe3.preco_kg
    peixe3_total_peixe = peixe3.calcular_total_peixe()

    #total_preco: float = (preco_peixe1 + preco_peixe2 + preco_peixe3)
    total_preco: float = (peixe1_total_peixe + peixe2_total_peixe + peixe3_total_peixe)

    total_peso: float = (peixe1.peso + peixe2.peso + peixe3.peso)

    print("Peixe 1: ", peixe1.nome_peixe)     
    print(" Peso: ", peixe1.peso,"kg")
    print(f" Preço Kg: R$", peixe1.preco_kg)
    #print(" Preço: R$", preco_peixe1, "\n")
    print(" Preço: R$", peixe1_total_peixe, "\n")

    print("Peixe 2: ", peixe2.nome_peixe)     
    print(f" Peso: ", peixe2.peso,"kg")
    print(" Preço Kg: R$", peixe2.preco_kg)
    #print(" Preço: R$", preco_peixe2, "\n")
    print(" Preço: R$", peixe2_total_peixe, "\n")

    print("Peixe 3: ", peixe3.nome_peixe)     
    print(f" Peso: ", peixe3.peso,"kg")
    print(" Preço Kg: R$", peixe3.preco_kg)
    #print(" Preço: R$", preco_peixe3, "\n")
    print(" Preço: R$", peixe3_total_peixe, "\n")

    print("Peso total: ", total_peso)
    print("Preço total: R$", total_preco,"\n")

class Calculadora:
    def __init___(self, numero1: float, numero2: float):
        self.numero1 = numero1
        self.numero2 = numero2

    def calculo_somar(self) -> float:
        somar: float = (numero1 + numero2)
        return somar

    def calculo_subtrair(self) -> float:
        subtrair: float = (numero1 - numero2)
        return subtrair

    def calculo_multiplicar(self) -> float:
        multiplicar: float = (numero1 * numero2)
        return multiplicar

    def calculo_dividir(self) -> float:
        dividir: float = (numero1 / numero2)
        return dividir

def exemplo_calculadora():
    num1: Calculadora = Calculadora




#Ponto de inicio da aplicação
if __name__ == "__main__":
    #Executar a função do colaborador
    exemplo_pesquepague()



#git status
#git add .
#git commit - m "Exemplos de classes"
#git push origin main
