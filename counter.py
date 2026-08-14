numero = 0
for i in range (1, 101):
of i % 3 == 0 and i % 5 != 0:
print(i)
numero = numero + 1
print()
print(f"A quantia de números entre 1 e 100 múltiplos de 3 e não múltiplos de 4 é: {numero}")
