from random import randint
import os

b = -1
c = -1
p = 0
n = 9
a = 0
k = 0
l = 0
dil = 'd'
ero = 'e'
konec = 'q'
none = 'z'

def showfield(n, pole2):
    for n in range(3):
        for y in range(3):
            print(pole2[n][y], end = " ")
        print()

#pole2 = [[randint(1,10) for n in range(3)] for y in range(3)]

#print(pole2)
#showfield(n, pole2)
#print()
def dilatace(n, pole2, b, c):
        if b == -1 and c == -1:
            for n in range(3):
                for y in range(3):
                    pole2[n][y] += 1
                    if pole2[n][y] > 10:
                           pole2[n][y] = 10
                    print(pole2[n][y], end = " ")  
                print()
        else:
            pole2[b][c] += 1
            for n in range(3):
                for y in range(3):
                    if pole2[n][y] > 10:
                         pole2[n][y] = 10
                    print(pole2[n][y], end = " ")
                print()

#dilatace(n, pole2, b, c)

def eroze(n, pole2, b, c):
        if b == -1 and c == -1:
            for n in range(3):
                for y in range(3):
                    pole2[n][y] -= 1
                    if pole2[n][y] < 1:
                           pole2[n][y] = 1
                    print(pole2[n][y], end = " ")  
                print()
        else:
            pole2[b][c] -= 1
            for n in range(3):
                for y in range(3):
                    if pole2[n][y] < 1:
                           pole2[n][y] = 1
                    print(pole2[n][y], end = " ")
                print()

#eroze(n, pole2, b, c)
while True:
    print()
    pole2 = [[randint(1,10) for n in range(3)] for y in range(3)]
    showfield(n,pole2)
    print()
    print("d = dilatace, e = eroze, q = konec.")
    p = input()
    if p == konec:
        exit()
    print("x pokud žádný parametr napište z")
    k = input()
    print("y pokud žádný parametr napište z")
    l = input()
    if k == none:
         c == -1
    if l == none:
         b == -1
    k == c - 1
    l == b - 1
    if p == dil:
       dilatace(n, pole2, b, c)
    if p == ero:
        eroze(n, pole2, b, c)
