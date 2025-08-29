perguntas = ["qual raiz quadrada de 64", "Quanto é 4x8", "Qual a capital do Ceara"]
respostacerta = ["8", "32", "Fortaleza"]
acertos = 0

for numeropergunta in range(3): 
    print (perguntas[numeropergunta])
    respostas = input ("Resposta: ")
    if respostas == respostacerta[numeropergunta]: 
        acertos += 1
        print ("parabens, voce acertou")
    elif respostas == "":
        print ("voce digitou nada")
    else: 
        print ("Você errou")


if acertos == 0:
    print ("Voce errou todas")
elif acertos == 1:
    print ("voce acertou somente 1 pergunta")
elif acertos == 2 :
    print ("voce acertou somente 2 perguntas")
elif acertos == 3:
    print ("voce acertou 3 perguntas, parabens")
