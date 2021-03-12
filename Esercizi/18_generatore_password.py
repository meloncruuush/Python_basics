# Scrivi una funzione generatrice di password.
# La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice,
# o di 20 caratteri ascii qualora desideri una password più complicata.


def genera_password_semplice():


def genera_password_complicata():


input_utente = int(input("\nVuoi una password da 8 o da 20 caratteri? "))
if input_utente == 8:
    genera_password_semplice()
elif input_utente == 20:
    genera_password_complicata()
else:
    print("Hai inserito un valore non valido")
