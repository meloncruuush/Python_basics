#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una 
#lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def lunghezzaParole(ListaParole):
    ListaInteri = []
    for word in ListaParole:
        ListaInteri.append(len(word))
    
    print(ListaInteri)