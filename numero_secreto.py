#importou a biblioteca random
import random
#Declarar variáveis
numero_secreto = random.randint (1,10)
tentativas =0
contagem_tentativas = 0
#Intrudução ao jogo
print ("Seja bem-vindo ao jogo do Número Secreto")
print ("Adivinhe o numero de 1 a 10.")
#Laço de repetição
while tentativas != numero_secreto:
    numero = int(input(f"Digite o numero:"))
    contegem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print (f"Você acertou, parabens!")
        print (f"Você precisa de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print ("O numero secreto é maior.")
    else:
        print ("O numero secreto é menor.")
