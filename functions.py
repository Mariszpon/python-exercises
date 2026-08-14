# 1. Função soma_elementos
def soma_elementos(lista):
    return sum(lista)

# 2. Função e_palindromo
def e_palindromo(texto):
    return texto == texto[::-1]

# 3. Função maior_elemento
def maior_elemento(lista):
    return max(lista)

# 4. Função contar_caracteres
def contar_caracteres(texto, caractere):
    return texto.count(caractere)

# 5. Calculadora simples
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def exibir_menu():
    print("\n--- Calculadora Simples ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calculadora():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Encerrando a calculadora...")
            break

        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
                continue

            if opcao == "1":
                print("Resultado:", soma(num1, num2))
            elif opcao == "2":
                print("Resultado:", subtracao(num1, num2))
            elif opcao == "3":
                print("Resultado:", multiplicacao(num1, num2))
            elif opcao == "4":
                print("Resultado:", divisao(num1, num2))
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso das funções
print(soma_elementos([1, 2, 3, 4]))          # 10
print(e_palindromo("arara"))                 # True
print(maior_elemento([10, 25, 3, 7]))        # 25
print(contar_caracteres("banana", "a"))      # 3

# Executar a calculadora
calculadora()

# 6. Função imprimir_nome
def imprimir_nome():
    print("Mariana")  # substitua pelo seu nome

# 7. Função maior
def maior(a, b, c):
    return max(a, b, c)

# 8. Função criar_vetor
def criar_vetor():
    return [0] * 5

# 9. Função media
def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# 10. Função inverter
def inverter(texto):
    print(texto[::-1])

# 11. Função imprime_diagonal
def imprime_diagonal(matriz):
    for i in range(3):
        print(matriz[i][i])


# Testes
imprimir_nome()                       # Mariana
print(maior(10, 25, 7))               # 25
print(criar_vetor())                  # [0, 0, 0, 0, 0]
print(media([10, 20, 30]))            # 20.0
inverter("Python")                    # nohtyP
imprime_diagonal([[1,2,3],[4,5,6],[7,8,9]])  # 1, 5, 9
