# Exemplo_classe_eranca.py

import datetime

class ContaBancaria: # Classe pai
    # __init__ é o contrutor
    def __init__(self, cliente:str, saldo_inicial: float, numero: str):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.numero = numero
        # encapsulamento privado fora da classe n ter acesso
        self.__quantidade_saques = 0

    def sacar(self, valor: float):
        # Ao realizar o 3 saque naquele mes deve gerar uma cobrança de 1,50

        if self.__quantidade_saques >= 3:
            valor = valor + 1.50

        if valor > self.saldo:
            print("Saque não realizado por falta de saldo!")
            return

        self.saldo = self.saldo - valor
        print("Realizado saque de R$ ", valor, end="\n\n")
        # incrementar a variavel quantidade de saques
        self.__quantidade_saques = self.__quantidade_saques + 1

# Herança é a capacidade de herdar propriedades (caracteristicas) e função / metodos (comportamentos)
# ContaCorrente é uma classe de herdar "filha" da classe ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, cliente: str, saldo_inicial: float, numero: str, limite_credito: float):
        super().__init__(cliente, saldo_inicial, numero)
        self.limite_credito = limite_credito

    def apresentar_extrato(self):
        data_hora_atual = datetime.datetime.now() #import datetime
        # sata_hora_atual = datetime.now() # from datetime import datetime


        print("Extrato: ", data_hora_atual.strftime("%d/%m/%Y %H:%M"))
        print("Cliente: ", self.cliente)
        print("Número: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Limite de crédito: ", self.limite_credito, end="\n\n")

class ContaSalario(ContaBancaria):
    def __init__(self, cliente:str, saldo_inicial: float, numero: str):
        super().__init__(cliente, saldo_inicial, numero)
    # gerar_extrato
    # transferencia
    # sacar

def exemplo_contas():
    conta_zeh = ContaCorrente("zeh", 5000, "1234", 2000)
    conta_zeh.apresentar_extrato()
    conta_zeh.sacar(1000)
    conta_zeh.apresentar_extrato()

    conta_judity = ContaSalario("Judity", 145_945.00, "1235")
    conta_judity.sacar(30_000)
    # ContaSalario nao tem função apresentar_extrato, pois pertence a classe ContaCorrente
    #conta_judity.apresentar_extrato()

# EXERCÍCIO 1 - HERANÇA COM ANIMAIS
class Animal:

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Nome do animal:", self.nome)
        print("Idade do animal:", self.idade)

class Cachorro(Animal):

    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print("Au Au!")

class Gato(Animal):

    def __init__(self, nome: str, idade: int, cor: str):
        super().__init__(nome, idade)
        self.cor = cor

    def miar(self):
        print("Miau!")

def exemplo_animais():
    meu_cachorro = Cachorro(nome="Zeus", idade=3, raca="Pitbull")
    meu_cachorro.apresentar()
    meu_cachorro.latir()

    meu_gato = Gato(nome="Thor", idade=2, cor="Cinza")
    meu_gato.apresentar()
    meu_gato.miar()

# EXERCÍCIO 2 - SISTEMA DE VEÍCULOS
class Veiculo:

    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor: float):
        self.velocidade = self.velocidade + valor

    def frear(self, valor: float):
        self.velocidade = self.velocidade - valor
        if self.velocidade < 0:
            self.velocidade = 0

class Carro(Veiculo):

    def __init__(self, marca: str, modelo: str, quantidade_portas: int):
        super().__init__(marca, modelo)
        self.quantidade_portas = quantidade_portas

    def apresentar_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Velocidade atual:", self.velocidade)
        print("Quantidade de portas:", self.quantidade_portas, end="\n\n")

class Moto(Veiculo):

    def __init__(self, marca: str, modelo: str, cilindradas: int):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def apresentar_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Velocidade atual:", self.velocidade)
        print("Cilindradas:", self.cilindradas, end="\n\n")

def exemplo_veiculos():
    meu_carro = Carro(
        marca="Volkswagen", modelo="Gol", quantidade_portas=4)
    meu_carro.acelerar(100)
    meu_carro.frear(20)
    meu_carro.apresentar_dados()

    minha_moto = Moto(marca="Honda", modelo="CB 400", cilindradas=400)
    minha_moto.acelerar(90)
    minha_moto.frear(30)
    minha_moto.apresentar_dados()

if __name__ == "__main__":
    exemplo_veiculos()