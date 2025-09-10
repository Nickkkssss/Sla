alunos = ["nicolas", "Icaro", "Clarice", "João"]
print (str(alunos) + "você ira escolher um número e tentar achar um aluno")
respostas = input ("Escolha um número: " )

if respostas < "0":
    print ("Nao pode escolher um numero menor que 0")
elif respostas > "3":
    print ("O numero tem que ser igual ou menor que 3")
else:
    print ("O aluno foi " + alunos[int(respostas)])
