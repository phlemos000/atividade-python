# Exibir ou menu de conversao
print ("\n---conversor de calculadora---")
print("1- celsius para fahrenheit")
print ("2- celsius para kelvin")

#solicite uma opcao do usuario 
opcao = float(input("esclha uma opcao (1 ou 2):"))

#verifique a opcao escolhida 
if opcao  == 1:
    temperatura_celsius = float(input("Digite a temperatura em celsius"))
    fahrenheit = (temperatura_celsius *9/5)+32
    print (f"resultado : {temperatura_celsius}°C ={fahrenheit:.2F}°F")
elif opcao ==2:
    temperatura_celsius = float(input("digite a temperatura em celsius:*"))
    kelvin = temperatura_celsius +273,15 
    #correcao da formula: = 273,15 e o valor para kelvin 
    print (f"resultado:{temperatura_celsius}°c={kelvin:.f}")

