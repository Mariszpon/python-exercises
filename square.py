coordenada_x = int(input("Digite uma coordenada (x): "))
coordenada_y = int(input("Digite uma coordenada (y): "))
if 10 > coordenada_x > 0 and 10 > coordenada_y > 0:
    print ("Dentro do quadrado.")
elif coordenada_x == 0 or coordenada_x == 10 and coordenada_y == 0 or coordenada_y == 10:
    print ("Na fronteira.")
else:
    print ("Fora do quadrado.")
