#inicializando variaveis
numero1 =0
numero2 =0
resultado =0
opcao = -1
while opcao !=0:
    #exibindo menu
  print("\n---calculadira---")
  print("1-soma")
  print("2-subtrair")
  print("3-multiplicar")
  print("4-dividir")
  print("0-sair")
#solicitar que o usuario escolha uma opcao
  opcao = int(input("Qual opção deseja:"))
  #verifica se se a opcao esta entre 1 ou 4
  if opcao in[1,2,3,4]:
  #solicitar os numeros
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero:"))
  #realizar a operacao correspondente
  if opcao ==1: 
    resultado = numero1+ numero2
    print(f"resultado da soma:{resultado}")
  elif opcao ==2:
    resultado =numero1- numero2
    print(f"resultado da subtração: {resultado}")
  elif opcao ==3:
    resultado =numero1 * numero2
    print(f"resultado da multiplicação: {resultado}")
  elif opcao ==4:
    resultado =numero1 / numero2
    print(f"resultado da divisão: {resultado}")
  elif opcao == 0:
    print("encerrando a calculadora.Volte sempre!")
    break
  else:
  #mensagem de erro para opções invalidas
    print("opcao invalida.Por favor, escolha uma opção valida.")