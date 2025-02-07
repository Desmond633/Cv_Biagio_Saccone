# Chiedi all'utente di inserire il primo numero
numero1 = float(input("Inserisci il primo numero: "))  # Input per il primo numero (convertito in decimale)

# Chiedi all'utente di inserire il secondo numero
numero2 = float(input("Inserisci il secondo numero: "))  # Input per il secondo numero (convertito in decimale)

# Chiedi all'utente di scegliere un'operazione
operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")  # L'utente inserisce il simbolo dell'operazione

# Controlla quale operazione è stata scelta
if operazione == "+":  # Se l'utente ha scelto l'addizione
    risultato = numero1 + numero2  # Esegui l'addizione
    print("Risultato:", risultato)  # Stampa il risultato

elif operazione == "-":  # Se l'utente ha scelto la sottrazione
    risultato = numero1 - numero2  # Esegui la sottrazione
    print("Risultato:", risultato)  # Stampa il risultato

elif operazione == "*":  # Se l'utente ha scelto la moltiplicazione
    risultato = numero1 * numero2  # Esegui la moltiplicazione
    print("Risultato:", risultato)  # Stampa il risultato

elif operazione == "/":  # Se l'utente ha scelto la divisione
    if numero2 == 0:  # Controlla se il secondo numero è 0
        print("Errore: Divisione per zero")  # Stampa un messaggio di errore
    else:  # Se il secondo numero NON è 0
        risultato = numero1 / numero2  # Esegui la divisione
        print("Risultato:", risultato)  # Stampa il risultato

else:  # Se l'utente ha inserito un'operazione non valida
    print("Operazione non valida")  # Stampa un messaggio di errore