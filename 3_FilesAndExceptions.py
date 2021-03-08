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

myfile = open("filename.txt")