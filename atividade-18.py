itens = ["espada", "escudo", "diamante", "poção", "arco"]
coletados = []
print ("Você finalizou uma masmorra e agora pode escolher quais itens irá coletar.")
for item in itens:
     escolha = input("Você quer pegar este item? " + item + " sim ou não: ")
     if escolha == "sim":
          coletados.append(item)
print (coletados)
