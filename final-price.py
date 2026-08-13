custo_por_kg = float(input("Custo por kg: "))
lucro_desejado = float(input("Lucro desejado: "))
preço_de_venda = custo_por_kg * (1+lucro_desejado)
preço_total = input(f"O total é {preço_de_venda}")
