nota = float(input("Qual sua nota? "))
while nota < 0 or nota > 10:
    print("Nota inválida. Digite novamente.")
    nota = float(input("Qual sua nota? "))
print("Nota válida.")
