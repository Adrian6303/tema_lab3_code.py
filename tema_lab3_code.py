

def cmmdc(a,b): #functie cmmdc
    if a<1 or b<1:
        return 0
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def prim(x):    #functie prim
    ok=1
    if x < 2:
        ok = 0
    for i in range(2, x):
        if x % i == 0:
            ok = 0
    return ok
def semn(x):
    if x<0:
        return 1
    return 0

import sys
from os import system


def display_menu(menu): #afisarea meniului
    for k, function in menu.items():
        print(k, function.__name__)
lista = []  #declarare lista goala global
def citire_lista(): #functie citire lista
    print("Ai ales optiunea citire elemente lista")

    lista.clear()

    n = int(input("Introduceti numarul de elemente : "))

    for i in range(0, n):
        elem = int(input("Introduce numar : "))
        lista.append(elem)
    if lista ==[2,3,4]:
        assert gasire_secventa_nr_prime() ==[2]
    if lista ==[3,5,7]:
        assert gasire_secventa_nr_prime() == [3,5,7]
    if lista ==[2,4,6]:
        assert gasire_secventa_nr_prime() == [2]
    input("Pentru a continua apasa Enter\n")
    system('cls')

def gasire_secventa_nr_relativ_prime(): #functie pentru prima proprietate
    print("Ai ales optiunea gasire secventa de lungime maxima cu numere relstiv prime intre ele")

    l = []
    k = []
    j = 0
    max_l = []
    aux=-1
    for i in range(len(lista)-1):

        if cmmdc(lista[i],lista[i+1]) == 1:
            if lista[i] != aux:
                l.append(lista[i])
            l.append(lista[i+1])
            aux=lista[i+1]
        else:
            if len(l) > len(max_l):
                max_l = l
            l = []

    if len(l) > len(max_l):
        max_l = l
    if len(max_l) == 0:
        print("Nu exista o secventa de numere relativ prime intre ele.")
    else:
        print("Secventa de lungime maxima cu elementele relativ prime ",max_l)

    input("Pentru a continua apasa Enter\n")
    system('cls')



def gasire_secventa_nr_prime():  #functie pentru a doua proprietate
    print("Ai ales optiunea gasire secventa de lungime maxima cu numere prime")

    l = []
    k = []
    j = 0
    max_l = []
    for i in range(len(lista)):

        if prim(lista[i]) == 1:
            l.append(lista[i])
        else:
            if len(l) > len(max_l):
                max_l = l
            l = []

    if len(l) > len(max_l):
        max_l = l

    return max_l

    input("Pentru a continua apasa Enter\n")
    system('cls')

def proprietatea_10():
    print("Ai ales optiunea proprietatea 10")

    l = []
    k = []
    j = 0
    max_l = []
    aux1=-1
    aux2=-1
    for j in range(len(lista)-2):

        if semn(lista[j+1] - lista[j]) != semn(lista[j+2] - lista[j+1]):
            if lista[j] != aux1:
                l.append(lista[j])
            if lista[j+1] !=aux2:
                l.append(lista[j+1])
                aux1=lista[j+1]
            l.append(lista[j+2])
            aux2=lista[j+2]


        else:
            if len(l) > len(max_l):
                max_l = l
            l = []

    if len(l) > len(max_l):
        max_l = l
    if len(max_l) == 0:
        print("Nu exista o secventa de ce respecta proprietatea.")
    else:
        print("Secventa de lungime maxima ce respecta proprietatea ", max_l)

    input("Pentru a continua apasa Enter\n")
    system('cls')



def Iesire_din_aplicatie(): #functie terminare program
    system('cls')
    print("La revedere!")
    sys.exit()


def main():

    #creearea unui meniu dictionar unde cheia este un numar iar valoarea este numele fuctiei
    functions_names = [citire_lista,gasire_secventa_nr_relativ_prime,gasire_secventa_nr_prime,proprietatea_10, Iesire_din_aplicatie]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(input("Intrudu indicele actiunii corespunzatoare: "))  # Preia cheia actiunii
        selected_value = menu_items[selection]  # preia numele functiei
        selected_value()  # apeleaza functia


if __name__ == "__main__": #apelarea programului
    main()