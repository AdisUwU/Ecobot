import random 
import time

JakieHaslo = int(input("Jak długie chcesz hasło?"))
IlCyf = int(input("Ile cyfr"))
IlLit = int(input("Ile liter"))
Cyfry = "1234567890"
Litery = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Haslo1 = []
Haslo2 = []
if IlCyf + IlLit == JakieHaslo:
    for i in range(IlCyf):
        Haslo1.append(Cyfry[random.randint(0,9)])

    for i in range(IlLit):
        Haslo2.append(Litery[random.randint(0,61)])
    Haslo = ''.join(Haslo1 + Haslo2)
    print(Haslo)
else:
    print("Liczby sie nie zgadzają spróbuj ponownie!")
