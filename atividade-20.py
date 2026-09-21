import random
piratas = random.randint(0, 5)
tesouros = []
encontros = [ "Marinha", "Kraken", "Naufragos", "Sereias", "Piratas", "Barco cargueiro", "Barco cargueiro", "Barco cargueiro"]

while piratas >= 0 and len(tesouros) < 10:
    print (f"Você tem {piratas} piratas em sua tripulação e tem {len(tesouros)} tesouros: {tesouros}")
    encontro = random.randint(0, 7)
    print (f"Você achou {encontros[encontro]} no mar!")
    if encontro == 0:
        piratasPerdidos = random.randint(0, 2)
        piratas -= piratasPerdidos
        print (f"\nVocê encontrou a marinha enquanto explorava e infelizmente perdeu {piratasPerdidos} piratas")
    elif encontro == 1:
        tesouros.clear()
        piratasPerdidos = random.randint(3, 5)
        piratas -= piratasPerdidos
        print (f"\nVocê encontrou um Kraken, perdeu todos os seus tesouros e perdeu {piratasPerdidos} piratas!")
    elif encontro == 2:
        piratasGanhos = random.randint(1, 5)
        piratas += piratasGanhos
        tesouros.append("Lindas Mulheres")
        print (f"\nVocê encontrou alguns Naufragos, recebeu o tesouro 'Lindas Mulheres' e ganhou {piratasGanhos} piratas!")
    elif encontro == 3:
        temLindasMulheres = False
        for tesouro in tesouros:
            if tesouro == "Lindas Mulheres":
                temLindasMulheres = True
        if temLindasMulheres == True:
            print ("\nVocê encontrou sereias, porém, como tem Lindas Mulheres, conseguiu escapar do encanto delas")
        else:
            piratas -= piratas/2
            print (f"\nVocê encontrou sereias e perdeu metade de seus homens ({piratas})")
    elif encontro == 4:
        resultadoLuta = random.randint(1, 4)
        if resultadoLuta == 1:
            piratasPerdidos = random.randint(0, 2)
            piratas -= piratasPerdidos
            print (f"\nVocê encontrou piratas, a luta foi acirrada e você decidiu fugir, perdendo {piratasPerdidos} piratas")
            if len(tesouros) > 0:
                posicaoTesouroPerdido = random.randint(0, len(tesouros) - 1)
                tesouroPerdido = tesouros.pop(posicaoTesouroPerdido)
                print (f"Durante a luta você perdeu esse tesouro: {tesouroPerdido}")
        elif resultadoLuta == 2:
            piratasPerdidos = random.randint(0, 5)
            piratas -= piratasPerdidos
            tesouros.clear()
            print (f"\nVocê encontrou piratas, tiveram uma luta complicada e você saiu perdendo")
            print (f"Você perdeu {piratasPerdidos} piratas e perdeu todos os tesouros")
        else:
            tesouros.append("Ouro de pirata")
            piratasGanhos = random.randint(0, 2)
            piratas += piratasGanhos
            print (f"\nVocê encontrou piratas, a luta foi facil e você saiu vitorioso")
            print (f"Alguns piratas inimigos sobreviveram e entraram para a sua tripulação, você ganhou {piratasGanhos} piratas")
            print ("Você achou o tesouro 'Ouro de pirata'")
    else:
        tesouros.append("Lindas Mulheres")
        tesouros.append("Ouro de comercio")
        tesouros.append("Suprimentos")
        piratasGanhos = random.randint(1, 5)
        piratas += piratasGanhos
        print (f"\nVocê achou um barco cargueiro, ganhou Lindas mulheres, Ouro de comercio, Suprimentos e além disso ganhou {piratasGanhos} piratas")
if piratas < 0:
    print ("\nVocê e toda a sua tripulação morreu, você perdeu o jogo")
else:
    print (f"\nVocê voltou para casa com {len(tesouros)} tesouros e muitas historias para contar")
    print (tesouros)
