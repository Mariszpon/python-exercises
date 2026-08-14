A = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º valor: "))
    A.append(num)

print("Valores lidos:", A)
print("Maior:", max(A))
print("Menor:", min(A))
print("Média:", sum(A)/len(A))
print()
print("Exercício 11")
A = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º valor: "))
    A.append(num)

maior = max(A)
menor = min(A)

print("Posição do maior:", A.index(maior))
print("Posição do menor:", A.index(menor))
