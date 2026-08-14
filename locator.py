A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)

maior = max(A)
posicao = A.index(maior)
print("Vetor:", A)
print("Maior elemento:", maior)
print("Posição:", posicao)
