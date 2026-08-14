matriz = [
    [20, 2, 3],
    [4, 5, 15],
    [7, 19, 9]
]
print(matriz)
print()
for linha in range(3):
    print(matriz[linha])
print()
for linha in range(3):
    for coluna in range(3):
        print (matriz[linha][coluna])
print()
print("Atividade 03 - Slides")
soma = matriz[0][0] + matriz[1][0]
subtracao = matriz[2][2] - matriz[2][1]
multiplicacao = matriz[0][1] * matriz[2][0]
divisao = matriz[1][2] / matriz[0][2]

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
