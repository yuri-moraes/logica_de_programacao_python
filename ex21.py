"""Exercício 3 da Atividade Prática - Lógica de programação e Algorítimos"""

print("Bem-vindo ao Exportation Logistic's Yuri Nogueira de Moraes")

# Dicionário de rotas com suas respectivas informações
routes = {
    "RS": ("De Rio de Janeiro até São Paulo", 1),
    "BS": ("De Brasília até São Paulo", 1.2),
    "BR": ("De Brasília até Rio de Janeiro", 1.5),
}


def dimensoesObjeto():
    while True:
        try:
            # Solicita ao usuário as dimensões do objeto
            height = float(input("Insira a altura do objeto em centímetros (cm): "))
            length = float(
                input("Insira o comprimento do objeto em centímetros (cm): ")
            )
            width = float(input("Insira a largura do objeto em centímetros (cm): "))

            volume = height * length * width

            if volume < 1000:
                value = 10
            elif 1000 <= volume < 10000:
                value = 20
            elif 10000 <= volume < 30000:
                value = 30
            elif 30000 <= volume < 100000:
                value = 40
            else:
                print("Não aceitamos objetos cujo volume é alto.")
                print("Entre com as dimensões desejadas novamente.")
                continue

            print(f"O volume do objeto é: {volume} cm³")
            print(f"O valor para o objeto é R${value:.2f}")
            return value

        except ValueError:
            print("Valor inválido, tente novamente.")


def pesoObjeto():
    weight_mult = 0
    while True:
        try:
            # Solicita ao usuário o peso do objeto
            weight = float(input("Insira o peso do produto em quilogramas (Kg): "))

            if weight <= 0.1:
                weight_mult = 1
            elif 0.1 <= weight < 1:
                weight_mult = 1.5
            elif 1 <= weight < 10:
                weight_mult = 2
            elif 10 <= weight < 30:
                weight_mult = 3
            else:
                print("Não aceitamos peso muito alto.")
                print("Entre com o peso desejado novamente.")
                continue

            break
        except ValueError:
            print("Valor do peso inválido, tente novamente.")

    return weight_mult


def rotaObjeto():
    mult = 0
    print("-" * 65)
    print("Sigla\t\t\tRota\t\t\t\tValue")
    print("-" * 65)
    for rota, (rote, value) in routes.items():
        print(f"{rota}\t\t{rote:<25}\t\t{value}")
    print("-" * 65)

    while True:
        try:
            # Solicita ao usuário a sigla da rota desejada
            route = input("Insira a rota desejada (exemplo - RS)\nR: ").upper()

            if route == "RS":
                mult = 1
            elif route == "BS":
                mult = 1.2
            elif route == "BR":
                mult = 1.5
            else:
                print("Insira uma sigla válida!")
                continue

            break
        except ValueError:
            print("Insira um símbolo de rota válido!")

    print(f"Rota selecionada: {routes[route][0]}")
    return mult


print("*" * 60)
# Chamada da função para obter as dimensões do objeto
VOLUME = dimensoesObjeto()
print("*" * 60)

# Chamada da função para obter o peso do objeto
PESO = pesoObjeto()

# Chamada da função para obter a rota desejada
ROTA = rotaObjeto()

calc = VOLUME * PESO * ROTA

print("*" * 60)
print(f"O valor final do objeto é R${calc:.2f}")
print(f"Especificações -> Volume: {VOLUME} cm³, Massa: {PESO} Kg, Rota: {ROTA} ")
