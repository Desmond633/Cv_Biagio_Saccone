# Chiedere all'utente di inserire un numero positivo
while True:  # Ciclo infinito per garantire l'inserimento di un numero valido
    n = int(input("Inserisci un numero intero positivo: "))  # Richiede un numero intero all'utente
    if n > 0:  # Controlla se il numero è positivo
        break  # Se il numero è valido, esce dal ciclo
    else:
        print("Errore: Il numero deve essere positivo.")  # Messaggio di errore se il numero non è positivo

# Menù interattivo
while True:  # Ciclo infinito per permettere all'utente di eseguire più operazioni finché non sceglie di uscire
    print("Menu")  # Stampa l'intestazione del menu
    print("1) Somma dei numeri pari da 1 a", n)  # Opzione per calcolare la somma dei numeri pari
    print("2) Stampa dei numeri dispari da 1 a", n )  # Opzione per stampare tutti i numeri dispari
    print("3) Verifica se",n,"è primo")  # Opzione per verificare se il numero è primo
    print("4) Esci")  # Opzione per uscire dal programma
    scelta = int(input("Scegli un'opzione (1-4): "))  # Richiede all'utente di selezionare un'opzione

    if scelta == 1:
        # Calcolare la somma dei numeri pari da 1 a n
        somma_pari = 0  # Inizializza la somma dei numeri pari a zero
        for i in range(2, n + 1, 2):  # Itera solo sui numeri pari tra 2 e n
            somma_pari += i  # Aggiunge il numero pari alla somma
        print("La somma dei numeri pari da 1 a è primo:", somma_pari)  # Stampa il risultato
    
    elif scelta == 2:
        # Stampare tutti i numeri dispari da 1 a n
        print("Numeri dispari da 1 a", n, ":")  # Intestazione della stampa dei numeri dispari
        for i in range(1, n + 1, 2):  # Itera solo sui numeri dispari tra 1 e n
            print(i, end=" ")  # Stampa i numeri dispari sulla stessa riga
        print()  # Manda a capo alla fine della stampa
    
    elif scelta == 3:
        # Determinare se n è un numero primo
        primo = True  # Inizializza la variabile che indica se n è primo
        if n < 2:  # Se n è minore di 2, non è un numero primo
            primo = False
        for i in range(2, int(n ** 0.5) + 1):  # Controlla i divisori fino alla radice quadrata di n
            if n % i == 0:  # Se trova un divisore, n non è primo
                primo = False
                break  # Interrompe il ciclo appena trova un divisore
        
        if primo:
            print(n, "è un numero primo.")  # Stampa se n è primo
        else:
            print(n, "non è un numero primo.")  # Stampa se n non è primo
    
    elif scelta == 4:
        print("Esci dal programma")  # Messaggio di uscita
        break  # Esce dal ciclo e termina il programma
    
    else:
        print("Scelta non valida. Riprova.")  # Messaggio di errore per input non valido