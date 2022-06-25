
import os
import sys
import random


#zad 3

liczba = 32.1234
dane = 342
n = 16
print(f"Liczba jest rowna {liczba}, dane wynosza {dane}, n wynosi {n}")
print(f"Liczba jest rowna {liczba:15f}, dane wynosza {dane:15d}, n wynosi {n:15d}")
print(f"Liczba jest rowna {liczba:015f}, dane wynosza {dane:015d}, n wynosi {n:015d}")
print(f"Liczba jest rowna {liczba:030.25f}")
print(f"{n} szesnastkowo to {n:x}")
print(f"{n} osemkowo to {n:o}")


#zad 4

litery = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print("Alfabet w porzadku naturalnym:")
for c, v in enumerate(litery):
    e = '\n' if (c+1) % 5 == 0 else ''
    print(f"{v.upper()} => {v} ", end=e)
print("\nAlfabet w porzadku odwroconym:")
for c, v in enumerate(litery[::-1]):
    e = '\n' if (c+1) % 5 == 0 else ''
    print(f"{v.upper()} => {v} ", end=e)

#zad 5

try:
    sekundy = int(input("Podaj liczbe sekund: "))
except:
    print("Podano bledne dane!")
else:
    m, s = divmod(sekundy, 60)
    h, m = divmod(m, 60)
    print(f"Czas: {h:02d}:{m:02d}:{s:02d}")

#zad 6

pMax = 21
for i in range(0, pMax + 1):
    print(f"2 do potegi {i:_<3} = {2**i:>10}")

#zad 7

print(f"Liczba argumentow: {len(sys.argv)}")
for c,v in enumerate(sys.argv):
    print(f"Argument {c}: {v}")


#zad 8

plik = input("Podaj sciezke do pierwszego pliku: ")
try:
    czyt = open(plik, "r")
    liczba = len(czyt.readlines())
    czyt.close()
    plik = input("Podaj sciezke do drugiego pliku: ")
    pisz = open(plik, "w")
    pisz.write(str(liczba))
    pisz.close()
except FileNotFoundError:
    print("Nie znaleziono pliku!")

#zad 9


m = [chr(i) for i in range(ord('a'), ord('z') + 1)]
w = [i.upper() for i in m]
s = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+']
try:
    while True:
        dlugosc = int(input("Podaj dlugosc hasla: "))
        if dlugosc <= 0:
            print("Dlugosc musi byc wieksza od 0!")
        else:
            break
    r = dlugosc
    while True:
        wielkie = int(input("Ile wielkich liter: "))
        if wielkie < 0 or wielkie > dlugosc:
            print("Liczba nie moze byc ujemna, ani wieksza od dlugosci!")
        else:
            break
    r -= wielkie
    print(f"Pozostalo znakow: {r}")
    while True:
        male = int(input("Ile malych liter: "))
        if male < 0 or male > r:
            print("Liczba nie moze byc ujemna, ani wieksza od liczby dostepnych znakow!")
        else:
            break
    r -= male
    print(f"Pozostalo znakow: {r}")
    while True:
        cyfry = int(input("Ile cyfr: "))
        if cyfry < 0 or cyfry > r:
            print("Liczba nie moze byc ujemna, ani wieksza od liczby dostepnych znakow!")
        else:
            break
    r -= cyfry
    print(f"Pozostalo znakow: {r}")
    while True:
        specjalne = int(input("Ile znakow specjlanych: "))
        if specjalne < 0 or specjalne > r:
            print("Liczba nie moze byc ujemna, ani wieksza od liczby dostepnych znakow!")
        else:
            break
    r -= specjalne
    print(f"Pozostalo znakow: {r}")
    if r > 0:
        print(f"Niewykorzystane znaki ({r}) zostana uzupelnione malymi literami")
        male += r

    print(f'''Podsumowanie:
    Dlugosc hasla: {dlugosc}
    Ilosc malych liter: {male}
    Ilosc wielkich liter: {wielkie}
    Ilosc cyfr: {cyfry}
    Ilosc znakow specjalnych {specjalne}''')
    ile = int(input("Ile hasel wygenerowac? "))
    plik = input("Podaj nazwe pliku: ")
    f = open(plik, "w")
    for _ in range(ile):
        haslo = []
        gen = []
        for i in range(male):
            gen.append('m')
        for i in range(wielkie):
            gen.append('w')
        for i in range(cyfry):
            gen.append('c')
        for i in range(specjalne):
            gen.append('s')

        for x in range(dlugosc):
            indeks = random.randint(0, len(gen)-1)
            znak = gen.pop(indeks)
            if znak == 'm':
                indeks = random.randint(0, len(m)-1)
                haslo.append(m[indeks])
            elif znak == 'w':
                indeks = random.randint(0, len(w)-1)
                haslo.append(w[indeks])
            elif znak == 'c':
                cyfra = random.randint(0, 9)
                haslo.append(cyfra)
            elif znak == 's':
                indeks = random.randint(0, len(s)-1)
                haslo.append(s[indeks])

        for c in haslo:
            f.write(str(c))
        f.write('\n')

    f.close()

except ValueError:
    print("Wprowadzono bledne dane!")
except FileNotFoundError:
    print("Nie znaleziono pliku!")