A = []
B = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    A.append(num)
    B.append(num ** 2)
print("Vetor original:", A)
print("Quadrados:", B)
