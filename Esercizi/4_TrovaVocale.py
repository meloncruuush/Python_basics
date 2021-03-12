# Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere
# è o meno una vocale.

def trova_vocale(a):
    vocali = "aeiou"

    if a in vocali:
        print("Il carattere è una vocale")
    else:
        print("Il carattere non è una vocale")


trova_vocale("a")
