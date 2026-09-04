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

######## 1
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

######## 2
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

######## 3
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

######## 4
class Calculadora:
    def __init__(self, numero1: float, numero2: float):
        self.numero1 = numero1
        self.numero2 = numero2

    def calculo_somar(self) -> float:
        #somar: float = (numero1 + numero2)
        return self.numero1 + self.numero2

    def calculo_subtrair(self) -> float:
        #subtrair: float = (numero1 - numero2)
        return self.numero1 - self.numero2

    def calculo_multiplicar(self) -> float:
        #multiplicar: float = (numero1 * numero2)
        return self.numero1 * self.numero2

    def calculo_dividir(self) -> float:
        #dividir: float = (numero1 / numero2)
        return  self.numero1 / self.numero2

def exemplo_calculadora():
    calc = Calculadora(25, 10)
    
    soma = calc.calculo_somar()
    subtracao = calc.calculo_subtrair()
    multiplicar = calc.calculo_multiplicar()
    divisao = calc.calculo_dividir()
    
    
    print("Soma: ", soma)
    print("Subtração: ", subtracao)
    print("Multiplicar: ", multiplicar)
    print("Divisão: ", divisao)
    
class Retangulo:
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def calculo_area(self) -> float:
        return self.largura * self.altura

def exemplo_retangulo():
    calc = Retangulo(45, 15)
    area = calc.calculo_area()
    
    print("Área: ", area)

######## 5
class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def calcular_total_produto(self) -> float:
        total_produto: float = (self.preco * self.quantidade)
        return total_produto
        
def exemplo_produto():
    produto1: Produto = Produto("Costela", 23.9, 3.5)
    produto2: Produto = Produto("Alcatra", 45.3, 2.8)
    produto3: Produto = Produto("Vinho Tinto", 63, 2)
    
    produto1_total_produto = produto1.calcular_total_produto()
    produto2_total_produto = produto2.calcular_total_produto()
    produto3_total_produto = produto3.calcular_total_produto()  
    
    total_valor: float = (produto1_total_produto + produto2_total_produto + produto3_total_produto)
    
    print("Produto: ", produto1.nome)     
    print(" Peso: ", produto1.quantidade)
    print(f" Preço un: R$", produto1.preco)
    print(f" Preço: R$ {produto1_total_produto:.2f}", "\n")
    
    print("Produto: ", produto2.nome)     
    print(" Peso: ", produto2.quantidade)
    print(f" Preço un: R$", produto2.preco)
    print(f" Preço: R$ {produto2_total_produto:.2f}", "\n")
    
    print("Produto: ", produto3.nome)     
    print(" Peso: ", produto3.quantidade)
    print(f" Preço un: R$", produto3.preco)
    print(f" Preço: R$ {produto3_total_produto:.2f}", "\n")
    
    print(f"Total: R$ {total_valor:.2f}","\n")

######## 6 ???????
class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

def exemplo_conta_bancaria():
    conta = ContaBancaria("José Bonifacio", 500.00)
    print(f"Saldo inicial ({conta.titular}): R$ {conta.saldo:.2f}")

    conta.depositar(250.00)
    print(f"Após depósito de R$ 250.00: R$ {conta.saldo:.2f}")

    sucesso_saque_1 = conta.sacar(300.00)
    print(f"Tentativa de saque de R$ 300.00: {'Sucesso' if sucesso_saque_1 else 'Falhou'}")
    print(f"Saldo atual: R$ {conta.saldo:.2f}")

    sucesso_saque_2 = conta.sacar(1000.00)
    print(f"Tentativa de saque de R$ 1000.00: {'Sucesso' if sucesso_saque_2 else 'Falhou'}")
    print(f"Saldo atual: R$ {conta.saldo:.2f}")

######## 7
class Temperatura:
    def __init__(self, cidade: str, celsius: float):
        self.cidade = cidade
        self.celsius = celsius

    def para_fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32

    def para_kelvin(self) -> float:
        return self.celsius + 273.15

    def esta_congelando(self) -> bool:
        return self.celsius <= 0

