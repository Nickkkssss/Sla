import random
viagem = []
print ("Aang, Katara, Sokka estão viajando pelo mundo, faça a rota de viagem deles")
while len(viagem) < 10:
    print ("\n1- Colocar um lugar novo na rota")
    print ("2- Ver a rota completa")
    print ("0- Encerrar a viagem")
    opcao = int(input("Qual você escolhe? "))
    if opcao == 1:
        novolocal = input("\nNome do novo lugar na rota: ")
        viagem.append(novolocal)
    elif opcao == 2:
        print (viagem)
    elif opcao == 0:
        break
    else:
        print("Essa opção não existe")
    evento = random.randint(1, 6)
    if evento == 1:
        if len(viagem) == 0:
            print ("\nO senhor do fogo encurralou vocês, o jogo acabou")
            break
        else:
            viagem.clear()
            print ("\nO senhor do fogo descobriu seu grupo! Vocês tiveram que se esconder e devido a isso perderam toda a rota de viagem")
    elif evento == 2:
        if len(viagem) == 0:
            print("\nNão há paradas para cancelar")
        else:
            lugarPerdido = viagem.pop()
            print(f"\nDevido a imprevistos o grupo teve que tirar a ultima parada prevista ({lugarPerdido})")
    elif evento == 3:
        posicao = random.randint(0, len(viagem) - 1)
        print(f"\nO planejamento mudou! Um novo lugar vai ocupar a posição {posicao} da rota.")
        novolugar = input("\nQual é o nome desse lugar? ")
        viagem.insert(posicao, novolugar)
    else:
        print ("\nVocês seguiram viagem normalmente")
print ("\nFim da viagem")
print (f"Rota final: {viagem}")
if len(viagem) > 9:
    print ("Vocês aproveitaram a viagem e derrotaram o senhor do fogo")
