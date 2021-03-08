#EXCEPTIONS

#Common exceptions:
#ImportError: an import fails;
#IndexError: a list is indexed with an out-of-range number;
#NameError: an unknown variable is used;
#SyntaxError: the code can't be parsed properly;
#TypeError: a function is called on a value of an inappropriate type;
#ValueError: a function is called on a value of the correct type, but with an inappropriate value.

try:
    #code
except Exception:
    #code

#there can be more then one except, and for each except, more than one type of exception
#an except statement will catch every type of statement if nothing is specified
#this code is always run after the execution of try statement, even after an exception
#with raise you can raise another exception

try:
    #code
except ZeroDivisionError:
    raise ValueError
except (ValueError, TypeError):
    #code
finally:
    #code

#if you call raise inside an empty except, it will raise the error type that occurred

try:
    #code
except:
    raise

#le assertion servono per controllare che nel programma vada tutto bene. 
#Testano una espressione e se il risultato è falso sollevano una eccezione.
#Gli AssertionError possono essere gestiti come le eccezioni in un try-except
#Se non vengono gestite, termineranno il programma

temp = -12
assert (temp >= 0) "Wow so cold"



#FILES
#Prima di poter leggere un file, dobbiamo aprirlo. Possiamo specificare
#La modalità utilizzando r per read, w per write (riscrivere il contenuto), 
# a per append (aggiungere contenuto). Aggiungendo la b al file lo apriremo in 
#modalità binaria
myfile = open("filename.txt", "r")

#per chiudere il file quando abbiamo smesso di utilizzarlo
myfile.close()

#READ
documento = open("nomedocumento.txt")
ContenutoDocumento = documento.read() #si usa per leggere il contenuto del file
print(documento.read(8)) #legge solo 8 bytes di dati
print(documento.read(8)) #legge i successivi 8 (puoi usare anche altri valori)
print(documento.read()) #non specificando, legge fino alla fine
print(documento.read()) #leggendo da un file finito, restituisce stringa vuota
documento.close()

file = open("filename.txt", "r")
print(file.readlines()) #restituisce una lista dove ogni linea è un elemento

#per iterare tra le linee possiamo anche usare il for
for line in file:
    print(line)

file.close()

#WRITE
#Possiamo scrivere solo stringhe, tutto il resto deve essere convertito in stringa
file = open("filename.txt", "w") #se il file non esiste verrà creato da w
                                 #aprendo un file in w mode se ne cancella il contenuto
bytewritten = file.write("This line has been written to the file") #writes the line and return the number of byte written
file.close()                                        

#GOOD PRACTICE
#always make sure that a file is closed, you can use try and finally
try:
    file = open("filename.txt")
    print(file.read())
finally:
    file.close()

#possiamo ottenere questo anche tramite il with. crea una variabile temporanea solitamente chiamata f
#accessibile solo dentro al blocco e prende il valore del with
#il file viene chiuso automaticamente anche se causa una eccezione 
#puoi usare with dentro al try except
with open("filename.txt") as f:
    print(f.read())