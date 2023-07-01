def codigo_cliente():
    try:
      with open('Dados.txt', 'r') as arquivo_leitura:
          linhas = arquivo_leitura.readlines()

      codigo_cliente = int(input("Crie o código do cliente: "))

      for linha in linhas:
          dados = linha.strip().split(',')
          if int(dados[0]) == codigo_cliente:
              print("Erro: O código de cliente já existe no sistema.")
              return

    except ValueError:
        # Capturar erros de valor inválido
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do cliente.")

    except Exception as e:
        # Capturar outros erros
        print("Ocorreu um erro ao cadastrar os dados:", str(e))


def cadastrar_dados_cliente():

  try:
     with open('Dados.txt', 'a') as arquivo:

        # Variáveis para inserir os dados do cliente e seu pet
        codigo_cliente = int(input("Crie o código do cliente: "))
        nome = input("Nome e sobrenome: ")
        contato = int(input("Contato: "))
        endereco = input("Endereço: ")
        bairro = input("Bairro: ")
        cep = int(input("CEP: "))
        ponto_referencia = input("Ponto de referência: ")

        # Exibir uma mensagem para separar os dados do animal dos dados do dono
        print("****************")
        print("Dados do Animal:")
        print("****************")

        nome_animal = input("Nome do animal: ")
        data_nascimento = input("Data de nascimento: ")
        especie = input("Espécie: ")
        raca = input("Raça: ")
        peso = float(input("Peso: "))
        observacoes = input("Observações sobre o animal: ")

        # Formatar os dados do cliente em uma string (criaçao de um dicionario)
        cliente = f"{codigo_cliente}, {nome}, {contato}, {endereco}, {bairro}, {cep}, {ponto_referencia },{nome_animal}, {data_nascimento}, {especie}, {raca}, {peso}, {observacoes}"

        #Escrever a string formatada no arquivo 'Dados.txt' (gravar os dados)
        arquivo.write(cliente)

        #Exibir a mensagem de sucesso caso funcione
        print("Dados cadastrados com sucesso!")

  except ValueError:
      # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
      print("Valor inválido. Certifique-se de digitar um valor numérico para o CÓDIGO, CONTATO, CEP e PESO do cliente.")
  except TypeError:
        # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print("Valor inválido. Certifique-se de digitar um valor numérico para o CÓDIGO, CONTATO do cliente.")
  except Exception as e:
      # Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
      print("Ocorreu um erro ao cadastrar os dados:", str(e))

