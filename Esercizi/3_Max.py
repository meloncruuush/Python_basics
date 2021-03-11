#Scrivi un programma che, passata come parametro una lista di interi, 
#fornisce in output il maggiore tra i numeri contenuti nella lista.

def max(a):
    massimo = 0
    for i in a:
        if i > massimo:
            massimo = i

    print("Il numero più grande della lista è " + str(massimo))



lista = [1, 5, 7, 9, 88, 3, 111, 5, 23]
max(lista)