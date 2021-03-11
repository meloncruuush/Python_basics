#Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.

def sommatrice(lista):
    somma = 0
    for n in lista:
        somma += n

    print("Il risultato della somma è " + str(somma))