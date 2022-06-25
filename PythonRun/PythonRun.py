

def oblicz(x):
    if x == 10: return x
    return 1 + oblicz(x + 1)

print(oblicz(3))


liczby = [(7,9), (5,8), (2,6), (1,4), (0,3)]
liczby.sort()
print(liczby[3][1], liczby[2][0])

a= 'pythonmaster'
print('%.6s' % a)

b = 'hujzlamany'
print('%.3s' % b)

litery = ['p','a','w','e','l']
litery[2] = 'v'
print(litery[-3])

print ("CZESC".format(0,1))
print ("CZESC"[0])




