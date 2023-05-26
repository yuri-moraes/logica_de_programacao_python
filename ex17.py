"""Cálculo de tamanho de strings"""


def lenght(word="", min_lenght=0, max_lenght=0):
    """calcula o tamanho da palavra e dá retorno de acordo com os limites"""

    word = input("Digite uma palavra: ")
    min_lenght = int(input("Coloque o mínimo de caractéres aceitáveis: "))
    max_lenght = int(input("Coloque o máximo de caractéres aceitáveis: "))

    if min_lenght <= len(word) <= max_lenght:
        return print(True)
    else:
        return print(False)


lenght()
