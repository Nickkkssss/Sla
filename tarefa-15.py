def status(andar, hp, bolsa):
    print(f"\n=== Andar {andar} | HP: {hp} | Bolsa: {bolsa} ===")

def missao():
    from random import randint
    bolsa = ["Soma", "Cartão Bufu", "Cartão Agi"]
    hp = 30
    andar = 1
    while andar <= 8 and hp > 0:
        status(andar, hp, bolsa)
        if randint(1, 2) == 1:
            dano = randint(5, 12)
            hp -= dano
            print(f"\nUma Sombra atacou! Você perdeu {dano} de HP.")
        else:
            decisão = int(input("\nSala do tesouro! 1- Entrar 2- Se curar "))
            if decisão == 1:
                itemAleatorio = randint(1, 3)
                if itemAleatorio == 1:
                    item = "Soma"
                elif itemAleatorio == 2:
                    item = "Cartão Bufu"
                else:
                    item = "Cartão Agi"
                bolsa.append(item)
                print(f"Você pegou: {item}")
            elif decisão == 2:
                if len(bolsa) > 0:
                    hp += 10
                    itemUsado = bolsa.pop()
                    print (f"\nVocê se curou com {itemUsado}")    
                else:
                    print ("\nVocê não tem itens para se curar")
            else:
                print ("\nEssa não é uma opção.")
        andar += 1
    if hp <= 0: 
        print("\nVocê desmaiou no Tartarus. (Final ruim)")
    elif len(bolsa) >= 4: 
        print(f"\nVocê alcançou o topo com {len(bolsa)} itens! (Final bom)")
    else: 
        print(f"\nVocê alcançou o topo, com apenas {len(bolsa)} itens. (Final médio)")
    print(f"\nA Hora Sombria acabou. Bolsa: {bolsa}")
    bolsa.clear()

missao()
