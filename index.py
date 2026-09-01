class Colaborador:
    #Colaborador
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias

#Função sem parametros
def exemplo_colaborador():
    #Instanciar (criar) um objeto da classe Colaborador
    #       Colaborador(nome, idade, peso, tem_ferias)
    antonio= Colaborador("Antonio", 38,108, True)

    #Calculando o ano de nascimento
    antonio.nascimento = 2026 - antonio.idade

    marcus = Colaborador("Marcus", 40, 80, False)

    print("Colaborador 1:", antonio.nome)
    print("Idade:", antonio.idade)
    print("Ano de Nascimento:", antonio.nascimento)
    print("Peso:", antonio.peso)
    print("Tem férias:", antonio.tem_ferias, end="\n\n\n")

    
    print("Colaborador 2:", marcus.nome)
    print("Idade:", marcus.idade)
    print("Peso:", marcus.peso)
    print("Tem férias:", marcus.tem_ferias, end="\n\n\n")

class Aluno:
    #metodo contrutor
    def __init__(self, nome: str, nota1: float, nota2: float, nota3: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
     

def exemplo_aluno():
    #Instanciando um objeto (Matheus) da classe aluno
    matheus: Aluno = Aluno("Matheus da Silva", 7, 4.5, 10)

    print("Aluno: ", matheus.nome)
    print(" Nota 1: ", matheus.nota1)
    print(" Nota 2: ", matheus.nota2)
    print(" Nota 3: ", matheus.nota3)


#Ponto de inicio da aplicação
if __name__ == "__main__":
    #Executar a função do colaborador
    exemplo_aluno()



#git status
#git add .
#git commit - m "Exemplos de classes"
#git push origin main
