def exemplo_lista_simples():
    # CRUD Create, Read, Update e Delete

    # Criando uma lista com um elemento (Não é obrigatorio colocar item na lista ao criar)
    colegas: list[str] = ["Pedro"]
    # Adicionando elementos na lista/vetor
    colegas.append("Judity")
    colegas.append("Juliana")
    colegas.append("Francisco")

    # Remover Francisco
    colegas.remove("Francisco")

    # Alterando o nome da Juliana da terceira Posição
    colegas[2] = "Liana"

    # Apresentando a quantidade de elementos da lista
    print("Quantidade de coleguinhas:", len(colegas))

    # Apresentando os elementos da lista
    print("Primeiro colega: ", colegas[0])
    print("Segundo colega: ", colegas[1])
    print("Terceiro colega: ", colegas[2])

def exemplo_lista_simples_int():
    numeros: list[int] = []

    # Solicitar um numero e adicionar na lista(posicao 0)
    numeros.append(int(input("Digite um número: ")))
    numeros.append(int(input("Digite um número: ")))
    numeros.append(int(input("Digite um número: ")))

    soma: int = numeros[0] + numeros[1] + numeros[2]
    print("Soma: ", soma)

def exemplo_lista_simples_percorrendo():
    salarios: list[float] = []

    #quantidade_desejada: int = int(input("Digite a quantidade de salarios: "))

    # Solicitar para o usuario 4 salarios
    for i in range(0, 4):
        salario = float(input("Digite o salário: "))

        salarios.append(salario)

    # soma = salario[0] + salario[1] + salario[2] + salario[3]
    soma: float = 0
    for i in range(0, 4):
        soma = soma + salarios[i]

    # Qual é o maior salário
    maior_salario: float = 0
    for i in range(0, 4):
        salario_atual = salarios[i]
        if salario_atual > maior_salario:
            maior_salario = salario_atual

    # Qual é o menor salário
        menor_salario: float = 999999999
        for i in range(0, 4):
            salario_atual = salarios[i]
            if salario_atual > menor_salario:
                menor_salario = salario_atual

    media: float = soma / len(salarios)

    # Apresentar os salários
    for i in range(0, 4):
        salario_atual: float = salarios[i]
        print(f"Salário {(i +1)}º: R$ {salario_atual}")
    

    print("Soma: ", soma)
    print("Média: ", media)
    print("Maior salário: ", maior_salario)
    print("Menor salário: ", menor_salario)

# Ex.1: Criar uma lista de 5 produtos (N PODE UTILIZAR FOR)
#   Adicionar o nome de 5 produtos na lista
#   Alterar o nome do produto da posição 4
#   Remover  o produto da posição 1
#   Adicionar mais 2 produtos
#   Apresentar a quantidade de elementos da lista

def exercicio01():
    produtos: list[str] = []

    produtos.append("Arroz")
    produtos.append("Feijão")
    produtos.append("Macarrão")
    produtos.append("Leite")
    produtos.append("Café")

    produtos[4] = "Café Solúvel"

    produtos.pop(1)

    produtos.append("Açúcar")
    produtos.append("Óleo")

    print("Quantidade de produtos na lista:", len(produtos))

    print("\nProdutos na lista:")
    print("Posição 0:", produtos[0])
    print("Posição 1:", produtos[1])
    print("Posição 2:", produtos[2])
    print("Posição 3:", produtos[3])
    print("Posição 4:", produtos[4])
    print("Posição 5:", produtos[5])




#Ex.2: Criar uma lista para armazenar o nome dos jogos (UTILIZAR O FOR)
#   Fazer for para adicionar 5 jogos na lista (Solicitar para o usuario)
#   Apresentar os 5 jogos (outro for)
#   Modificar o for solicitar tbm o preço do jogo e adicionar na lista de preços
#   Modificar o for para apresentar tbm o preço do jogo
#   Calcular o total dos preços (utilizar o for)
#   Apresentar o total dos preços

def exercicio02():
    jogos: list[str] = []
    precos: list[float] = []

    # Solicitar para o usuário 5 jogos e seus respectivos preços
    for i in range(0, 5):
        nome_jogo = input(f"Digite o nome do {i + 1}º jogo: ")
        preco_jogo = float(input(f"Digite o preço do {i + 1}º jogo: R$ "))

        jogos.append(nome_jogo)
        precos.append(preco_jogo)

    print("LISTA DE JOGOS E PREÇOS")
    # Apresentar os 5 jogos e seus preços
    for i in range(0, 5):
        print(f"Jogo: {jogos[i]} - Preço: R$ {precos[i]:.2f}")

    # Calcular o total dos preços
    total_precos: float = 0
    for i in range(0, 5):
        total_precos = total_precos + precos[i]

    # Apresentar o total dos preços
    print("Total dos preços: R$", total_precos)


if __name__ == "__main__":
    exercicio02()