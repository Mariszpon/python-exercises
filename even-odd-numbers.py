pares = 0
impares = 0
contador = 0
while contador < 10:
    try:
        numero = int(input(f"Digite o {contador + 1}º número: "))
        if numero % 2 == 0:
            pares += 1
        elif numero % 2 != 0:
            impares += 1
        contador += 1
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
