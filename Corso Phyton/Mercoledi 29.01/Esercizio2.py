while True:  # Ciclo infinito
    n = int(input("Inserisci un numero intero positivo: "))  # Chiedi il numero all'utente
    
    if n >= 0:  # Verifica che il numero sia positivo o zero
        for i in range(n, -1, -1):  # Ciclo da n a 0, inclusi
            print(i)
    
    else:
        print("Per favore inserisci un numero positivo.")  # Se l'utente inserisce un numero negativo
    
    risposta = input("Vuoi inserire un altro numero? (si/no): ")  # Chiedi se l'utente vuole continuare

    if risposta != 'si':  # Se l'utente non risponde 'si', termina il ciclo
        print("Uscita dal programma.")
        TrueFalse = False  # Variabile per uscire dal ciclo
        while TrueFalse:  # Ciclo che non entra mai, quindi termina l'esecuzione
            TrueFalse = False  # Esce dal ciclo principale
