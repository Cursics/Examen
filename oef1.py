getallen = int(input("hoeveel getallen wil je ingeven?: "))
array = []
onGtl = ""
evGtl = ""
for x in range(1,getallen+1):
	geTal = int(input("Geef een getal in: "))
	if(geTal%2!=0):
		onGtl = onGtl + str(geTal)
	else:
		evGtl = evGtl + str(geTal)
	print(evGtl)