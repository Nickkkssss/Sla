vidaH = 10
vidaV = 10
Vraio = 1
Vcura = 1

for rodadas in range(4):
    if vidaH <= 0:
        print ("Voce perdeu, o monstro ganhou")
        break
    else:
        print ("Voce tem: " + str(vidaH) + " de vida. O monstro tem " + str(vidaV) + " de vida. Atacar da 3 de dano, Curar da 6 de vida e Raio da 6 de  dano")
        escolha = input ("Escolha uma ação: ")
        if escolha == "atacar":
            vidaV -= 3       
        elif escolha ==  "curar":
            Vcura -= 1
            vidaH += 6
        elif escolha == "raio":
            Vraio -= 1
            vidaV -=6
        else:
            print ("essa escolha não existe, escolha outra")
        
    if vidaV <= 0:
        print ("Voce ganhou do monstro")
        break
    else:
        vidaH -=5
