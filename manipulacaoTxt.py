def valida_int(pergunta, min, max):
    x = int(input(pergunta))

    while (x < min or x > max):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #rt - Abre o arquivo para leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+') #wt - Abre o arquivo para escrita e limpa o conteúdo existente nele
        a.close()
    except:
        print('Erro na criação do arquivo...')
    else:
        print(f'O arquivo {nomeArquivo} foi criado com sucesso!\n')

def cadastrarJogo (nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at') #at - Abre o arquivo para escrita, porém preserva o conteúdo já existente nele
    except:
        print('Erro ao abrir o arquivo...')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}\n')
    finally:
        a.close

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo...')
    else:
        print(a.read())
    finally:
        a.close
    

#Programa Principal
arquivo = "games.txt"

if (existeArquivo(arquivo)):
    print('Arquivo localizado!')

else:
    print('Arquivo inexistente...')
    criarArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar um novo item')
    print('2 - Listar os cadastros')
    print('3 - Sair do sistema')

    opcao = valida_int('Escolha uma das opções: ', 1, 3)

    if (opcao == 1):
        nomeJogo = input('Nome do Jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif (opcao == 2):
        listarArquivo(arquivo)

    elif (opcao == 3):
        print('Encerrando o programa...')
        break