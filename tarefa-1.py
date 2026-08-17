Geo = 0
listaGeo = []
Salas = int(input("Quantas salas você gostaria de explorar? " ))
for numero in range(Salas):
    GeoDaSala = int(input("Quantos geos você ganhou nessa sala? "))
    Geo += GeoDaSala
    listaGeo.append(GeoDaSala)
if Geo >= 500:
    print ("Você tem " + str(Geo) + " geos, você consegue consegue comprar um amuleto caro!")
elif Geo >= 100:
    print ("Você tem " + str(Geo) + " geos, você pode comprar algo simples na loja do Sly!")
else:
    print("Você tem " + str(Geo) + " geos, porém é muito pouco para comprar qualquer coisa.")
print (f"Essa foi a ordem que você coletou esses {listaGeo}")
