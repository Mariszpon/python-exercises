sorteados = [5, 12, 22, 29, 33, 41]
aposta = [0, 0, 0, 0, 0, 0]

indice = 0
while indice < 6:
    aposta[indice] = int(input(f"Digite o {indice+1}° número da aposta: "))
    indice += 1

acertos = 0
indice = 0
while indice < 6:
    if aposta[indice] in sorteados:
        acertos += 1
    indice += 1

print("Números sorteados:", sorteados)
print("Números apostados:", aposta)
print("Quantia de acertos:", acertos)
