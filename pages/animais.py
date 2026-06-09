animais = []

def cadastrar_animal():
    nome = input("Nome: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")

    animal = {
        "nome": nome,
        "especie": especie,
        "idade": idade
    }

    animais.append(animal)

    print("Animal cadastrado!")