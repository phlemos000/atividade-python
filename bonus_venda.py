#Solicite os dados ao fornecedor
nome = input ("Digite o nome do vendedor:")
salario_fixo = float(input ("Digite salario fixo:R$"))
total_vendas = int(input("Digite o total de vendas efetuadas:"))
#verifique se a meta foi atingida
if total_vendas >= 20:
    bonus = salario_fixo* 0.15
    salario_recebido = salario_fixo + bonus
    #exibe os resultados 
    print ("\nresultado")
    print (f"meta atingida, {nome}")
    print (f"salario final: R$ {salario_recebido:.2f}")
    print (f"comissão (15%): R$ {bonus:.2f}")
else:
    print ("resultado")
    print (f"meta nao atingida ")