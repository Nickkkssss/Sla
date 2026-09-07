import random
estoqueLoja = []
listaPreco = []
geo = 200
sair = False
while True:
    item = input("Digite o nome do item ('sair' para parar): ")
    if item == "sair":
        break
    else:
        estoqueLoja.append(item)
        precoEstoque = random.randint(10, 100)
        print(f"\n{item} custa {precoEstoque} geos.")
        listaPreco.append(precoEstoque)
print(f"Estoque da loja: {estoqueLoja}")
print(f"A loja tem {len(estoqueLoja)} itens à venda.")
while geo > 0 and len(estoqueLoja) > 0 and sair == False:
    compra = input(f"\nDeseja comprar qual item? {estoqueLoja} (Digite 'sair' para parar)")
    precoCompra = 0
    if compra != "sair":
        for index in range(len(estoqueLoja)):
            if estoqueLoja[index] == compra:
                precoCompra = listaPreco[index]
        if precoCompra == 0:
            print ("Esse item não está na loja")
        else:
            print (f"O preço do item é {precoCompra}")
            if geo >= precoCompra:
                geo -= precoCompra
                print(f"Compra realizada! Você gastou {precoCompra} geos. Restam {geo} geos.\n")
                estoqueLoja.pop(index) 
                listaPreco.pop(index)
            else:
                print(f"Compra cancelada! Você não tem geos suficientes.\n")
    else:
        sair = True
resposta = input("\nDeseja resetar a loja? (sim/não): ")
if resposta == "sim" and geo <= 50:
    estoqueLoja.clear()
    print("A loja foi resetada")
elif resposta == "sim":
    print("Reset não permitido, só é possivel resetar com o geo abaixo de 50")
    print(f"Geo atual: {geo}")
else:
    print("Loja não resetada")
print(f"\nVocê terminou com {geo} geos")
if len(estoqueLoja) == 0:
    print("A loja está vazia")
else:
    print(f"A loja ainda tem {len(estoqueLoja)} itens: {estoqueLoja}")
