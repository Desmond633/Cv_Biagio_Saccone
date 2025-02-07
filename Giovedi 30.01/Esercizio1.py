# Funzione che calcola un numero casuale, basato su un calcolo matematico determinato
def calcola_numero_casuale():
    base = 7  # Un numero base fisso utilizzato per il calcolo (può essere modificato per cambiare il numero)
    
    # Eseguiamo un calcolo matematico per ottenere un numero casuale tra 1 e 100
    # In questo caso, moltiplichiamo il numero base (7) per 11, aggiungiamo 3 e facciamo il modulo 100
    # L'operazione modulo 100 assicura che il numero risultante sia sempre compreso tra 0 e 99
    numero = (base * 11 + 3) % 100  # Numero che dipende dai calcoli precedenti (in questo caso è 80)
    
    # La funzione restituisce il numero calcolato
    return numero


# Funzione principale che gestisce il gioco
def gioca():
    # Chiamata alla funzione calcola_numero_casuale per ottenere il numero segreto
    numero_segreto = calcola_numero_casuale()  # Numero che cambia ogni volta che il programma viene eseguito
    
    # Variabile che tiene traccia se l'utente ha indovinato il numero
    indovinato = False  # Inizialmente, l'utente non ha ancora indovinato

    # Messaggio di benvenuto che spiega il gioco all'utente
    print("Benvenuto nel gioco! Indovina il numero tra 1 e 100.")

    # Ciclo che continua a chiedere il tentativo finché l'utente non indovina il numero
    # Il ciclo continua fintanto che indovinato è False, ossia quando l'utente non ha indovinato
    while indovinato == False:
        # Chiediamo all'utente di inserire il proprio tentativo
        tentativo_utente = int(input("Inserisci il tuo tentativo: "))
        
        # Se il numero inserito dall'utente è inferiore al numero segreto
        if tentativo_utente < numero_segreto:
            # Avvisiamo l'utente che il numero da indovinare è maggiore
            print("Il numero è più alto!")
        
        # Se il numero inserito dall'utente è superiore al numero segreto
        elif tentativo_utente > numero_segreto:
            # Avvisiamo l'utente che il numero da indovinare è minore
            print("Il numero è più basso!")
        
        # Se l'utente ha inserito il numero corretto
        else:
            # Cambiamo il valore di indovinato a True, indicando che l'utente ha indovinato
            indovinato = True  
            
            # Messaggio di congratulazioni con il numero segreto
            print(f"Congratulazioni! Hai indovinato il numero {numero_segreto}.")


# Avvia il gioco
gioca()
