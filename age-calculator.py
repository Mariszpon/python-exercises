ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = int(ano_atual) - int(ano_de_nascimento)
print(format(f"Sua idade é {idade}"))
print ()
idade_em_meses = int(idade)*12
idade_em_meses2 = input(f"Sua idade em meses é: {idade_em_meses}")
