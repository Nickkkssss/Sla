Escolha = int(input("Quanto espaço pra amuletos você tem? "))
Escolhidos = []
Espaço = 0
while Espaço < Escolha:
    NomeDoAmuleto = input("Qual o nome do amuleto? ")
    EspaçoOcupado = int(input("Quanto espaço ele ocupa? "))
    if EspaçoOcupado < 1:
        print ("Tamanho invalido")
    elif Espaço + EspaçoOcupado > Escolha:
        print ("Esse item ocupa mais espaço do que está disponivel, escolha outro com um valor menor")
    else:
        Escolhidos.append(NomeDoAmuleto)
        Espaço += EspaçoOcupado
        print (f"{NomeDoAmuleto} coube no inventario, sobrando {Escolha - Espaço}")
print ("Você conseguiu os seguintes itens: ")
for amuleto in Escolhidos:
    print (amuleto)
