#Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, 
#usando asterischi per disegnarlo.

def istogramma(lista):
    for i in lista:
        print("*"*i)