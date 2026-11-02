from random import randint
vivos = ["Light", "Misa", "Soichiro", "Matsuda", "Mikami", "Takada", "Near", "Mello", "Mogi", "Higuchi"]
kira = vivos[randint(0, 9)]
grampo = []
acao = 0
dia = 1
kiraEncontrado = False
while dia <= 7:
    vitima = vivos[randint(0, len(vivos) - 1)]
    while vitima == kira:
        vitima = vivos[randint(0, len(vivos) - 1)]
    print(f"\nDia {dia}: {vitima} morreu!")
    if acao == 2:
        if vitima in grampo and kira not in grampo:
            print(f"O Kira é {kira}!")
        else:
            print("\nNenhum dos grampeados foi assassinado")
    vivos.pop(vivos.index(vitima))
    for i in range(len(vivos)):
        print(i + 1, vivos[i])
    acao = int(input("\n1-investigar \n2-grampear \n3-chutar\nEscolha sua ação: "))
    if acao == 1:
        suspeito = vivos[int(input("Número de quem investigar: ")) - 1]
        if suspeito == kira:
            print(f"{suspeito} tem o caderno! É o Kira!")
        else:
            print(f"{suspeito} não tem caderno... por enquanto.")
    elif acao == 2:
        grampo.clear()
        grampo.append(vivos[int(input("Número da 1ª pessoa: ")) - 1])
        grampo.append(vivos[int(input("Número da 2ª pessoa: ")) - 1])
    elif acao == 3:
        suspeito = vivos[int(input("Número de quem você acha que é o Kira: ")) - 1]
        print(f"\nVocê anuncia que {suspeito} é o Kira!")
        if suspeito == kira:
            print(f"Você acertou! {kira} era o Kira! L venceu!")
            kiraEncontrado = True
        else:
            print("Você errou! O verdadeiro Kira continua à solta.")
            dia += 7
    dia += 1
if dia > 7 and kiraEncontrado == False:
    print(f"Acabou o tempo! O Kira era {kira}. O Kira venceu...")
