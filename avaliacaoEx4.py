lista_livro = []
id_global = 0

def cadastrar_livro(id):

    print("-" * 34)
    print("-" * 6, "MENU CADASTRAR LIVRO", "-" * 6)
    print(f"Id do livro: {id}")
    nome_livro = input("Por favor entre com o nome do livro: ")
    autor_livro = input("Por favor entre com o autor do livro: ").upper()
    editora_livro = input("Por favor entre com a editora do livro: ")

    dic_livro = {'id': id, 'nome livro': nome_livro, 'autor': autor_livro, 'editora': editora_livro}
    lista_livro.append(dic_livro) # Acrescente o dicionário dentro da lista_livro

def consultar_livro():

    print("-" * 34)
    print("-" * 6, "MENU CONSULTAR LIVRO", "-" * 6)

    while(True):
        print("Escolha a opção desejada: ")
        print("1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao Menu")
        res_consulta = input(">> ")

        if (res_consulta == "1"): # Testa se o input do usuário é igual a 1
            for i in range (0, len(lista_livro)): # Percorre toda a lista_livro, de um em um, e armazena os valores na variável i
                print(f"\nID: {lista_livro[i]['id']}")
                print(f"Nome do livro: {lista_livro[i]['nome livro']}")
                print(f"Autor: {lista_livro[i]['autor']}")
                print(f"Editora: {lista_livro[i]['editora']}")
                print("-" * 20)
        elif (res_consulta == "2"): # Testa se o input do usuário é igual a 2
            id_consulta = int(input("Informe o ID do livro: "))
            for i in range (0, len(lista_livro)):
                if (lista_livro[i]['id'] == id_consulta): # Testa se o atributo id guardado na variável i é igual ao id inserido pelo usuário
                    print(f"\nID: {lista_livro[i]['id']}")
                    print(f"Nome do livro: {lista_livro[i]['nome livro']}")
                    print(f"Autor: {lista_livro[i]['autor']}")
                    print(f"Editora: {lista_livro[i]['editora']}")
                    print("-" * 20)
                    break
        elif (res_consulta == "3"): # Testa se o input do usuário é igual a 3
            res_autor = input("Informe o nome do Autor(a) que deseja buscar: ").upper()
            for i in range(0, len(lista_livro)):
                if (lista_livro[i]['autor'] == res_autor): # Testa se o nome do autor guardado na variável i é igual ao autor inserido pelo usuário
                    print(f"\nID: {lista_livro[i]['id']}")
                    print(f"Nome do livro: {lista_livro[i]['nome livro']}")
                    print(f"Autor: {lista_livro[i]['autor']}")
                    print(f"Editora: {lista_livro[i]['editora']}")
                    print("-" * 20)
        elif (res_consulta == "4"):  # Testa se o input do usuário é igual a 4      
            return # Encerra a função e volta ao menu principal
        else: # Testa se o usuário inseriu uma opção inválida
            print("Opção inválida, tente novamente!")
            continue # Retorna ao início do Loop
                 
def remover_livro():

    achou = False
    print("-" * 34)
    print("-" * 7, "MENU REMOVER LIVRO", "-" * 7)

    while (True):
        id_remover = int(input("Informe o ID do livro a ser removido: "))
        for i in range(0, len(lista_livro)):
            if (lista_livro[i]['id'] == id_remover): # Testa se o atributo id guardado na variável i é igual ao id inserido pelo usuário
                achou = True
                del(lista_livro[i]) # Caso achou = True, remove o livro
                print("Livro removido com sucesso!")
                return # Encerra a função e retorna ao menu principal
        if(achou == False): # Testa se o id inseido pelo usuário existe na lista de registros
            print("ID inválido!") 
            continue # Retorna ao início do Loop
                
# CÓDIGO PRINCIPAL

print("Bem-vindo(a) a Livraria da Gabriella Franco!")

while (True):
    print("-" * 34)
    print("-" * 9, "MENU PRINCIPAL", "-" * 9)
    print("Escolha a opção desejada: ")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    res_principal = input(">> ")

    if (res_principal == "1"):
        id_global = id_global + 1
        cadastrar_livro(id_global)
    elif (res_principal == "2"):
        consultar_livro()
    elif(res_principal == "3"):
        remover_livro()
    elif (res_principal == "4"):
        break
    else:
        print("Opção inválida, tente novamente!")
        continue
