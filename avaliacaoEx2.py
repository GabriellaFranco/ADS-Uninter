acc = 0

# Menu da Loja
print("Bem-vindo(a) a loja de gelados da Gabriella Franco!\n")
print("-" * 16, " CARDÁPIO ", "-" * 16)
print("-" * 44)
print("-" * 3, "| Tamanho", "| CUPUAÇU (CP)|", "AÇAÍ (AC)|", "-" * 3,)
print("-" * 3,"|    P    |", "  R$9.00    |", " R$11.00 |", "-" * 3)
print("-" * 3, "|    M    |", "  R$14.00   |", " R$16.00 |", "-" *3)
print("-" * 3, "|    G    |", "  R$18.00   |", " R$20.00 |", "-" * 3)
print("-" * 44)
print("-" * 44)

while (True): # Looping infinito que é executado até o cliente informar que não deseja mais nenhum produto
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
    if (sabor != "CP") and (sabor != "AC"): # Testa se o sabor informado é válido
        print("Sabor inválido, tente novamente!\n")
        continue # Redireciona o usuário ao início do Loop
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if(tamanho != "P") and (tamanho != "M") and (tamanho != "G"): # Testa se o tamanho informado é válido
        print("Tamanho inválido, tente novamente!\n")
        continue 

    if (sabor == "CP" and tamanho == "P"): # Testa se o sabor inserido é Cupuaçu e o tamanho "P"
        acc += 9 # Adiciona o valor do item ao acumulador
        print("Você pediu um Cupuaçu no tamanho P: R$ 9.00")
    elif (sabor == "CP" and tamanho == "M"): # Testa se o sabor inserido é Cupuaçu e o tamanho "M"
        acc += 14
        print("Você pediu um Cupuaçu no tamanho M: R$ 14.00") 
    elif (sabor == "CP" and tamanho == "G"): # Testa se o sabor inserido é Cupuaçu e o tamanho "G"
        acc += 18
        print("Você pediu um Cupuaçu no tamanho G: R$ 18.00")
    elif (sabor == "AC" and tamanho == "P"): # Testa se o sabor inserido é Açaí e o tamanho "P"
        acc += 11
        print("Você pediu um Açaí no tamanho P: R$ 11.00")
    elif (sabor == "AC" and tamanho == "M"): # Testa se o sabor inserido é Açaí e o tamanho "M"
        acc += 16
        print("Você pediu um Açaí no tamanho M: R$ 16.00")
    else: # Caso todos os testes sejam falsos, o sabor inserido é Açaí e o tamanho "G"
        acc += 20
        print("Você pediu um Açaí no tamanho G: R$ 20.00")

    mais_itens = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper()
    if(mais_itens == "N"): # Testa se o usuário não quer comprar novos itens
        break # Encerra o Loop e segue para a apresentação do valor da compra
    else:
        continue # Volta ao início do Loop

print(f"\nO valor total a ser pago: R$ {"%.2f" % (acc)}") # Apresenta o valor do acumulador em float com duas casas decimais
