import random
mochila = ["Bumerangue", "Planador"]
print ("\nA equipe avatar estão indo a Ilha do sol de inverno! Pegue coisas pra mochila deles")
for dia in range (1, 11):
    print (f"\nDia {dia}")
    evento = random.randint(1, 12)
    if evento < 5:
        print ("\nVocê achou um vilarejo amigavel!")
        item = input("Eles te concederam um item, qual o nome dele? ")
        mochila.append(item)
    elif evento < 9:
        item = input("\nSokka achou algo! Qual item? ")
        mochila.insert(0, item)
    elif evento < 11:
        print ("\nLadrões tentaram te roubar!")
        if len(mochila) > 0:
            mochila.pop
            print("Eles roubaram o ultimo item da sua mochila!")
        else:
            print ("Como os assaltantes não encontraram nada para assaltar eles mataram vocês.")
            break
    else:
        mochila.clear()
        print ("\nVocês se deram de cara com a nação do fogo e fugiram, perdendo todos os itens na mochila") 
if len(mochila) > 5:
    print ("\nO grupo chegou a Ilha do Sol de inverno com folga!")
if len(mochila) > 1:
    print ("\nO grupo chegou mas passou dificuldades no caminho!")
else:
    print ("\nO grupo não conseguiu chegar")
