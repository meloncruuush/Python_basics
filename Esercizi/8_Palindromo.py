#Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo 
#(parole che si leggono uguali anche al contrario) oppure meno.

def palindromo (word):
    word_reversed = word[::-1]
    if(word == word_reversed):
        print("Hai inserito una parola palindroma")
    else:
        print("La parola non è palindroma")