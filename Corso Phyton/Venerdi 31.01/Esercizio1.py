utenti = []  # Crea una lista vuota chiamata 'utenti' che conterrà le informazioni di ciascun utente registrato

while True:  # Avvia un ciclo infinito (while True) che permetterà di registrare utenti finché non si decide di fermarsi
    print("Registrazione Account")  # Stampa una domanda per avvisare l'utente che sta per registrarsi
    username = input("Inserisci un username: ")  # Chiede all'utente di inserire il proprio username
    
    tentativi_password = 3  # Definisce una variabile che imposta il numero massimo di tentativi per inserire la password
    
    for i in range(tentativi_password):  # Avvia un ciclo che permette fino a 3 tentativi di inserire una password corretta
        password = input("Inserisci una password (min 6 caratteri, max 12 caratteri, almeno una lettera e un numero - Tentativo " + str(i+1) + " di " + str(tentativi_password) + "): ")  # Chiede all'utente di inserire una password. Viene mostrato anche il numero di tentativo corrente
        conferma_password = input("Conferma la password: ")  # Chiede all'utente di confermare la password appena inserita

        conta_caratteri = 0  # Variabile che tiene conto del numero di caratteri presenti nella password
        ha_numero = False  # Variabili che indicano se la password contiene almeno un numero
        ha_lettera = False  # Variabili che indicano se la password contiene almeno una lettera

        for char in password:  # Ciclo che attraversa ogni singolo carattere della password per verificare se soddisfa i requisiti
            conta_caratteri += 1  # Incrementa il contatore dei caratteri per ogni carattere che si incontra nella password
            if "0" <= char <= "9":  # Verifica se il carattere corrente è un numero
                ha_numero = True  # Se è un numero, imposta ha_numero a True
            if ("a" <= char <= "z") or ("A" <= char <= "Z"):  # Verifica se il carattere corrente è una lettera
                ha_lettera = True  # Se è una lettera, imposta ha_lettera a True

        if password == conferma_password:  # Verifica se la password e la conferma sono uguali
            if 6 <= conta_caratteri <= 12 and ha_lettera and ha_numero:  # Verifica se la password soddisfa tutti i requisiti (lunghezza tra 6 e 12, almeno una lettera, almeno un numero)
                utenti.append((username, password))  # Se la password è corretta, aggiunge il nome utente e la password alla lista 'utenti' come una tupla
                print("Registrazione completata con successo!")  # Stampa un messaggio di successo per informare l'utente che la registrazione è stata completata
                break  # Esce dal ciclo dei tentativi di password perché l'utente ha registrato con successo il proprio account
            else:
                print("La password non soddisfa i requisiti.")  # Se la password non soddisfa i requisiti, stampa un messaggio di errore
        else:
            print("Le password non coincidono.")  # Se la password e la conferma non coincidono, stampa un messaggio di errore

        if i == tentativi_password - 1:  # Se l'utente ha esaurito i tentativi, stampa un messaggio di errore
            print("Hai esaurito i tentativi di inserimento password.")  
            break  # Esce dal ciclo dei tentativi di password

    scelta = input("Vuoi registrare un altro account? (sì/no): ").strip().lower()  # Chiede se l'utente desidera registrare un altro account. La risposta deve essere "sì" o "no"
    if scelta == "no":  # Se la risposta è "no", esce dal ciclo infinito
        break  

def stampa_utenti(*utenti):  # Definisce una funzione che stampa tutti gli utenti registrati, utilizzando lo splat per passare una lista di tuple
    print("Utenti registrati:")  # Stampa un'intestazione per la lista degli utenti registrati
    for user, pwd in utenti:  # Cicla attraverso ogni tupla di dati (username, password) nella lista 'utenti'
        password_oculta = ""  # Inizializza una variabile vuota per memorizzare la password nascosta (asterischi)
        for _ in pwd:  # Cicla attraverso ogni carattere della password per nasconderla con asterischi
            password_oculta += "*"  # Aggiunge un asterisco alla password nascosta per ogni carattere della password originale
        print("Username: " + user + ", Password: " + password_oculta)  # Stampa lo username e la password nascosta, dove la password viene mostrata solo come asterischi

stampa_utenti(*utenti)  # Passa tutti gli utenti registrati (tutti gli elementi della lista 'utenti') come argomenti alla funzione 'stampa_utenti