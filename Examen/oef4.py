Letter = ord(input("Geef een hoofdletter in: "))
start = 65
for rij in range(start, Letter+1):
    for col in range(Letter-rij+1):
        print(chr(65 + col), end="")
    print()