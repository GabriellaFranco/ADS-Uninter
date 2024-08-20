

def escolha_servico():

    print("Bem-vindo(a) a Copiadora da Gabriella Franco!\n")

    while (True): # Cria um Looping infinito que se repete até o usuário escolher uma opção válida
        print("Entre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico_escolhido = input(">> ").upper()

        if (servico_escolhido == "DIG"): # Testa se o serviço escolhido foi DIG 
            servico = 1.10 # Atribui o valor correspondente ao serviço a variável
            break
        elif (servico_escolhido == "ICO"): # Testa se o serviço escolhido foi ICO
            servico =  1.00
            break
        elif (servico_escolhido == "IPB"): # Testa se o serviço escolhido foi IPB
            servico = 0.40
            break
        elif (servico_escolhido == "FOT"): # Testa se o serviço escolhido foi IPB
            servico = 0.20
            break
        else: # Caso os testes anteriores retornem falso, o usuário digitou um valor inválido
            print("Escolha inválida, entre com o tipo de serviço novamente!\n")
            continue # Redireciona o usuário ao início do Loop

    return servico # Retorna o valor da variável "servico" de acordo com o teste verdadeiro
    
def num_pagina():

    while (True): # Cria um Looping infinito que se repete até o usuário indicar um número válido

        try: # Testa se o usuário inseriu um número inteiro
            pagina_inicial = int(input("Entre com o número de páginas: "))
        except (TypeError, ValueError): # Caso ocorra um dos dois error indicados, o usuário receberá a mensage e erro e será redirecionado ao início do Loop
            print("Ocorreu um erro, por favor entre novamente o número de páginas\n")
            continue

        if (pagina_inicial >= 20 and pagina_inicial < 200): #Testa se o número de páginas inserido é maior ou igual a 20 e menor que 200
            num_paginas = pagina_inicial - (pagina_inicial * (15/100))
            break
        elif (pagina_inicial >= 200 and pagina_inicial < 2000): #Testa se o número de páginas inserido é maior ou igual a 200 e menor que 2000
            num_paginas = pagina_inicial - (pagina_inicial * (20/100))
            break
        elif (pagina_inicial >= 2000 and pagina_inicial < 20000): #Testa se o número de páginas inserido é maior ou igual a 2000 e menor que 10000
            num_paginas = pagina_inicial - (pagina_inicial * (25/100))
            break
        elif (pagina_inicial < 20): #Testa se o número de páginas inserido é menor que 20
            num_paginas = pagina_inicial
            break
        else: # Caso todos os testes retornem falso, o usário digitou um número de páginas acima do aceito pelo sistema
            print("Não aceitamos tantas páginas de uma vez!\n")
            continue

    return num_paginas

def servico_extra():

    while (True): # Cria um Looping infinito que se repete até o usuário escolher uma opção válida
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        res_extra = input(">> ")

        if (res_extra == "1"): # Testa se o usuário selecionu a opção 1
            extra = 15.00
            break
        elif (res_extra == "2"): # Testa se o usuário selecionu a opção 2
            extra = 40.00
            break
        elif (res_extra == "0"): # Testa se o usuário selecionu a opção 0
            extra = 0
            break
        else: # Caso todos os testes retornem falso, o usário digitou uma opção inválida
            print("Opção inválida, tente novamente!\n")
            continue

    return extra

#PROGRAMA PRINCIPAL:

servico = escolha_servico()
num_paginas = num_pagina()
extra = servico_extra()

total = (servico * num_paginas) + extra # Calcula o valor total dos serviços solicitados
print(f"Total: {"%.2f" % total}", f"(Serviço: {"%.2f" % servico} * Páginas: {num_paginas} + Extra: {"%.2f" % extra})")


        

