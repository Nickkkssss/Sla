import random
itens = ["espada", "escudo", "diamante", "poção", "arco"]
coletados = []
pontosItens = [5, 3, 7, 1, 4]
meusPontos = 0
print ("Você finalizou uma masmorra e agora pode escolher quais itens irá coletar.")
for index in range(5):
     escolha = input(f"Você quer pegar este item? {itens[index]}  sim ou não: ")
     if escolha == "sim":
          chance = random.randint(1, 10)
          if chance > 5:
               meusPontos += pontosItens[index]
               print (f"Você conseguiu um {itens[index]} encantado e ganhou {pontosItens[index]} pontos!")
               coletados.append(itens[index] + "Encantado")
          else:
               meusPontos -= pontosItens[index]
               print (f"Você conseguiu um {itens[index]} amaldiçoado e perdeu {pontosItens[index]} pontos!")
               coletados.append(itens[index] + "amaldiçoado")
     else:
          print ("Você não pegou o item")
          
print (f"Você está com esses seguintes itens na sua mochila: {coletados}")
print (f"Você ficou com {meusPontos} pontos!")
