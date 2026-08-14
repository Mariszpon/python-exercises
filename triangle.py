a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
if a + b > c and a + c > b and b + c > a:
    print("Os lados podem formar um triângulo.")
if a == b ==c:
    tipo = "Equilátero"
elif a ==b or a== c or b == c:
    tipo = "Isósceles"
else:
    tipo = "Escaleno"
print ("Tipo:", tipo)
