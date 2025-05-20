#Solicitar dados ao usuário
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
 #Calcular o imc
imc = peso / (altura * altura)
 #Mostrar resultado do IMC
print(f"\n{nome}, o resultado é:{imc:.2f}")
 #Classificação com baseno valor do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Classificação: Peso normal.")
elif imc >= 25.0 and imc <= 29.9:
    print("Classificação: Sobrepeso.")
elif imc >= 30.0:
    print("Classificação: Obesidade.")