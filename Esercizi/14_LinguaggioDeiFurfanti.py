# In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", 
# che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. 
# Ad esempio la parola "mangiare" diventa "momanongogiarore".
# Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".
# Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra,
# e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.

def convertiInRovarspraket(parola):
    vocali = "aeiou"
    parolaFurfante = ""
    for carattere in parola:
        parolaFurfante += carattere
        if carattere not in vocali:
            parolaFurfante = parolaFurfante + "o" + carattere
    
    print(parolaFurfante)


continua = True
while continua:
    convertiInRovarspraket( input("Inserisci una parola da convertire nel linguaggio dei furfanti: ") )

    x = int(input("Vuoi inserire un'altra parola?\n0)Esci \n1)Continua\n"))
    if x == 0:
        continua = False