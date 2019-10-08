klinkers = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
rij = ""
    
zin = str(input("vul een zin of woord in: "))
for Letter in zin:
    if (Letter not in klinkers):
        rij = rij +  Letter
print(zin)
print(rij)