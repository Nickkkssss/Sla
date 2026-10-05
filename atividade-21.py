import random
pontos = 0
mochila = ["Tocha", "Escudo"]
for andar in range(1, 6):
    print (f"\n\nVocê está no andar {andar} | Esses são os itens na sua mochila: {mochila} | Você está com {pontos} pontos")
    encontro = random.randint(1, 5)
    if encontro == 1:
        roubar = input("\nVocê achou um gigante adormecido, quer roubar algo do quarto dele? ")
        if roubar == "sim":
            conseguirRoubar = random.randint(1, 3)
            if conseguirRoubar == 1:
                print("\nVocê não conseguiu roubar")
                pontos -= 3
            else:
                print("\nVocê conseguiu roubar")
                itemEscolhido = input("\nQual item você roubou? ")
                mochila.append(itemEscolhido)
                pontos += 10
        else:
            print ("\nVocê decidiu não roubar")
        acordar = random.randint(1, 5)
        if roubar == "sim":
            if acordar == 1 or acordar == 2:  
                print("\nO gigante acordou")
                pontos -= 5
                chanceFugir = random.randint(1, 4)
                if chanceFugir == 1:
                    print("\nVocê não conseguiu fugir")
                    pontos -= 10
                    if andar > 1:
                        andar -= 1
                        print ("\nVocê também voltou 1 andar")
                    else:
                        print("\nVocê saiu da masmorra e perdeu")
                        break
                else:
                    print("\nVocê conseguiu fugir para o proximo andar")
                    pontos += 3

            else:
                print ("\nO gigante não acordou")
                pontos += 2
        else:
            if acordar == 1:
                pontos -= 5
                print("\nO gigante acordou")
                chanceFugir = random.randint(1, 4)
                if chanceFugir == 1:
                    print("\nVocê não conseguiu fugir")
                    pontos -= 10
                    if andar > 1:
                        andar -= 1
                        print ("\nVocê também voltou 1 andar")
                    else:
                        print("\nVocê saiu da masmorra e perdeu")
                        break
                else:
                    print("\nVocê conseguiu fugir para o proximo andar")
                    pontos += 3
            else:
                print("\nO gigante não acordou")
                pontos += 2
    elif encontro == 2:
        print ("\nEsse andar não tem nenhum ser vivo")
        item = input("\nEscolha qualquer item para adiciona-lo na mochila: ")
        posicao = int(input("\nEm que posicao da mochila o item deve ficar? "))
        while posicao > len(mochila) or posicao < 0:
            pontos -= 1
            print(f"\nEsse número não faz sentido, você perdeu 1 ponto, ficando com {pontos}")
            posicao = int(input(f"\nEm que posicao da mochila o item deve ficar?(Número positivo menor que {len(mochila)}): "))
        mochila.insert(posicao, item)
        pontos += 2
    elif encontro == 3:
        print ("\nVocê sofreu o ataque de um goblin pelas costas")
        if len(mochila) > 0:
            itemPerdido = mochila.pop()
            print (f"\nVocê jogou seu último item no Goblin, perdendo o {itemPerdido}")
        else:
            pontos -= 10
            print ("\nVocê não tinha nada na mochila e levou dano do goblin")
    elif encontro == 4:
        print ("\nVocê está prestes a cair em uma armadilha, mas pode arremessar um item na alavanca para passar de andar")
        if len(mochila) > 0:
            posicao = int(input("Você quer sacrificar o item de qual posição? "))
            if posicao < 0 or posicao > len(mochila) - 1:
                print (f"\nNão existe um item nessa posição, você falhou, caiu na armadilha e perdeu pontos, ficando com {pontos}")
                pontos -= 10
            else:
                itemSacrificado = mochila.pop(posicao)
                print (f"\nVocê sacrificou o {itemSacrificado}, mas conseguiu fugir da armadilha")
                pontos += 20
        else:
            print ("\nVocê não tem item e levou dano da armadilha")
            pontos -= 10
    elif encontro == 5:
        print ("\nCaiu slime na sua mochila, faça uma decisão:")
        print ("1- Limpar a mochila, perdendo todos os itens, mas ganhando pontos")
        print ("2- Se queimar para salvar seus itens, mas perdendo muitos pontos")
        decisao = int(input("Qual você escolhe? "))
        if decisao == 1:
            pontos += 20
            mochila.clear()
            print ("\nVocê decide jogar todos os seus itens fora")
        elif decisao == 2:
            pontos -= 20
            print ("\nVocê decide se queimar levando muito dano, mas salva todos seus itens")
        else:
            print ("\nEssa opção não existe, como você não pensou rapido a mochila queima, fazendo você perder todos os itens")
            mochila.clear()
if pontos < 0:
    print ("Você foi derrotado pela masmorra, mais sorte da proxima vez")
    print (f"Total de pontos: {pontos}")
    print (f"Itens na mochila:")
    for item in mochila:
        print(f"- {item}")
else:
    print (f"Você finalizou a masmorra com {pontos} pontos")
    print ("Para cada item você vai receber 10 pontos")
    PontosMochila = len(mochila) * 10
    pontos += PontosMochila
    print (f"Total de pontos: {pontos}")
    print (f"Itens na mochila:")
    for item in mochila:
        print(f"- {item}")
    if pontos < 50:
        print ("Você fez uma boa expedição")
    else:
        print ("Você fez uma expedição lendaria")
