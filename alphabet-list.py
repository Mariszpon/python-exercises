import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(alfabeto)

print("Lista embaralhada:", alfabeto)

letra = input("Digite uma letra para adivinhar a posição: ")
posicao = int(input("Digite a posição que você acha (0 a 25): "))

if alfabeto[posicao] == letra:
    print("Acertou!")
else:
    print("Errou! A letra nessa posição é:", alfabeto[posicao])
print()
