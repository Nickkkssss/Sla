import random
bolsa = []
itens = ["Moedas de ouro", "Mapa da rota de fuga", "Chá de jasmim", "Adaga da familia real", "Roupas de disfarce"]
for comodo in range(5):
    print ("\nZuko e Iroh estão fugindo da nação do fogo e terão que passar por 5 salas para fugir sem serem pegos")
    encontro = random.randint(1, 5)
    itemEncontrado = itens[encontro - 1]
    print (f"\nEles encontraram {itemEncontrado}")
    acao = input("\nQuer ficar com o item? (Digite 'sim' ou 'não' ou 'soltar'): ")
    if acao == "sim":
        if len(bolsa) >= 3:
            print ("Não há mais espaço dentro da bolsa, não pode levar o item")
        else:
            bolsa.append(itemEncontrado)
            print (f"{itemEncontrado} foi para a bolsa")
    elif acao == "soltar":
        if len(bolsa) == 0:
            print("\n A bolsa está vazia, não tem nada para soltar")
        else:
            for posicao in range(len(bolsa)):
                print(f"{posicao} - {bolsa[posicao]}")
            numero = int(input("Digite o numero do item que quer soltar:"))
            if numero >= 0 and numero < len(bolsa):
                itemRemovido = bolsa.pop(numero)
                print (f"\nEles deixaram {itemRemovido} para trás")
            else:
                print ("Numero invalido")
    else:
        print ("Eles não pegaram o item")
print ("\nEles conseguiram escapar, esses foram os itens que ficaram na bolsa:")
print (bolsa)
esvaziar = input("Você quer esvaziar a bolsa? ('sim' ou 'não') ")
if esvaziar == "sim":
    bolsa.clear()
    print ("Bolsa esvaziada")
else:
    print ("Você não esvaziou")
