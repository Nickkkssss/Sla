from random import randint
fila = ["Zuko", "Azula", "Ty Lee", "Mai", "Zhao"]
vidas = 3
vitorias = 0

while len(fila) > 0 and vidas > 0:
    sorteio = randint(1, 5)
    if sorteio == 1:
        fila.insert(0, "Soldado extra")
        print("\nA Nação do Fogo mandou um soldado extra!")

    adversario = fila.pop(0)
    print(f"\nAang vai lutar contra {adversario}!")
    golpe = int(input("Escolha um golpe (1, 2 ou 3): "))
    bloqueado = randint(1, 3)
    print (f"{adversario} escolheu {bloqueado}!")

    if golpe != bloqueado:
        print("\nAang venceu a luta!")
        vitorias += 1
    else:
        print("\nAang foi bloqueado e perdeu uma vida!")
        vidas -= 1
        vitorias = 0
        fila.append(adversario)

    if vitorias == 3:
        print("\nEstado Avatar! Todos os adversários fugiram!")
        fila.clear()

    print(f"\nVidas: {vidas} / Adversários na fila: {len(fila)} / Vitorias Seguidas: {vitorias}")

if vidas > 0:
    print("\nAang venceu o torneio!")
else:
    print("\nAang foi derrotado...")
