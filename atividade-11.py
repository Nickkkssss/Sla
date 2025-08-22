import random
minimo = float(input("escolha o numero minimo: "))
maximo = float(input("escolha o numero maximo: "))
vida = float(input("escolha o numero de tentativas: "))
numero = random.randint(int(minimo), int(maximo))
escolha = 0
while escolha != numero and vida > 0:
    escolha = float(input("escolha um numero entre " + str(minimo) + " e " + str(maximo) + ": "))
    if escolha > numero:
        print ("Voce errou, seu numero foi maior")
    elif escolha < numero:
        print ("Voce errou, seu numero foi menor.")
    else :
        print ("voce acertou")
    vida -= 1
    if vida == 0 and escolha != numero:
        print ("Voce perdeu, suas tentativas acabaram")
