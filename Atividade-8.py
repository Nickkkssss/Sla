nota1 = input ("Escreva sua nota na primeira materia: ")
nota2 = input ("Escreva sua nota na segunda materia: ")
nota3 = input ("Escreva sua nota na terceira materia: ")
media = (int(nota1) + int(nota2) + int(nota3)) / 3
if media < 5 :
    print ("voce reprovou com media " + str(media))
elif media == 10 :
    print ("voce passou com a nota perfeita" + str(media))
else :
    print ("voce foi aprovado com a nota " + str(media))
