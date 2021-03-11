#Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.

def moltiplicatrice(lista):
    totale = 0
    for n in lista:
        if n != 0:
           totale *= n
    
    print("Il prodotto di tutti i numeri della lista è " +str(totale))