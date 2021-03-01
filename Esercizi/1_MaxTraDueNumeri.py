#Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
#Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.

def massimo(x, y):
    if(x > y):
        return x
    else:
        return y 

x = int(input("Inserisci il primo valore: "))
y = int(input("Inserisci il secondo valore: "))

print("Il valore massimo tra i due e' ", massimo(x, y))