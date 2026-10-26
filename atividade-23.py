from random import randint
from time import sleep
print ("Você está em uma corrida de 3 caracois")
caracoisNome = ["Lenister", "Casemiro", "Osmar"]
apostado = int(input(f"\nEscolha em qual caracol você vai apostar (0 = Lenister, 1 = Casemiro ou 2 = Osmar)? "))
caracoisPosicao = [0, 0, 0]
posicaoVencedores = [0, 0, 0]
vencedor = -1
while vencedor == -1:
    for indice in range(len(caracoisNome)):
        andar = randint(-1, 3)
        caracoisPosicao[indice] += andar
        print (f"\nCaracol: {caracoisNome[indice]} / Posição:{caracoisPosicao[indice]}")
        sleep(1)
        if caracoisPosicao[indice] >= 10:
            vencedor = indice
            posicaoVencedores[indice] = caracoisPosicao[indice]

if posicaoVencedores[0] >= posicaoVencedores[1] and posicaoVencedores[0] >= posicaoVencedores[2]:
    vencedor = 0
elif posicaoVencedores[1] >= posicaoVencedores[0] and posicaoVencedores[1] >= posicaoVencedores[2]:
    vencedor = 1
elif posicaoVencedores[2] >= posicaoVencedores[0] and posicaoVencedores[2] >= posicaoVencedores[1]:
    vencedor = 2

if caracoisPosicao[0] == caracoisPosicao[1] == caracoisPosicao[2]:
    print ("\nEmpate total")
elif caracoisPosicao[apostado] == caracoisPosicao[vencedor]:
    print (f"\nSeu caracol {caracoisNome[apostado]} e {caracoisNome[vencedor]} empataram")
elif vencedor == apostado:
    print ("\nVocê ganhou!")
else:
    print ("\nVocê perdeu!")
    print (f"O vencedor foi: {caracoisNome[vencedor]}")
