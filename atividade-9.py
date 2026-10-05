estoque = []
for recebimento in range(3):
    item = input("Você está em uma sala, qual item decide pegar? ")
    estoque.append(item)
print ("Você pegou esses itens:")
for item in estoque:
    print (f"-{item}")
pergunta = input("Você quer remover algum item da lista? ")
if pergunta == "sim":
    nome = input("Qual item deseja remover? ")
    posicao = estoque.index(nome)
    estoque.pop(posicao)
    print(estoque)
else:
    ("Você não removeu nada")
apagar = input("Deseja encerrar o turno? ")
if apagar == "sim":
    estoque.clear()
else:
    print ("Você não encerrou o turno")
