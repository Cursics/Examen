# mijnReeks = (0,3),(1,3),(2,6),(3,9),(4,12)
#reeks 1 = 0,1,2,3,4
#reeks 2 = 3,3,6,9,12

eindGetal = int(input("Geef een eindGetal: "))
array = []
Teller = 3
afdruk = ""

print("Resultaat: ")
for x in range(0,eindGetal):
	if(x < 1):
		geTal = Teller + x
	else:
		geTal = x*Teller
	eindresult = "(" + str(x) + "," + str(geTal) + ")" + ","
	afdruk = afdruk + eindresult
print(afdruk[:-1])