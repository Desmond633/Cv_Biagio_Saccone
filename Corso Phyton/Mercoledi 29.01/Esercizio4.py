input_numeri = input("Inserisci una lista di numeri separati da spazio: ")  # Chiedi all'utente di inserire i numeri separati da spazio
numeri = input_numeri.split()  # Dividi l'input in una lista di stringhe

if numeri == []:  # Verifica se la lista è vuota senza usare len()
    print("La lista è vuota.")  # Se la lista è vuota, stampa questo messaggio
else:
    numeri = [int(num) for num in numeri]  # Converte la lista di stringhe in una lista di numeri interi

    max_num = numeri[0]  # Inizializza max_num con il primo numero della lista
    for numero in numeri:  # Ciclo per trovare il massimo
        if numero > max_num:
            max_num = numero  # Aggiorna il numero massimo

    count = 0  # Inizializza il contatore
    for _ in numeri:  # Ciclo per contare gli elementi della lista
        count += 1  # Aumenta il contatore per ogni numero nella lista

    print("Il numero massimo nella lista è:", max_num)  # Stampa il numero massimo
    print("Il numero di elementi nella lista è:", count)  # Stampa il numero di elementi
