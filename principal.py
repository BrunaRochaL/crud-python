from funcoesbruna import *
opcao = 1

while opcao:
  print("*******Escolha a opção********")
  print("1. Cadastrar dados do cliente")
  print("2. Listar dados do cliente")
  print("3. Alterar dados do cliente")
  print("4. Excluir dados do cliente")
  print("5. Realizar Backup do arquivo")
  print("6. Sair")


  opcao = int(input("Digite sua opção:"))

  if(opcao==1):
    cadastrar_dados_cliente()

  elif(opcao==2):
    listar_dados()

  elif(opcao==3):
    alterar_dados()

  elif(opcao==4):
    excluir_dados()

  elif(opcao==5):
    realizar_backup()

  elif(opcao==6):
    print("Encerrando o programa...")
    break
  else:
    print("Opção inválida. Por favor, escolha uma opção valida.")