# In Python non esiste l'equivalente Java di switch, ma possiamo comunque crearcelo

def switch(mese):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    print(switcher.get(mese, "Mese non valido"))
