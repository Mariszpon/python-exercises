usuario = input("Qual seu usuário: ")
if usuario == "admin":
    senha = input("Qual a senha? ")
    if senha == "1234":
        print("Senha válida!")
    else:
        print ("Senha inválida!")
elif usuario == "convidado":
    senha = input ("Qual a senha? ")
    if senha == "1234":
        print ("Senha válida!")
    else:
        print ("Acesso restrito.")
else:
    print ("Acesso bloqueado.")
