# Exibe uma mensagem de boas-vindas ao programa
print("Bem-vindo à Bicycle Stock Control's Yuri Nogueira de Moraes")

def cadastrarPeca():
    # Cria um dicionário para armazenar os dados da peça
    peca = {
        "nome": input("Digite o nome da peça: "),
        "fabricante": input("Digite o fabricante da peça: "),
        "valor": float(input("Digite o valor da peça: ")),
    }
    return peca


def consultarPeca(pecas):
    while True:
        # Exibe o menu de consulta
        print("\nMENU DE CONSULTA")
        print("1 - Consultar Todas as Peças")
        print("2 - Consultar Peças por Código")
        print("3 - Consultar Peças por Fabricante")
        print("4 - Retornar")

        # Solicita a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultarTodasPecas(pecas)
        elif opcao == "2":
            consultarPecasPorCodigo(pecas)
        elif opcao == "3":
            consultarPecasPorFabricante(pecas)
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Digite novamente.")


def consultarTodasPecas(pecas):
    # Exibe todas as peças cadastradas
    print("\nTODAS AS PEÇAS CADASTRADAS:")
    for peca in pecas:
        info_peca = f"Código: {peca['codigo']}\nNome: {peca['nome']}\nFabricante: {peca['fabricante']}\nValor: R$ {peca['valor']:.2f}\n------------------------"
        print(info_peca)


def consultarPecasPorCodigo(pecas):
    codigo = input("\nDigite o código da peça: ")
    for peca in pecas:
        if peca["codigo"] == codigo:
            # Exibe as informações da peça encontrada pelo código
            print(f"Código: {peca['codigo']}")
            print(f"Nome: {peca['nome']}")
            print(f"Fabricante: {peca['fabricante']}")
            print(f"Valor: R$ {peca['valor']:.2f}")
            break
    else:
        print("Peça não encontrada.")


def consultarPecasPorFabricante(pecas):
    fabricante = input("\nDigite o fabricante da peça: ")
    for peca in pecas:
        if peca["fabricante"] == fabricante:
            # Exibe as informações das peças encontradas pelo fabricante
            print(f"Código: {peca['codigo']}")
            print(f"Nome: {peca['nome']}")
            print(f"Fabricante: {peca['fabricante']}")
            print(f"Valor: R$ {peca['valor']:.2f}")
            print("------------------------")


def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    for i, peca in enumerate(pecas):
        if peca["codigo"] == codigo:
            # Remove a peça da lista de peças cadastradas
            del pecas[i]
            print("Peça removida com sucesso.")
            break
    else:
        print("Peça não encontrada.")


def main():
    pecas = []
    contador = 1

    while True:
        # Exibe o menu principal
        print("\nMENU PRINCIPAL")
        print("1 - Cadastrar Peça")
        print("2 - Consultar Peça")
        print("3 - Remover Peça")
        print("4 - Sair")

        # Solicita a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            peca = cadastrarPeca()
            peca["codigo"] = str(contador)
            pecas.append(peca)
            contador += 1
            print("Peça cadastrada com sucesso.")
        elif opcao == "2":
            consultarPeca(pecas)
        elif opcao == "3":
            removerPeca(pecas)
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Digite novamente.")

    print("Programa encerrado.")


# Inicia a execução do programa
main()
