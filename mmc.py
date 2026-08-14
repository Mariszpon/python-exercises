num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
mmc = num1 if num1 > num2 else num2
while True:
    if mmc % num1 == 0 and mmc % num2 ==0:
        print(f"O MMC de {num1} e {num2} é {mmc}.")
        break
    else:
        mmc += 1
print(f"O MMC de {num1} e {num2} é {mmc}.")
