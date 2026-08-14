A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)

print("Maior elemento:", max(A))
print("Menor elemento:", min(A))
