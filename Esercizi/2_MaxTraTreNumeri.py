#Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

def maxDeiTre(x, y, z):
    numbers = [x, y, z]
    return max(numbers)

x = int(input("Inserisci il primo numero: "))
y = int(input("Inserisci il secondo numero: "))
z = int(input("Inserisci il terzo numero: "))

print("Il massimo tra i tre numeri e': ", maxDeiTre(x, y, z))