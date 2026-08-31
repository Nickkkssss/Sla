import random
vidamaxima = 100
vida = vidamaxima
inventario = []
rodadas = 0
while vida > 0 and len(inventario) < 10:
    print (f"\nvida atual  {vida}")
    print ("Você está no abismo, seu objetivo é achar 10 talismãs, escolha alguma opção (Coloque o número):")
    print ("1- Explorar o abismo")
    print ("2- Ver o inventario")
    print ("3- Esvaziar o inventario (Fugir)")
    print ("4- Sair do jogo")
    escolha = input ("Qual opção você quer? ")
    rodadas += 1
    if escolha == "1":
        resultado = random.randint(1, 4)
        if resultado == 1:
            talisma = input("\nVocê encontrou um talisma, qual o nome dele? ")
            inventario.append(talisma)
            print (f"{talisma} foi adicionado ao seu inventario")
        elif resultado == 2:
            if vida == 100:
                print ("\nVocê achou cura, porém está com a vida cheia, não precisa curar.")
            elif vida > 84:
                vida = 100
                print ("\nVocê achou cura, sua vida foi pro maximo!")
            else:
                print ("\nVocê achou cura, curou 15 de vida!")
                vida += 15
        else:
            dano =  random.randint (5, 20)
            vida -= dano
            print(f"\nVocê achou um inimigo, ele te atacou. Você levou {dano} de dano")
        
    elif escolha == "2":
        if len(inventario) == 0:
            print("\nSeu inventario ta vazio")
        else:
            print (f"\nVocê possui {len(inventario)} talismãs!")
            for talisma in inventario:
                print (talisma)
    elif escolha == "3":
        if len(inventario) == 0:
            print ("\nSeu inventario já está vazio")
        else:
            confirmar = input("\nTem certeza que quer apagar todo o inventario? ")
            if confirmar == "sim":
                cura = len(inventario) * 15 
                if vida == 100:
                    print ("Sua vida está cheia, você perdeu seus talismas atoa ")
                elif vida + cura >= 100:
                    print ("Você restaurou sua vida até o maximo")
                    vida = 100
                else:
                    print (f"Você curou {cura} de vida  ")
                    vida += cura
                inventario.clear()
                print (f"Você fugiu, mas em troca recuperou {cura} de vida, porém perdeu todos os talismãs")
            else:
                print ("Você não fugiu")
    elif escolha == "4":
        print ("\nVocê decidiu sair do abismo, isso é um resumo de sua aventura: ")
        print (f"Talismas coletados: {len(inventario)}")
        print (f"Rodadas sobrevividas: {rodadas}")
        print (f"Vida final: {vida}")
        break
    else:
        print ("Opção invalida")
    if vida <= 0:
        if len(inventario) > 0:
            print ("\nVocê iria morrer, mas seus talismas lhe salvaram, em troca você perdeu todos eles!")
            inventario.clear()
            vida = 1
        else:
            print ("\nVocê morreu! Esse é o resumo de sua aventura:")
            print ("\nVocê decidiu sair do abismo, isso é um resumo de sua aventura: ")
            print (f"Talismas coletados: {len(inventario)}")
            print (f"Rodadas sobrevividas: {rodadas}")
            print (f"Vida final: {vida}")
    if len(inventario) == 10:
        print ("\nVocê venceu, conseguiu 10 talismas! Esse é um resumo da sua aventura:")
        print (f"Talismas coletados: {len(inventario)}")
        print (f"Rodadas sobrevividas: {rodadas}")
        print (f"Vida final: {vida}")
