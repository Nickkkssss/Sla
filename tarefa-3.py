import random
VidaJ = 5
VidaB = 5
ataques = ["Salto", "Impacto", "Investida"]
acontecerFuria = False
ataqueEscolhido = ""
while VidaJ > 0 and VidaB > 0:
    print (f"Vida Jogador: {VidaJ} | Vida Vilão: {VidaB}")
    if acontecerFuria:
        ataqueEscolhido = "Fúria"
        acontecerFuria = False
    else:
        numeroEscolhido = random.randint(0, 2)
        ataqueEscolhido = ataques[numeroEscolhido]
    print (f"O proximo ataque dele será {ataqueEscolhido}")
    if ataqueEscolhido == "Salto":
        print ("chance media em atacar e desviar")
        chanceAtaque = 5
        chanceEsquiva = 5
        danoInimigo = 2
    elif ataqueEscolhido == "Impacto":
        print ("chance ruim de atacar. Chance boa de desviar")
        chanceAtaque = 3
        chanceEsquiva = 7
        danoInimigo = 2
    elif ataqueEscolhido == "Investida":
        print ("Boa chance de atacar. Chance ruim de desviar")
        chanceAtaque = 7
        chanceEsquiva = 3
        danoInimigo = 1
    elif ataqueEscolhido == "Fúria":
        print ("não consegue atacar. Chance media de desvio")
        chanceAtaque = 0
        chanceEsquiva = 5
        danoInimigo = 2
    ação = input("Você vai Atacar(a) ou Esquivar(e)? ")
    if ação == "a":
        sorteio = random.randint(1, 10)
        print (f"Sua sorte foi {sorteio}")
        if sorteio <= chanceAtaque:
            print ("Você acertou o boss!")
            VidaB -= 1
            acontecerFuria = True
        else:
            print (f"Você errou o ataque, levou {danoInimigo} de dano!") 
            VidaJ -= danoInimigo
    elif ação == "e":
        sorteio = random.randint(1, 10)
        print (f"Sua sorte foi {sorteio}")
        if sorteio <= chanceEsquiva:
            print ("Você esquivou!")
        else:
            print(f"Você não conseguiu esquivar, levou {danoInimigo} de dano!")
            VidaJ -= danoInimigo
    else:
        print ("Invalido, tente novamente")
    print ("")
print ("Fim de jogo!")
if VidaJ <= 0:
    print("O vilão venceu!")
else:
    print ("Você venceu!")
