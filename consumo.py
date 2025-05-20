# solicita ao usuário a quantidade de quilômetros percorridos
km = float(input("Digite a quantidade de km percorridos: "))
#solicita ao usuário a quantidade de litros consumidos
litros = float (input("Digite a quantidae de litros de combustível consumidos:"))
# calcula o consumo médio 
if litros != 0:
    consumo = km /litros 
    print(f"o consumo médio do carro é de {consumo:.2f}KM/L")
else:
    print("Não foi possível calcular o consumo com 0 litros.")
    print("Por gentileza, digite valores numéricos válidos.")
