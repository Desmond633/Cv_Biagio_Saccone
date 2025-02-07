input_numeri = input("Inserisci una lista di numeri separati da spazio: ")  # Chiediamo all'utente di inserire i numeri separati da spazi

numeri = input_numeri.split() # Divide la stringa in una lista di numeri (stringhe)

for numero in numeri:  # Itera su ciascun numero della lista
    numero = int(numero)  # Converte la stringa in un numero intero
    print("Il quadrato di", numero, "è", numero ** 2)  # Stampa il quadrato del numero
