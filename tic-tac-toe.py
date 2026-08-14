def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador = "X"
for _ in range(9):
    imprimir_tabuleiro(tabuleiro)
    linha = int(input("Digite a linha (0-2): "))
    coluna = int(input("Digite a coluna (0-2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        jogador = "O" if jogador == "X" else "X"
    else:
        print("Posição ocupada, tente novamente!")

imprimir_tabuleiro(tabuleiro)
print()
