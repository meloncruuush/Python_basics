# Scrivi una funzione che, a scelta dell'utente, calcoli l'area di: un cerchio, un quadrato, un rettangolo, un triangolo

from math import pi


def calcola_area():
    switch = {
        1: area_cerchio,
        2: area_quadrato,
        3: area_rettangolo,
        4: area_triangolo
    }

    x = int(input("Quale area vuoi calcolare?\n1)Cerchio\n2)Quadrato\n3)Rettangolo\n4)Triangolo\n\nInserisci: "))
    
    funzione = switch.get(x, "Input non valido")
    funzione()


def area_cerchio():
    r = float(input("Inserisci il raggio: "))
    area = (r**2)*pi
    print(round(area, 3))


def area_quadrato():
    lato = float(input("Inserisci il lato del quadrato: "))
    area = lato**2
    print(round(area, 2))


def area_rettangolo():
    base, altezza = float(input("Inserisci la base: ")), float(input("Inserisci l'altezza: "))
    area = base*altezza
    print(round(area, 2))


def area_triangolo():
    base, altezza = float(input("Inserisci la base: ")), float(input("Inserisci l'altezza: "))
    area = base*altezza/2
    print(round(area, 2))


while True:
    calcola_area()
    scelta = int(input("\n\nVuoi continuare?\n1)Sì\n0)Esci\n"))
    if scelta == 0:
        break
