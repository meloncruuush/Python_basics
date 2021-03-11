# Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi,
# e che ti dica in output se l'elemento passato sia presente o meno nella lista. 
# Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.

def isSocio(persona, ListaSoci):
    if persona in ListaSoci:
        print(persona + " compare nella posizione " + ListaSoci.index(persona) + " della lista soci.")
    else:
        print(persona + " non fa parte della lista soci")