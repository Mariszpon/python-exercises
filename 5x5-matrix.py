print ("Atividade 01")
matriz = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

print(matriz)
print()
for linha in range (5):
    print (matriz[linha])
print()
for linha in range(5):
    for coluna in range(5):
        print (matriz[linha][coluna])