def exibir_informacoes(temp: Temperatura):
    print(f"--- Cidade: {temp.cidade} ---")
    print(f"Celsius: {temp.celsius:.1f} °C")
    print(f"Fahrenheit: {temp.para_fahrenheit():.1f} °F")
    print(f"Kelvin: {temp.para_kelvin():.2f} K")
    
    if temp.esta_congelando():
        print("Está congelando! \n")
    else:
        print("Não está congelando.\n")

def exemplo_temperatura():
    cidade1 = Temperatura("Brusque", 22.5)
    cidade2 = Temperatura("Urupema", -5.0)

    exibir_informacoes(cidade1)
    exibir_informacoes(cidade2)
        
######## 8
class Funcionario:
    def __init__(self, nome: str, cargo: str, valor_hora: float, horas_trabalhadas: float):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self) -> float:
        return self.valor_hora * self.horas_trabalhadas

    def calcular_bonus(self) -> float:
        salario_bruto = self.calcular_salario_bruto()
        if self.horas_trabalhadas > 180:
            return salario_bruto * 0.10
        elif self.horas_trabalhadas >= 160:
            return salario_bruto * 0.05
        return 0.0

    def calcular_salario_total(self) -> float:
        return self.calcular_salario_bruto() + self.calcular_bonus()

def exemplo_folha_pagamento():
    func1 = Funcionario("Ana Souza", "Desenvolvedora", 50.00, 190.0)  # > 180h (Bônus 10%)
    func2 = Funcionario("Carlos Lima", "Analista", 45.00, 170.0)      # 160h a 180h (Bônus 5%)
    func3 = Funcionario("Beatriz Alves", "Assistente", 30.00, 150.0)  # < 160h (Bônus 0%)

    funcionarios = [func1, func2, func3]
    custo_total_folha = 0.0

    print("=== RELATÓRIO DE FUNCIONÁRIOS ===")
    for f in funcionarios:
        bruto = f.calcular_salario_bruto()
        bonus = f.calcular_bonus()
        total = f.calcular_salario_total()
        custo_total_folha += total

        print(f"Nome: {f.nome} | Cargo: {f.cargo}")
        print(f"Horas trabalhadas: {f.horas_trabalhadas}h (R$ {f.valor_hora:.2f}/h)")
        print(f"Salário Bruto: R$ {bruto:.2f}")
        print(f"Bônus: R$ {bonus:.2f}")
        print(f"Salário Total: R$ {total:.2f}", "\n")

    print(f"Custo Total da Folha de Pagamento: R$ {custo_total_folha:.2f}")
        
######## 9
class Viagem:
    def __init__(
        self,
        origem: str,
        destino: str,
        distancia_km: float,
        consumo_km_l: float,
        preco_litro: float,
    ):
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km
        self.consumo_km_l = consumo_km_l
        self.preco_litro = preco_litro

    def calcular_litros(self) -> float:
        return self.distancia_km / self.consumo_km_l

    def calcular_custo(self) -> float:
        return self.calcular_litros() * self.preco_litro

def exemplo_viagem():
    viagem1 = Viagem("Brusque", "Lages", 300.0, 12.0, 6.30)
    viagem2 = Viagem("Brusque", "Florianópolis", 120.0, 8.0, 4.20)

    viagens = [viagem1, viagem2]

    print("DETALHES DAS VIAGENS")
    for v in viagens:
        litros = v.calcular_litros()
        custo = v.calcular_custo()
        print(f"\nDe: {v.origem} -> Para: {v.destino}")
        print(f"Litros necessários: {litros:.2f} L")
        print(f"Custo total: R$ {custo:.2f}")

    print("\n")
    custo1 = viagem1.calcular_custo()
    custo2 = viagem2.calcular_custo()

    if custo1 > custo2:
        print(f"A viagem mais cara é: {viagem1.origem} -> {viagem1.destino} (R$ {custo1:.2f})")
    elif custo2 > custo1:
        print(f"A viagem mais cara é: {viagem2.origem} -> {viagem2.destino} (R$ {custo2:.2f})")
    else:
        print(f"Ambas as viagens possuem o mesmo custo (R$ {custo1:.2f})")
        
        

#Ponto de inicio da aplicação
if __name__ == "__main__":
    #Executar a função do colaborador
    exemplo_viagem()


#git status
#git add .
#git commit - m "Exemplos de classes"
#git push origin main
