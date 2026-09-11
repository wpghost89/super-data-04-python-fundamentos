# exemplo_dicionarios.py

def exemplo_dicionario_simples():
    # dicionario em lugar onde é possivel armazenar valor utilizando uma chame
    #dict[chave, valor]
    carros: dict[str, str] = {}

    # Armazenar um dado no dicionario passando o nome da chave "VW"
    carros["VW"] = "Fusca"
    carros["GM"] = "Opala"
    carros["BYD"] = "Song Plus"

    # Acessar o valor armazenado na chave 'vw'
    print("Valores armazenados nos dicionários:" )
    print(carros["VW"])
    print(carros["GM"])
    print(carros["BYD"])

    print("\n\n")
    print("Chaves:" , carros.keys())
    print("Valores: ", carros.values())

def exemplo_dicionario_complexo():
    alunos: dict[str, dict[str, str | int]] = {}

    alunos["89201"] = {
        "nome": "Pedro",
        "idade": 23,
        "cpf": "201.312.231-30",
    }

    alunos["89202"] = {
            "nome": "Judity",
            "idade": 39,
            "cpf": "293.120.492-31"
    }

    print("Nome da Judity", alunos["89202"]["nome"])
    print("Idade Judity", alunos["89202"]["idade"])
    print("CPF Judity", alunos["89202"]["cpf"])


if __name__ =="__main__":
    exemplo_dicionario_complexo()