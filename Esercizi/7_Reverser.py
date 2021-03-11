#Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) 
#della stessa stringa (ad esempio "abcd" diventerà "dcba")

def reverser(stringa):
    reverse = stringa[::-1] #il primo parametro è il valore da cui partire, il secondo quello a cui arrivare, il terzo ogni quanto saltare
                            #lasciando vuota la prima casella, significa "dall'inizio"
                            #lasciando vuota la seconda, significa "fino alla fine"
                            #infine un valore di salto negativo serve per andare nel senso oppposto
    print("La stringa inverita è " + reverse)