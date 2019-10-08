Getal = int(input("Geef een eindgetal in: "))
aantalGetallen = int(input("Geef het aantal weergegeven getallen in: "))
getal1 = 1 
rij= " "


for x in range(1, aantalGetallen+1):
	getal1 = x*Getal
	Getal = getal1
	rij = rij + str(getal1) + ","
print(rij[:-1])
