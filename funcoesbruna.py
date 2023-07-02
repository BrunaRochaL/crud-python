#Cria uma exception especifica para códigos duplicados (aparece quando digitarem um cõdigo que já existe)
class BadCodigo(Exception): #class classificara uma classe de exception e pass para não resultar em erro de sintaxe
    pass

#A função fara com que se qualquer caractere do valor for um digito ira resultar em erro e pedira para digitar uma resposta valida
def input_texto(prompt):
    valor = input(prompt) #prompt é o campo que esta sendo preenchido
    if any(char.isdigit() for char in valor):
        raise TypeError(prompt + "por favor digite um valor válido como texto!") #raise levantara a excessão
    return valor


# A função ira verificar se o valor digitado no prompt será um digito inteiro ou não e ira solicitar que digite novamente, caso seja invalido.
def input_int(prompt):
      valor = input(prompt)
      if valor.isdigit():
          return int(valor)
      else:
          raise TypeError(prompt + "por favor digite um valor válido como número inteiro!")

# A função ira verificar se o valor digitado no prompt será um float e ira solicitar que digite novamente, caso seja invalido.
def input_float(prompt):
      valor = input(prompt)
      try:
          return float(valor)
      except ValueError:
          raise TypeError(prompt + "por favor digite um valor válido como número decimal!")

def obter_codigo_cliente():
    #Ira abrir o documento em modo de leitura
    with open('Dados.txt', 'r') as arquivo_leitura:
        #ira adicionar um array de linhas na variavel
          linhas = arquivo_leitura.readlines()

    #Solicita criar um código para o cliente e ira ler linha por linha, caso o código ja seja existente no sistema, será informado que já existe no sistema
    codigo_cliente = int(input("Crie o código do cliente: "))
    if not linhas:
        return codigo_cliente
    for linha in linhas:
        dados = linha.strip().split(',')
        if dados[0].isdigit() and int(dados[0]) == codigo_cliente:
          raise BadCodigo("Erro: O código de cliente já existe no sistema.")
          return
        else:
          return codigo_cliente


def cadastrar_dados_cliente():
  try:
      #Abre o código em modo de adicionar dados
     with open('Dados.txt', 'a') as arquivo:

        # Variáveis para inserir os dados do cliente
        codigo_cliente = obter_codigo_cliente()
        nome = input_texto("Nome e sobrenome: ")
        contato = input("Contato: ")
        endereco = input("Endereço: ")
        bairro = input_texto("Bairro: ")
        cep = input_int("CEP: ")
        ponto_referencia = input_texto("Ponto de referência: ")

        # Exibir uma mensagem para separar os dados do animal dos dados do dono
        print("****************")
        print("Dados do Animal:")
        print("****************")

        nome_animal = input_texto("Nome do animal: ")
        data_nascimento = input("Data de nascimento: ")
        especie = input_texto("Espécie: ")
        raca = input_texto("Raça: ")
        peso = input_float("Peso: ")
        observacoes = input("Observações sobre o animal: ")

        # Formatar os dados do cliente em uma string (criaçao de um dicionario)
        cliente = f"{codigo_cliente}, {nome}, {contato}, {endereco}, {bairro}, {cep}, {ponto_referencia },{nome_animal}, {data_nascimento}, {especie}, {raca}, {peso}, {observacoes}\n"

        #Escrever a string formatada no arquivo 'Dados.txt' (gravar os dados)
        arquivo.write(cliente)

        #Exibir a mensagem de sucesso caso funcione
        print("Dados cadastrados com sucesso!")
  except BadCodigo as e:
      print(e)
  except TypeError as e:
        # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print(e)
  except Exception as e:
      # Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
      print("Ocorreu um erro ao cadastrar os dados:", str(e))

def listar_dados():
    try:
        # Função criada para listar, ler os dados e retorná-los como string
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        # Se não houverem linhas detectadas, imprimir que nenhum dado existe.
        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return

        codigo_cliente = input("Digite o código do cliente que deseja buscar: ")
        encontrado = False
        # Senão, apresentar dados do cliente cadastrado
        print("Dados dos clientes cadastrados: ")
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados[0] == str(codigo_cliente):
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
                encontrado = True
                break
        if not encontrado:
            print("Nenhum cliente encontrado com o código fornecido.")
    # Se não houver arquivo, imprimir que o arquivo de dados nao foi encontrado. (arquivo inexistente)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    # Qualquer outro erro que possa ocorrer durante o cadastro dos dados
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
    #Abre o arquivo de dados no modo de escrita e ira fazer um for nas linhas e jogar os dados que estao alterados para a nova variavel
      with open('Dados.txt', 'r+') as arquivo:
        for linha in linhas:
          dados = linha.strip().split(',')
          if dados[0] == codigo_cliente:
              novo_nome = input_texto("Digite o novo nome: ")
              novo_contato = input("Digite o novo contato: ")
              novo_endereco = input("Digite o novo endereço: ")
              novo_bairro = input_texto("Digite o novo bairro: ")
              novo_cep = input_int("Digite o novo CEP: ")
              novo_ponto_referencia = input_texto("Digite o novo ponto de referência: ")
              print("***************")
              print("Dados do Animal")
              print("***************")
              novo_nome_animal = input_texto("Digite o novo nome do animal: ")
              novo_data_nascimento = input("Digite a nova data: ")
              novo_especie = input_texto("Digite a nova espécie: ")
              novo_raca = input_texto("Digite a nova raça: ")
              novo_peso = input_float("Digite o novo peso: ")
              novo_observacoes = input("Digite as novas observações: ")

              #Será gravado no arquivo os novos dados alterados
              nova_linha = f"{codigo_cliente}, {novo_nome}, {novo_contato}, {novo_endereco}, {novo_bairro}, {novo_cep}, {novo_ponto_referencia }, {novo_nome_animal}, {novo_data_nascimento}, {novo_especie}, {novo_raca}, {novo_peso}, {novo_observacoes}\n"
              print(nova_linha)
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
  except TypeError as e:
  # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
      print(e)
  #Qualquer outro erro que possa ocorrer durante o cadastro dos dados
  except Exception as e:
    print(e)

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
    codigo_cliente = input("Digite o código do cliente que deseja excluir: ")
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
        # Abrir o arquivo de origem em formato de leitura para enviar para a memória
        with open('Dados.txt', 'r') as arquivo_origem:
            linhas = arquivo_origem.readlines()
        # Abrir o arquivo de backup em formato de escrita para gravar o conteúdo
        with open('backup_dados.txt', 'w') as arquivo_backup:
            for linha in linhas:
                arquivo_backup.write(linha)
        print("Backup do arquivo realizado com sucesso!")
    # Se o arquivo não for encontrado, imprimir que o arquivo de dados não foi encontrado (arquivo inexistente)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    # Qualquer outro erro que possa ocorrer durante o backup dos dados
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup:", str(e))

