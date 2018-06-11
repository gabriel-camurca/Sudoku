#from os import system
#system("cls")
import os

with open("pls.txt") as f:
    
    s = f.readlines()
    s =[i.replace("\n","") for i in s]
    s =[i.replace(" ","") for i in s]
    s =[i.replace(",","") for i in s]
    s =[i.replace(":","") for i in s]

l1 = "++---+---+---++---+---+---++---+---+---++"
l2 = "++===+===+===++===+===+===++===+===+===++"
l3 = '    A   B   C    D   E   F    G   H   I  '
l4 = 'ABCDEFGHI'

f.close()
matriz = [[0 for i in range (9)] for j in range (9)]
x = len(s)
for i in range(x):
    a = s[i]
    a = str(a)
    i = l4.find(a[0])
    j = int(a[1])-1
    matriz[i][j] = int(a[2])

n = ''
j = 1
print(l3)
print("",l1)
for i in range(9):
    for j in matriz[i]:
        if matriz[0]:
            n += '|| {} |'
        elif matriz[1]:
            if int(i+1) % 3 == 0 and i != 8:
                print('',l2)
                j += 1
            else:
                print('',l1)
                j += 1

print(l3)

