#1
while True:
    side1 = float(input("Sisestage ruudu esimene külg: "))
    side2 = float(input("Sisenege ruudu teisele küljele: "))
    if side1 == side2:
        square_area = side1 * side2
        print("Väljaku pindala on: ", square_area)
        break
    else:
        print("Ruudu mõlemad küljed peaksid olema võrdsed. Palun sisestage uuesti.")

while True:
    sides = input("Sisestage ruudu kaks külge, eraldades need tühikuga:").split()
    side1, side2 = map(float, sides)
    if side1 == side2:
        square_area = side1 * side2
        print("Väljaku pindala on: ", square_area)
        break
    else:
        print("Ruudu mõlemad küljed peaksid olema võrdsed. Palun sisestage uuesti.")

#2

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i*j:<5}", end=" ")
        j += 1
    print()
    i += 1


for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()

