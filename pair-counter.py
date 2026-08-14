A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)

pares = sum(1 for num in A if num % 2 == 0)
print("Quantidade de pares:", pares)
