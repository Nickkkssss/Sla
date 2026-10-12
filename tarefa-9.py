import random
evento = ["Novo Pedido Comum", "Pedido Prioritário", "Cancelamento", "Prato do fundo pronto", "Agilizar pedido", "Inspeção da Vigilância Sanitária"]
pontos = 0
pedidos = ["Hamburguer", "Pizza"]
print ("Você é um chefe de cozinha que precisa chegar a 100 pontos para poder finalizar seu turno!")
while pontos < 100:
    print (f"\nVocê tem {pontos} pontos / Essa é sua lista de pedidos: {pedidos}")
    Ievento = random.randint(0, 5)
    if Ievento == 0:
        pedido = input("\nColoque um pedido no começo da lista: ")
        pedidos.insert(0, pedido)
        pontos += 10
    elif Ievento == 1:
        print ("\nVocê recebeu um pedido prioritario")
        pedido = input("Qual nome do pedido? ")
        pedidos.append(pedido)
        pontos += 15
    elif Ievento == 2:
        print ("\nUm cliente decidiu cancelar seu pedido")
        pedidoRemovido = input("Qual pedido removido? ")
        pedidoEncontrado = False
        for prato in pedidos:
            if prato  == pedidoRemovido:
                pedidoEncontrado = True
                print("\nVocê cancelou o pedido do cliente")
                pedidos.remove(pedidoRemovido)
                pontos += 10
        if pedidoEncontrado == False:
            print("\nVocê não cancelou o pedido do cliente, atrasando todos")
            pontos -= 10
    elif Ievento == 3:
        if len(pedidos) > 0:
            pratoRemovido = pedidos.pop()
            print(f"\nO prato do fundo ficou pronto, removendo o {pratoRemovido} dos seus pedidos!")
            pontos += 10

    elif Ievento == 4:
        if len(pedidos) > 0:
            pedidoAgilizado = random.randint(0, len(pedidos) - 1)
            pedidoRemovido = pedidos.pop(pedidoAgilizado)
            print (f"Um {pedidoRemovido} foi agilizado pela equipe e tirado da lista! (Na posição {pedidoAgilizado})")
            pontos += 20
    else:
        print ("\nA vigilancia sanitaria veio visitar seu restaurante, decida oq vai fazer: ")
        print ("1- Tirar todos os itens da lista para organizar a cozinha")
        print ("2- Ignorar o inspetor perdendo pontos")
        decisao = int(input("Oq você vai fazer? "))
        if decisao == 1:
            pedidos.clear()
            print ("\nVocê tirou todos os pedidos da lista para organizar a cozinha")
            pontos += 30
        elif decisao == 2:
            print ("\nVocê ignorou o inspetor. Como você não fez nada o inspetor encontrou problemas na cozinha e você perdeu pontos")
            pontos -= 50
        else:
            print("\nEssa opção não existe. Como você não fez nada o inspetor encontrou problemas na cozinha e você perdeu pontos")
            pontos -= 60
print (f"\nFinal do expediente, você conseguiu {pontos} pontos!")
print (f"Essa foi a lista de pedidos que você deixou para o proximo chefe: {pedidos}")
