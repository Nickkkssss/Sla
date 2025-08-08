idade = float(input("idade: "))
pais = input("Autorizacao dos pais: ")
Vip = input("Vip: ")
ingresso = input("Ingresso: ")

if (idade >=18 and Vip == "True"):
    print ("Pode entrar como vip")
elif idade >= 18 and ingresso == "True" :
    print ("Pode entrar")
elif idade > 12 and pais and ingresso == "True"  :
   print  ("Pode entrar devido a autorizaçao de seus pais")
else: 
   print ("Não pode entrar")
