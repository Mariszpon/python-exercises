palavra = input("Digite uma palavra: ")
while len(palavra) < 3 or len(palavra) > 10:
    print ("O palavra deve estar entre 3 e 10 letras.")
    palavra = input ("Digite uma palavra: ")
print (f"A palavra digitada foi {palavra} e ela tem {len(palavra)} letras.")
