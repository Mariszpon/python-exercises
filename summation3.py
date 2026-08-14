n = int(input("Digite um número inteiro positivo: "))
while n <= 0:
n = int(input("Digite um valor válido: "))
soma = 0
expressao = "
for i in range(1, n + 1):
soma = soma + i
if i == 1:
expressao = str(i)
else:
expressao = expressao + "+" + str(i)
print(expressao + "=" + str(soma))
