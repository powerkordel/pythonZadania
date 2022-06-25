
#zad 0

def napis(boolValue = True):
    end = ''
    if boolValue:
        end = '\n'
    print('Dzielenie przez zero', end=end)

napis(False)


def napis(newLine = True):
    if(newLine):
        print("Dzielenie przez zero \n")
    else:
        print("Dzielenie przez zero")

napis()

#zad 0a

def dziel_nat(liczba):
    if liczba == 0:
        return -1
    elif liczba < 0:
        return -2
    else:
        return 1/liczba

print(dziel_nat(0))
print(dziel_nat(-5))
print(dziel_nat(3))

#zad 0b

def checkIfHex(number):
    try:
        s = str(number)
        _ = int(s,16)
        return True
    except:
        return False

print(checkIfHex(4))
print(checkIfHex(0xF))
print(checkIfHex("9ASF"))
print(checkIfHex("FAB"))

#zad 0c

def zamien(a,b):
    return b, a

a = 3
b = 2
print(a,b)
a,b = zamien(a,b)
print(a,b)

#zad 0d

def szukaj(dane, wartosc):
    indeksy = []
    i = 0
    for dana in dane:
        if(dana == wartosc):
            indeksy.append(i)
        i += 1
    return indeksy

tekst = 'Ciekawa sprawa, to szukanie'
indeksy = szukaj(tekst, 'a')
print(indeksy)

#zad 1

def convertKMtoMI(value):
    try:
        number = float(value)
        if number <= 0:
            raise ValueError
        return number * 1.61
    except:
        raise ValueError

def convertMItoKM(value):
    try:
        number = float(value)
        if number <= 0:
            raise ValueError
        return number / 1.61
    except:
        raise ValueError

print(convertKMtoMI(2))
print(convertMItoKM(1.61))

#zad 2

def convertToBinaryString(number):
    string = str()
    while(number != 0):
        string += str(number % 2)
        number >>= 1
    
    return string[::-1]

string = convertToBinaryString(11)
print(string)
print(int(string,2))

#zad 3

def countSetBits(number):
    setBits = 0
    while number != 0:
        setBits += number % 2
        number >>= 1
    return setBits

print(countSetBits(255))

#zad 4

def recNFib(n):
    numbers = [int] * n
    for i in range(0, n):
        numbers[i] = recFib(i+1)
    return numbers

def recFib(n):
    if n <= 2:
        return 1
    else:
        return recFib(n-1)+recFib(n-2)

def itFib(n):
    numbers = [int] * n
    p = 1
    pp = 1
    for i in range(n):
        if i < 2:
            numbers[i] = 1
        else:
            numbers[i] = pp + p
            pp = p
            p = numbers[i]
    return numbers

n = 15
print(recNFib(n))
print(itFib(n))

#zad 5

def factRec(n):
    if n <= 1:
        return 1
    else:
        return n*factRec(n-1)

def factIt(n):
    if n <= 0:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

n = 10
print(factRec(n))
print(factIt(n))

#zad 6

def nwdSub(a,b):
    it = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        it += 1
    return a, it

def nwdDiv(a,b):
    it = 0
    while True:
        it += 1
        c = a % b
        a = b
        b = c
        if b == 0:
            return a, it

a = 1989
b = 867
print(nwdSub(a,b)) # (51, 8)
print(nwdDiv(a,b)) # (51, 4)


#zad 7

def encrypt(input):
    encrypted = str()
    x = 2
    for c in input:
        if c >= 'a' and c <= 'z':
            n = ((ord(c) - ord('a')) + x ) % 26
            encrypted += chr(n + ord('a'))
        elif c >= 'A' and c<= 'Z':
            n = ((ord(c) - ord('A')) + x ) % 26
            encrypted += chr(n + ord('A'))
        else:
            encrypted += c
    return encrypted

tekst = 'Moja wiadomosc do zaszyfrowania'
print(encrypt(tekst))


#zad 7

import string
def cezar(word, n):
    alfLower = string.ascii_lowercase.lower()
    alfUpper = string.ascii_lowercase.upper()
    result = ""
    for char in word:
        if char in alfLower:
            result += alfLower[(alfLower.index(char) + n) % len(alfLower)]
        elif char in alfUpper:
            result += alfUpper[(alfUpper.index(char) + n) % len(alfUpper)]
        else:
            result += char
    return result

print(cezar("CymbaliSta", 3))

#zad 8

def ile_cyfr(x):
    return len(list(str(x)))

print(ile_cyfr(1234567890))

#zad 8

def ile_cyfr(x):
    if type(x) is int or type(x) is float:
        n = 1
        while x % 10 == 0:
            x /= 10
            n += 1
        return n
    return 0

print(ile_cyfr(2))
print(ile_cyfr(10))
print(ile_cyfr(10000))
print(ile_cyfr("23"))

#zad 9

def isPrime(n):
    if n <= 1:
        return False
    k = n // 2
    for i in range(2, k+1):
        if n % i == 0:
            return False
    return True

for i in range(100):
    if(isPrime(i)):
        print(i)

#zad 10

def policz(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    elif type(a) is str and type(b) is int:
        return a*b
    elif type(a) is float and type(b) is float:
        return a+b
    else:
        return None

print(policz(1,2))
print(policz("tekst",3))
print(policz(2.4,3.12))
print(policz(1,1.0))