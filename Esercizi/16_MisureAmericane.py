# Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print 
# l'equivalente in miglia terrestri, iarde, piedi e pollici.

def conversione_americana(m):
    miglia = m/0.000621371
    iarde = m*1.09361
    piedi = m*3,28084
    pollici = m*39,2701
    print(str(m) + "metri equivalgono a " + str(miglia) + " miglia, " + str(iarde) + " iarde, " + str(piedi) + " piedi, " + str(pollici), " pollici.")



conversione_americana(1)