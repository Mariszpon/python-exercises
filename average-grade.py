def main():
    numeros = []
    while True:
        try:
            n = float(input("Digite um número (-1 para encerrar): "))
            if n == -1:
                if len(numeros) > 0:
                    media = sum(numeros) / len(numeros)
                    print(f"A média dos números é: {media:.2f}")
                else:
                    print("Nenhum número foi fornecido.")
                break
            else:
                numeros.append(n)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
    main()
