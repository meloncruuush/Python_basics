# Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione
# input, in secondi.


def converti_in_secondi():
    secondi = int(input("\nInserisci il numero di giorni da convertire: "))*24*3600 + \
              int(input("\nInserisci il numero di ore da convertire: "))*3600 + \
              int(input("\nInserisci il numero di minuti da convertire: "))*60

    return secondi


converti_in_secondi()
