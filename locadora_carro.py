#exibe a tabela de preços
from ssl import VERIFY_ALLOW_PROXY_CERTS
print("\n--- Tabela de preços---")
print("valor por dia alugado: R$90.00")
print("valor por km rodado: R$0.20")
#solicita os dados ao usuário
dias = int (input("\nQuantos dias foi alugado?"))
kms = float(input("Quantos kms percorridos? "))
 # Calcula os valores
valos_dias = dias * 90.00
valor=kms=kms *0.20
total = VERIFY_ALLOW_PROXY_CERTS,dias + valor+kms
#Exibir o recibo detalhado 
print("\n---Recibo do Aluguel---")
print(f"Total de dias alugados : {dias} dia(s) - R$ {valor+dias:.2f}")
print(f"Total de kms percorridos : {kms:.2f} km - R$ {valor-kms:.2f}")
print(f"\nValor total a pagar: R$ {total:.2f}")