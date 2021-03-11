#Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print("Il numero maggiore è " + str(max(15,333,11)))