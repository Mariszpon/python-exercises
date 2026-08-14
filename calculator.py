while True:
    print("\n--- Calculadora ---")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando a calculadora...")
        break
    elif opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if opcao == "1":
                resultado = num1 + num2
                print(f"Resultado da soma: {resultado}")
            elif opcao == "2":
                resultado = num1 - num2
                print(f"Resultado da subtração: {resultado}")
            elif opcao == "3":
                resultado = num1 * num2
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado da divisão: {resultado}")
                else:
                    print("Erro: divisão por zero não é permitida.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
    else:
        print("Opção inválida. Tente novamente.")
