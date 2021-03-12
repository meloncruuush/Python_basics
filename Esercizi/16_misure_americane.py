# Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print 
# l'equivalente in miglia terrestri, iarde, piedi e pollici.


def conversione_americana(metri):
    valori_convertiti = {
        "miglia": metri * 0.000621371,
        "iarde": metri * 1.09361,
        "piedi": metri * 3.28084,
        "pollici": metri * 39.2701}

    print(f"{metri} metri corrispondono a:")
    for key, value in valori_convertiti.items():
        print(f"{key}: {value}")


conversione_americana(10)
