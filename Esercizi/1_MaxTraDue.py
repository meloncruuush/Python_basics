def max(a, b):
    if a == b:
        print("I due numeri sono uguali.")
    elif a > b:
        print(str(a) + " è maggiore di " + str(b))
    else:
        print(str(b) + " è maggiore di " + str(a))

max(int(input("Inserisci il primo numero: ")), int(input("\nInserisci il secondo numero: ")))