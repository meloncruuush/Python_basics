#Scrivi una funzione che, a scelta dell'utente, calcoli l'area di: un cerchio, un quadrato, un rettangolo, un triangolo 

def calcolaArea():
    switch = {
        1: areaCerchio,
        2: areaQuadrato,
        3: areaRettangolo,
        4: areaTriangolo
    }

    x = int( input("Quale area vuoi calcolare?\n1)Cerchio\n2)Quadrato\n3)Rettangolo\n4)Triangolo\nInserisci: ") )
    
    funzione = switch.get(x, "Input non valido")
    print(funzione())

def areaCerchio():
    print("area cercio")

def areaQuadrato():
    print("quadra")

def areaRettangolo():
    print("rett")

def areaTriangolo():
    print("tri")

calcolaArea()