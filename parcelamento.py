#solicite ao usuario o valor total da compra
valor_total = float(input("Digite o valor total da compra; R$"))
#calcula o valor de cada um das 5 prestações (sem juros)
prestacao = valor_total / 5 
#Exibe os resultados
print("\nResumo da compra:")
print(f"Valor total: R$ {valor_total:.2f}")
print (f"Valor de cada prestações: R$ {prestacao:.2f}") 