def listar_dados():
  try:
    #função criada para listar, ler os dados e retornalos como string
      with open('Dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    #se não houverem linhas detectadas, imprimir que nenhum dado existe.
        if not linhas:
          print("Nenhum dado de cliente cadastrado.")

        #Senão, apresentar dados do cliente cadastrado
        else:
            print("Dados dos clientes cadastrados: ")
            for linha in linhas:
                dados = linha.strip().split(',')
                print("Código do cliente:", dados[0])
                print("Nome:", dados[1])
                print("contato:", dados[2])
                print("endereco:", dados[3])
                print("bairro:", dados[4])
                print("cep:", dados[5])
                print("ponto_referencia:", dados[6])
                print("***************")
                print("Dados do Animal")
                print("***************")
                print("nome_animal:", dados[7])
                print("data_nascimento:", dados[8])
                print("especie:", dados[9])
                print("raca:", dados[10])
                print("peso:", dados[11])
                print("observacoes:", dados[12])
  #Se não houver arquivo, imprimir que o arquivo de dados nao foi encontrado. (arquivo inexistente)
  except FileNotFoundError:
    print("Arquivo de dados não econtrado.")
  #Qualquer outro erro que possa ocorrer durante o cadastro dos dados
  except Exception as e:
    print("Ocorreu um erro ao listar os dados:", str(e))


def alterar_dados():

  try:
    # Funçao é aberta em arquivo.readlines para poder ler todas as linhas do arquivo
      with open('Dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    #Verifica se há linhas cadastradas no arquivo, se não há, a mensagem de "Nenhum dado de cliente cadastrado." será exibida.
        if not linhas:
          print("Nenhum dado de cliente cadastrado.")
          return

    #Procura o código do cliente desejado, caso não seja encontrado será false e se encontrar será true
        codigo_cliente = input("Digite o código do cliente que deseja alterar:")
        encontrado = False

    #Abre o arquivo de dados no modo de escrita e ira fazer um for nas linhas e jogar os dados que estao alterados para a nova variavgevl
      with open('Dados.txt', 'w') as arquivo:
        for linha in linhas:
          dados = linha.strip().split(',')
          if dados [0] == codigo_cliente:
              novo_nome = input("Digite o novo nome: ")
              novo_contato = int(input("Digite o novo contato: "))
              novo_endereco = input("Digite o novo endereço: ")
              novo_bairro = input("Digite o novo bairro: ")
              novo_cep = int(input("Digite o novo CEP: "))
              novo_ponto_referencia = input("Digite o novo ponto de referência: ")
              print("***************")
              print("Dados do Animal")
              print("***************")
              novo_nome_animal = input("Digite o novo nome do animal: ")
              novo_data_nascimento = input("Digite a nova data: ")
              novo_especie = input("Digite a nova espécie: ")
              novo_raca = input("Digite a nova raça: ")
              novo_peso = input("Digite o novo peso: ")
              novo_observacoes = input("Digite as novas observações: ")

              #Será gravado no arquivo os novos dados alterados
              nova_linha = f"{novo_nome}, {novo_contato}, {novo_endereco}, {novo_bairro}, {novo_cep}, {novo_ponto_referencia }, {novo_nome_animal}, {novo_data_nascimento}, {novo_especie}, {novo_raca}, {novo_peso}, {novo_observacoes}"
              arquivo.write(nova_linha)
              encontrado = True #se foi encontrado passara para TRUE
              print("Dados do cliente alterados com sucesso!")
          else:
            arquivo.write(linha)
      # Se não foi encontrado, ira imprimir a mensagem comunicando.
      if not encontrado:
        print("Nenhum cliente encontrado com o código fornecido.")

  #Se não houver arquivo, imprimir que o arquivo de dados nao foi encontrado. (arquivo inexistente)
  except FileNotFoundError:
      print("Arquivo de dados não encontrado.")
  #Qualquer outro erro que possa ocorrer durante o cadastro dos dados
  except Exception as e:
    print("Ocorreu um erro ao alterar os dados:", str(e))

def excluir_dados():
  try:
    #Abre o arquivo e verifica se há lihas
    with open('Dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    #Se não houverem dados nas linhas, será imprimida a mensagem abaixo
    if not linhas:
      print("Nenhum dado de cliente cadastrado.")
      return

    #Procura o código do cliente desejado, caso não seja encontrado será false e se encontrar será true
    codigo_cliente = input("Digite o código do cliente que deseja excluir")
    encontrado = False

    #Abre o arquivo para alteração de dados
    with open('Dados.txt', 'w') as arquivo:
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados [0] == codigo_cliente:
              encontrado = True #se foi encontrado passara para TRUE e será excluido
              print("Dados do cliente excluidos com sucesso!")
            else:
              arquivo.write(linha)

            if not encontrado:
              print("Nenhum cliente encontrado com o código fornecido.")
  #Se não houver arquivo, imprimir que o arquivo de dados nao foi encontrado. (arquivo inexistente)
  except FileNotFoundError:
    print("Arquivo de dados não encontrado.")

  #Qualquer outro erro que possa ocorrer durante o cadastro dos dados
  except Exception as e:
    print("Ocorreu um erro ao excluir os dados.", str(e))

def realizar_backup():
    try:
      #Abrira o arquivo em formato de leitura para enviar para a memoria (le o arquivo de origem e envia para a variavel de conteudo)
      with open('Dados.txt', 'r') as arquivo_origem:
        #Abrira o arquivo em formato de escrita para gravar (recebera todo o conteudo que esta na memoria)
          with open('backup_dados.txt', 'w') as arquivo_backup:
              conteudo = arquivo_origem.readlines()
              #conteudo = arquivo_origem.read()
              arquivo_backup.write(conteudo)
          print("Backup do arquivo realizado com sucesso!")
    #Se não houver arquivo, imprimir que o arquivo de dados nao foi encontrado. (arquivo inexistente)
    except FileNotFoundError:
      print("Arquivo de dados não encontrado")
    #Qualquer outro erro que possa ocorrer durante o cadastro dos dados
    except Exception as e:
      print("Ocorreu um erro ao realizar o backup.", str(e))