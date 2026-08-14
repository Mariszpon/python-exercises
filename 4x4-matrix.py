matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print()
for linha in matriz:
    print(linha)

maior = matriz[0][0]
posicao = (0, 0)

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            posicao = (i, j)
print()
print(f"O maior valor é {maior} na posição {posicao}")
