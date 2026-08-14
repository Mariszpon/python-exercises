nota = -1
while nota < 0 or nota > 10:
    nota = float(input("Digite sua nota (0 a 10): "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.")
    else:
        print(f"Sua nota registrada foi: {nota}")
