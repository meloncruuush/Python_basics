# Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.

def massimo(a, b):
    if a == b:
        print("I due numeri sono uguali.")
    elif a > b:
        print(str(a) + " è maggiore di " + str(b))
    else:
        print(str(b) + " è maggiore di " + str(a))


massimo(int(input("Inserisci il primo numero: ")), int(input("\nInserisci il secondo numero: ")))
