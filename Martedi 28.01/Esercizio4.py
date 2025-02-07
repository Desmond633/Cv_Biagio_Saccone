# Inizializziamo il contatore per i numeri pari trovati
pari_count = 0
pari = []  # Lista per salvare i numeri pari

# Ciclo per chiedere numeri all'utente finché non sono stati trovati 5 numeri pari
while pari_count < 5:
    # Chiediamo all'utente di inserire un numero
    number = int(input("Inserisci un numero: "))
    
    # Verifica se il numero è pari
    if number % 2 == 0:  # Se il numero è divisibile per 2
        pari.append(number)  # Aggiungi il numero alla lista dei numeri pari
        pari_count += 1  # Incrementa il contatore dei numeri pari trovati
        print("Il numero è pari")
    else:
        print("Il numero non è pari")

# Dopo aver trovato 5 numeri pari, stampiamo la lista
print("I 5 numeri pari che hai inserito sono:", pari)