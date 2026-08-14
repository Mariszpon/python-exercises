A = []
for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)

X = int(input("Digite a posição X (0 a 7): "))
Y = int(input("Digite a posição Y (0 a 7): "))

soma = A[X] + A[Y]
print("Soma dos valores:", soma)
