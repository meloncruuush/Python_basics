# Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

def massimo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print("Il numero maggiore è " + str(massimo(15, 333, 11)))
