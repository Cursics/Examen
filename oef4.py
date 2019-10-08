array = []
hoeveel = 5
deNamen = int(input("hoeveel namen wil je ingeven?: "))

for x in range(0,deNamen):
	namen = str(input("Geef een naam in: "))
	hoeveel = len(namen)
	if(hoeveel >5):
		array.append(namen)

print(array)