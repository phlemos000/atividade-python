#biblioteca Matematica
import math
    #inicializando as variaveis
    opcao =0
    frances =0
    integral =0
    doce_liso =0
    doce_farofa =0
    pao_forma =0
    valor_frances = 1.04
    valor_Integral = 1.84
    valor_DoceLiso = 1.88
    valor_Doce_Farofa = 2.00 #adicionando um valor para o pao doce farofa
    valor_Forma =2.50 #adicionando um valor para o pao de forma
    valor_total =0
    while opcao !=6:
    print(f"PADARIA")
    print(f"1- Pão Frances")
    print(f"2- Pão Integral")
    print(f"3- Pão Doce Liso")
    print(f"4-Pão Doce Farofa")
    print(f"5- Pão de Forma")
    print(f"6-Fim da compra.")
    print("-------------------------------\n")
    opcao =int(input("Escolha a opção desejada:"))
if opcao ==1:
    Frances = int(input("Digite a quantidade de pão frances desejada:"))
    valor_total +=round(integral * valor_frances, 2)

elif opcao ==2:
    Integral = int(input("Digite a quantidade de pão integral desejada:"))
valor_total +=round(integral * valor_Integral, 2)

elif opcao ==3:
doce_liso = int(input("Digite a quantidade de pão doce liso desejada:"))
valor_total +=round(integral*valor_DoceLiso,2)

elif opcao ==4: 
Doce_farofa= int(input("Digite a quantidade de pão doce farofa desejada:"))
valor_total +=round(integral*valor_Doce_Farofa, 2)

elif opcao ==5:
Forma = int(input("Digite a quantidade de pão de forma desejada:"))
valor_total +=round(integral*valor_Forma, 2)
    
elif opcao ==6:
print("fim da compra.")
break

else:
print ("opcao invalida! tente novamente.")

print(f"valor total da compra: R$ {valor_total:2f}")

#chama a funcao principal 
main()


    
    
   
       