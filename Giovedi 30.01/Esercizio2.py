# Definiamo tre funzioni per calcolare l'area di triangoli, quadrati e rettangoli

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato * lato

def area_rettangolo(base, altezza):
    return base * altezza

# Definiamo la funzione principale che gestisce il menu e le interazioni con l'utente
def calcolo_area():
    while True:  # Ciclo infinito per far ripetere il menu fino a quando l'utente sceglie di uscire
        print("Benvenuto! Scegli la forma geometrica per calcolare l'area:")
        print("1. Triangolo")
        print("2. Quadrato")
        print("3. Rettangolo")
        print("4. Esci")

        # L'utente inserisce un numero per selezionare un'opzione
        scelta = int(input("Cosa scegli? (1-4): "))

        if scelta == 1:
            base = float(input("Inserisci la base del triangolo: "))
            altezza = float(input("Inserisci l'altezza del triangolo: "))
            area = area_triangolo(base, altezza)
            print("L'area del triangolo è:", area)
        
        elif scelta == 2:
            lato = float(input("Inserisci il lato del quadrato: "))
            area = area_quadrato(lato)
            print("L'area del quadrato è:", area)

        elif scelta == 3:
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            area = area_rettangolo(base, altezza)
            print("L'area del rettangolo è:", area)

        elif scelta == 4: 
            print("Hai scelto di uscire")
            break  # Il comando break interrompe il ciclo while e termina la funzione

        else:
            print("Errore: devi inserire un numero tra 1 e 4. Riprova!")

# Chiamata della funzione per avviare il programma
calcolo_area()
