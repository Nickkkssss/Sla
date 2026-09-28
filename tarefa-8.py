import random
bisoes = []
while True:
    print ("\nVocê está no templo do ar do Sul, escolha uma opção:")
    print ("1- Achar um bisão voador")
    print ("2- Ver a lista atual de bisões")
    print ("0- Sair do jogo")
    escolha = input("Qual opção você escolhe? ")
    if escolha == "1":
        chanceEncontrar = random.randint(1, 5)
        if chanceEncontrar == 1 or chanceEncontrar == 2:
            print ("\nVocê não achou nenhum bisão")
        else:
            nome = input("\nVocê achou um bisão, qual o nome dele? ")
            posicao = int(input(f"Em que posição do rebanho ele deve entrar?(Escolha uma posição positiva menor que {len(bisoes) + 1}) "))
            while posicao > len(bisoes) or posicao < 0:
                print("Posicao invalida")
                posicao = int(input(f"Em que posição do rebanho ele deve entrar?(Escolha uma posição positiva menor que {len(bisoes) + 1}) "))
            print(f"{nome} se juntou ao rebanho na posição {posicao}")
        evento = random.randint(1, 6)
        if evento == 1:
            if len(bisoes)  == 0:
                print("Uma tempestade aconteceu, porém você não tinha bisões para perder")
            else:
                print ("\nUma tempestade aconteceu enquanto você esteve fora, todos os seus bisões foram embora!")
                bisoes.clear()
        elif evento == 2 or evento == 3:
            if len(bisoes) == 0:
                print ("Ladrões vieram, porém você não tinha bisões para eles roubarem")
            else:    
                print ("\nEnquanto você esteve fora, ladrões apareceram e roubaram o ultimo bisão da manada")
                bisoes.pop()
        else:
            print("\nEnquanto você esteve fora nada aconteceu")
        if chanceEncontrar > 2:
            bisoes.insert(posicao, nome)
        chanceEncontrar = 0
    elif escolha == "2":
        if len(bisoes) == 0:
            print ("\nVoce ainda não tem bisoes")
        else:
            print("\nRebanho atual:")
            for nome in bisoes:
                print(f"-{nome}")
    elif escolha == "0":
        print("\nVocê parou de coletar bisões, esse foi seu rebanho final: ")
        if len(bisoes) == 0:
            print ("Você não tinha nenhum bisão")
        else:
            for nome in bisoes:
                print(f"-{nome}")
        break
    else:
        print ("Opção invalida")
