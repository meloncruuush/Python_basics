#Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario
#rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.

def frequenziamento(stringa):
    dizionario = {}
    for carattere in stringa:
        if carattere in dizionario:
            dizionario[carattere] += 1
        else:
            dizionario[carattere] = 1

    return dizionario
