A = []
for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    A.append(num)

negativos = sum(1 for num in A if num < 0)
soma_positivos = sum(num for num in A if num > 0)

print("Quantidade de negativos:", negativos)
print("Soma dos positivos:", soma_positivos)
