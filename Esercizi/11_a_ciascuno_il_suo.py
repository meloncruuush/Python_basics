# Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una
# lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def lunghezza_parole(lista_parole):
    lista_interi = []
    for word in lista_parole:
        lista_interi.append(len(word))
    
    print(lista_interi)
