for i in range (5):
    linha = []
    matricula = int(input(f"Digite a matrícula do aluno {i+1}: "))
    media_provas = int(input(f"Digite a média das provas do aluno {i+1}: "))
    media_trabalhos = int(input(f"Digite a média dos trabalhos do aluno {i+1}: "))

    nota_final = media_provas + media_trabalhos

    linha.append(matricula)
    linha.append(media_provas)
    linha.append(media_trabalhos)
    linha.append(nota_final)

    matriz.append(linha)

print("\nMatriz de alunos:")
for linha in matriz:
    print(linha)
print()
maior_nota = matriz[0][3]
matricula_maior = matriz[0][0]

for i in range(5):
    if matriz[i][3] > maior_nota:
        maior_nota = matriz[i][3]
        matricula_maior = matriz[i][0]

print(f"\nA matrícula com maior nota final é: {matricula_maior} com a nota de {maior_nota}")
