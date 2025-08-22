numero = 8
escolha = 10
while escolha != numero :
    escolha = float(input("escolha um numero entre 1 e 10: "))
    if escolha > numero:
        print ("Voce errou, seu numero foi maior")
    elif escolha < numero:
        print ("Voce errou, seu numero foi menor.")
    else :
        print ("voce acertou")
    
