# Avvio del ciclo while che continua finché l'utente non decide di fermarsi
while True:
    # Chiediamo all'utente di inserire un numero
    numero = int(input("inserisci un numero: "))

    # Ciclo for che va dal numero inserito fino a 0, decrescendo di 1 ogni volta
    for pippo in range(numero, -1, -1):
        # Stampa ogni numero che appare durante il ciclo for
        print(pippo)

    # Chiediamo all'utente se vuole ripetere l'operazione
    ripetizione = input("vuoi ripetere? si/no ")
    
    # Se l'utente inserisce "no", il ciclo while si ferma
    if ripetizione == "no":
        break  # Esce dal ciclo while