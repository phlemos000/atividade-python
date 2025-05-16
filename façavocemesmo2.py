#Solicitar ao usuario o valor total da compra 
valor_total = float (input("Digite o valor total a compra ; R$"))
 
#calcula o valor de cada uma das 5 prestações ( sem juros)
prestacao = valor_total / 5

# Exibir os resultados 
print("\nresumo da compra :")
print(f"valor total da compra: R$ {valor_total:.2f}")
print("valor de cada prestações: R$ {prestação:.2f}")
