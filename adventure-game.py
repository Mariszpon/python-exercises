print ("Você está em uma floresta. Decida se quer ir para a direita ou esquerda.")
lado = input("Você quer virar para que lado? ")
if lado == 'direita':
    escolha = input("Você encontrou uma montanha. Deseja subir ou voltar? ")
    if escolha == 'subir':
        print ("Você encontra um tesouro no topo.")
    elif escolha == 'voltar':
        print("Você permanece perdido na floresta.")
elif lado =='esquerda':
    escolha2 = input("Você encontra um rio. Deseja atravessar ou voltar? ")
    if escolha2 == 'atravessar':
        print ("Você chega a uma vila segura.")
    else:
        print ("Você permanece perdido na floresta.")
else:
    print ("Você morre.")
