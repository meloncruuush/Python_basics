#Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. 
#In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!

def lenght(x):
    lunghezza = 0
    for i in x:
        lunghezza += 1
    
    print(lunghezza)