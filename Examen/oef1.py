import random

eindGetal = int(input("Geef een eindGetal: "))
aantalGetallen = int(input("hoeveel getallen dien ik te genereren: "))

Teller = 0 
reeks1 = []
Reeks2 = []
JaNEE = "ja"

while(JaNEE == "ja"):
	for x in range(0,aantalGetallen):
		reeks1.append(random.randint(0,eindGetal))
	Teller += 1	
	print(reeks1)
	Reeks2 = reeks1
	Reeks2.sort()
	print(Reeks2)
	JaNEE = input("wenst u het programma nogmaals uit te voeren? J/N: ")
	Reeks2.clear()



print("programma werd reeds", Teller ,"uitgevoerd.")