import random
filaClientes = []
clientes = True
geoGanho = 0
while clientes == True:
    nomeCliente = input("Escolha o nome do seu cliente (Digite fim para parar): ")
    if nomeCliente == "fim":
        clientes = False
    else:
        filaClientes.append(nomeCliente)
print (f"Você tem {len(filaClientes)} clientes esperando")
for atendimento in range(len(filaClientes)):
    clienteAtual = filaClientes.pop(0)
    valorCompra = random.randint(5, 50)
    print(f"{clienteAtual} comprou algo e pagou {valorCompra} geos!")
    geoGanho += valorCompra
if geoGanho >= 100:
    print ("Foi um ótimo dia de vendas!")
elif geoGanho >= 50:
    print ("Foi um dia razoavel de vendas!")
else:
    print ("Hoje foi um dia fraco de vendas!")
filaClientes.clear()
print (f"Agora tem {len(filaClientes)} pessoas na sua fila!")
