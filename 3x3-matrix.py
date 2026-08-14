matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
print()
for linha in range(3):
    print (matriz[linha])
print()
for coluna in range (3):
    print (matriz[coluna])
print()
for linha in range(3):
    for coluna in range(3):
        print (matriz[linha][coluna])
