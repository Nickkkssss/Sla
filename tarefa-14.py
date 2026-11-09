from random import randint
equipe = ["Joker", "Ryuji", "Ann", "Morgana"]
reservas = ["Yusuke", "Makoto", "Futaba", "Haru"]
def mostrar(equipe): print(f"\nEquipe: {equipe}")
def batalha(equipe):
    lutador = equipe.pop(0)
    poderMembro = randint(1, 10)
    poderSombra = randint(1, 10)
    if poderMembro >= poderSombra:
        equipe.append(lutador)
        print(f"\n{lutador} ({poderMembro}) x Sombra ({poderSombra}): {lutador} venceu!")
    else:
        print(f"\n{lutador} ({poderMembro}) x Sombra ({poderSombra}): {lutador} foi ferido!")
for rodada in range(1, 6):
    if len(equipe) > 0:
        print(f"\n- Rodada {rodada} -")
        mostrar(equipe)
        batalha(equipe)
        if len(equipe) == 3:
            valido = False
            while valido == False:
                print (f"\n{reservas}")
                escolha = input("\nQuem entra como reforço? ")
                if escolha == "fugir" or escolha in reservas:
                    valido = True
            if escolha == "fugir":
                equipe.clear()
                print("\nOs Phantom Thieves recuaram!")
            else:
                reservas.pop(reservas.index(escolha))
                equipe.insert(1, escolha)
if len(equipe) > 0:
    print("\nVocês roubaram o Tesouro!")
