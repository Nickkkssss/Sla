def parqueDeDiversao():
    from random import randint
    from time import sleep
    dinheiro = 0
    tempoEsperaRussa = 0
    tempoEsperaAlvo = 0
    filaRussa = []
    filaAlvo = []
    filaIngresso = 0
    premios = ["Brinquedo", "Broche", "Boné"]
    parqueAberto = True
    print ("\nVocê é atendente de um parque, escolha oq vai fazer\n")
    while parqueAberto == True:
        filaIngresso += randint(0, 2)
        print (f"\nVocê tem {dinheiro} reais!\n Pessoas na fila dos ingressos: {filaIngresso}")
        print (f"\nMONTANHA RUSSA: Tamanho da fila: {len(filaRussa)} / Tempo de espera: {tempoEsperaRussa}")
        print (f"TIRO AO ALVO: Tamanho da fila: {len(filaAlvo)} / Tempo de espera: {tempoEsperaAlvo}")
        escolha = int(input("\n1- Atender fila do ingresso \n2- Colocar pessoas na fila do Tiro ao Alvo " \
        "\n3- Colocar pessoas na fila da montanha Russa \n4- Abastecer o estoque dos premios \n5- Fechar o parque \nEscolha o número: "))
        sleep(1)
        if escolha == 1:
            if filaIngresso > 0:
                filaIngresso -= 1
                nome = input("\nQual o nome da pessoa que você atendeu? ")
                sleep(1)
                dinheiroCliente = randint(0, 20)
                print (f"\n{nome} tem {dinheiroCliente} reais!")
                sleep(1)
                brinquedoEscolhido = randint(0, 1)
                if brinquedoEscolhido == 0:
                    print (f"\n{nome} escolheu o Tiro ao alvo")
                    sleep(1)
                    if dinheiroCliente >= 5:
                        dinheiro += 5
                        print (f"\n{nome} conseguiu comprar o ingresso para o tiro ao alvo, e sobrou {dinheiroCliente - 5} reais")
                        sleep(1)
                        filaAlvo.append(nome)
                    else:
                        print(f"\n{nome} não tinha dinheiro suficiente para brincar no tiro ao alvo")
                        sleep(1)
                else:
                    print (f"\n{nome} escolheu a Montanha Russa")
                    sleep(1)
                    alturaCliente = randint(10, 90)
                    print (f"\n{nome} tem 1,{alturaCliente} de altura!")
                    sleep(1)
                    if alturaCliente >= 40 and dinheiroCliente >= 10:
                        filaRussa.append(nome)
                        dinheiro += 10
                        print (f"\n{nome} conseguiu comprar o ingresso para a montanha russa, e sobrou {dinheiroCliente - 10} reais")
                        sleep(1)
                    elif dinheiroCliente >= 5:
                        print("\nVocê ofereceu ao cliente para ele entrar no Tiro ao Alvo")
                        sleep(1)
                        quer = randint(0, 1)
                        if quer == 1:
                            print (f"\n{nome} aceitou entrar na fila do Tiro ao alvo")
                            sleep(1)
                            dinheiro += 5
                            filaAlvo.append(nome)
                            print (f"\n{nome} conseguiu comprar o ingresso para o tiro ao alvo, e sobrou {dinheiroCliente - 5} reais")
                            sleep(1)
                        if quer == 0:
                            print (f"\n{nome} recusou comprar o ingresso para o Tiro ao Alvo")
                            sleep(1)
                    else:
                        print (f"\n{nome} está sem o dinheiro suficiente para qualquer um dos brinquedos")
                        sleep(1)
            else:
                print ("\nNão tem ninguem na fila de Ingressos.")
        elif escolha == 2:
            if len(filaAlvo) > 0:
                if tempoEsperaAlvo == 0:
                    pessoaJogando = filaAlvo.pop(0)
                    print (f"\n{pessoaJogando} está jogando no tiro ao alvo!")
                    tempoEsperaAlvo += 5
                    sleep(1)
                else:
                    print (f"\nNão podemos colocar uma pessoa para jogar pois o tempo de espera está em {tempoEsperaAlvo} minutos!")
                    sleep(1)
            else:
                print ("\nNão podemos colocar alguem para jogar pois não tem nenhuma pessoa na fila")
                sleep(1)
        elif escolha == 3:
            if len(filaRussa) > 0:
                if tempoEsperaRussa == 0:
                    tempoEsperaRussa += 5
                    for pessoa in filaRussa:
                        filaRussa.pop()
                        print (f"\n{pessoa} está na montanha russa!")
                        sleep(1)
                    print ("\nA montanha russa começou a se mover!")
                    sleep(1)
                else:
                    print (f"\nNão podemos colocar alguem na montanha russa pois o tempo de espera está em {tempoEsperaRussa} minutos!")
                    sleep(1)
            else:
                print (f"\nNão podemos colocar alguem pra jogar pois não há ninguem na fila")
                sleep(1)
        elif escolha == 4:
            premioAdicionado = input("\nQual o nome do premio que você quer adicionar? ")
            posiçãoPremio = int(input(f"Em qual posição você quer colocar esse premio? (Coloque de 0 a {len(premios)}) "))
            if posiçãoPremio <= len(premios) and posiçãoPremio >= 0:
                premios.insert(posiçãoPremio, premioAdicionado)
                print (f"\nVocê colocou {premioAdicionado} na posição {posiçãoPremio}")
                sleep(1)
            else:
                print("\nEssa posição não existe, por isso foi adicionado no começo da fila")
                premios.insert(0, premioAdicionado)
                sleep(1)
        elif escolha == 5:
            if tempoEsperaRussa == 0 and tempoEsperaAlvo == 0:
                if len(filaRussa) > 0 or len(filaAlvo) > 0:
                    print (f"\nVocê deseja reembolsar as {len(filaAlvo)} pessoas que estão na fila do Alvo e as {len(filaRussa)} pessoas que estão na fila da Montanha Russa? ")
                    decisao = input("\nDeseja fechar mesmo assim? (sim ou não) ")
                    if decisao == "sim": 
                        reembolsoAlvo = filaAlvo * 5
                        dinheiro -= reembolsoAlvo
                        reembolsoRussa = filaRussa * 10
                        dinheiro -= reembolsoRussa
                        print (f"\nVocê fechou o parque e reembolsou {reembolsoAlvo} para as pessoas na fila do Tiro ao Alvo e {reembolsoRussa} para as pessoas na fila da montanha russa")
                        sleep(1)
                        parqueDeDiversao = False
                    else:
                        print ("\nVocê pensou melhor e não fechou o parque!")
            else:
                print ("\nVocê não pode fechar o parque com pessoas brincando!")
        else:
            print ("\nEssa opção não é valida")
        print ("\n1 minuto se passou")
        if tempoEsperaAlvo > 0:
            tempoEsperaAlvo -= 1
            if tempoEsperaAlvo == 0:
                print (f"\n{pessoaJogando} acabou de jogar no tiro ao alvo!")
                sleep(1)
                acertouAlvo = randint(0, 1)
                if acertouAlvo == 1:
                    print (f"\n{pessoaJogando} venceu!")
                    sleep(1)
                    if len(premios) > 0:
                        indexPremioEscolhido = randint(0, len(premios) - 1)
                        premioEscolhido = premios[indexPremioEscolhido]
                        print (f"{pessoaJogando} pegou {premioEscolhido}!")
                        premios.pop(indexPremioEscolhido)
                        sleep(1)
                    else:
                        print ("\nVocê não tem premios, todos na filam ficam revoltados e pedem reembolso!")
                        sleep(1)
                        valorReembolsado -= len(filaAlvo) * 5
                        dinheiro -= valorReembolsado
                        print (f"\nVocê perdeu {valorReembolsado} ficando com {dinheiro}") 
                        filaAlvo.clear()
                        sleep(1)
        if tempoEsperaRussa > 0:
            tempoEsperaRussa -= 1
    print (f"\nEncerramos nosso espediente com {dinheiro} reais!")
parqueDeDiversao()
