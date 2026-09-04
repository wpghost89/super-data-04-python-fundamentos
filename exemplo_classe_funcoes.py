import os

def limpar_terminal():
    os.system("cls")

# exemplo_classe_funcoes.py
class ContaBancaria:
    # Construtor
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self,valor: float):
        # saldo recebe ele mesmo + valor a depositar
        self.saldo = self.saldo + valor
        print("Depositado R$ ", valor)

    def sacar(self, valor: float):
        # se saldo for maior ou igual que o valor
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            # serve para dizer que o saque foi realizado com sucesso
            return True
        else:
            return False

def exemplo_conta_bancaria():
    zeh_conta: ContaBancaria = ContaBancaria("Zeh da Conta", 500.00)
    print("Conta: ", zeh_conta.titular)
    print("Saldo: ", zeh_conta.saldo)

    zeh_conta.depositar(250)
    print("Saldo: ", zeh_conta.saldo)
    if zeh_conta.sacar(3000) == True:
        print("Saque realizado com sucesso: R$300,00")
    else:
        print("Saldo: ", zeh_conta.saldo)

def exemplo_conta_bancaria_com_usuario():
    titular = input("Digite o nome do titular: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))

    limpar_terminal()
    conta_bancaria: ContaBancaria = ContaBancaria(titular, saldo_inicial)

    menu = """Bem vindo ao sistema do Banco XYZ
    1 - Saldo
    2 - Depositar
    3 - Sacar
    9 - Sair
    Escolha a opção desejada:"""
    opcao = int(input(menu))
    # enquanto opcao for diferente de 9 repetir
    while opcao != 9:
        limpar_terminal()

        if opcao == 1:
            print("Conta: ", conta_bancaria.titular)
            print("Saldo: ", conta_bancaria.saldo)
        elif opcao == 2:
            valor_depositar = float(input("Digite o valor para depoistar: "))
            conta_bancaria.depositar(valor_depositar)
        elif opcao ==3:
            valor_sacar = float(input("Digite o valor para sacar: "))
            resultado_saque = conta_bancaria.sacar(valor_sacar)
            if resultado_saque == True:
                print("Saque realizado com sucesso!")
            else:
                print("Saque não realizado por saldo insuficiente!")

        opcao = int(input(menu))
    limpar_terminal()
    print("Obrigado por utilizar o Banco XYZ")

# franciscosensaulas/AJS

#import questionary

# Propriedades: nome, quantidade_horas = 220, valor_hora, cargo

# Quantidade de horas fixas:
# Estag     110
# Demais    220

# Valor hora por cargo:
# Estag         R$ 14,73    => 1621.40
# Junior        R$ 9,10     => 2000
# Pleno         R$ 22,73    => 5000.60
# Senior        R$ 36,37    => 8001.40
# Especialista  R$ 68,19    => 15001.8

# Aumento máximo de 20% e n pode para estag

# PLR:
# Estag         0.40
# Junior        1.0
# Pleno         1.5
# Senior        3.5
# Especialista  5.0
class Funcionario:
    def __init__(self, nome: str, cargo: str):
        self.nome = nome
        self.cargo = cargo

        self.percentual_aumento = 1

        if self.cargo == "Estag":
            self.quantidade_horas = 110
        else:
            self.quantidade_horas = 220

        if self.cargo == "Estag":
            self.valor_hora = 14.74
        elif self.cargo == "Junior":
            self.valor_hora = 9.10
        elif self.cargo == "Pleno":
            self.valor_hora = 22.73
        elif self.cargo == "Senior":
            self.valor_hora = 36.37
        elif self.cargo == "Especialista":
            self.valor_hora = 68.19


    def calcular_salario(self) -> float:
        salario = self.valor_hora * self.quantidade_horas
        aumento = salario * (self.percentual_aumento / 100)
        return salario + aumento

    # Função com retorno do tipo float
    def calcular_plr(self) -> float:
        # Estag         0.40
        # Junior        1.0
        # Pleno         1.5
        # Senior        3.5
        # Especialista  5.0
        if self.cargo == "Estag":
            multiplicador = 0.40
        elif self.cargo == "Junior":
            multiplicador = 1
        elif self.cargo == "Pleno":
            multiplicador = 1.5
        elif self.cargo == "Senior":
            multiplicador = 3.5
        elif self.cargo == "Especialista":
            multiplicador = 5.0

        salario: float = self.calcular_salario()

        plr: float = salario * multiplicador
        return plr

    def conceder_aumento(self, percentual_aumento):
        if self.cargo == "Estag":
            print("Estagiário não pode receber aumento")
            return False

        if percentual_aumento > 20:
            print("Não é possível conceder mais do que 20% de aumento")
            return False

        self.percentual_aumento = percentual_aumento


def exemplo_funcionario():
    cargos = ["Estag", "Junior", "Pleno", "Senior", "Especialista"]

    nome = input("Digite o nome do colaborador: ").strip()

    while len(nome) < 3 or len(nome) > 50:
        print("Nome deve conter no mínimo 3 caracteres e no máximo 50")
        nome = input("Digite o nome do colaborador: ").strip()

    cargo = input("Digite o cargo: ").strip().capitalize()
    # pip install questionary
    # import questionary
    # cargo = questionary.select("Escolha o cargo", choices=cargos).ask()

    while cargo not in cargos:
        print("Cargo inválido")
        cargo = input("Digite o cargo: ").strip().capitalize()

    funcionario: Funcionario = Funcionario(nome, cargo)

    conceder_aumento = input("Deseja conceder aumento para o colaborador: [s/n] ").upper().strip()
    # if conceder_aumento.upper().strip() == "S" or conceder_aumento.upper().strip() == "SIM":
    if conceder_aumento == "S" or conceder_aumento == "SIM":
        percentual_aumento = float(input("Digite o percentual de aumento: "))
        funcionario.conceder_aumento(percentual_aumento)

    print(f"""
Funcionário: {funcionario.nome}
Cargo: {funcionario.cargo}
Quantidade de horas: {funcionario.quantidade_horas}
Valor hora: {funcionario.valor_hora:.2f}
Salário: {funcionario.calcular_salario():.2f}
PLR: {funcionario.calcular_plr():.2f}""")

if __name__ ==  "__main__":
    exemplo_funcionario()

# https://franciscosensaulas.com/AJS