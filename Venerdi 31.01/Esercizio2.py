def decoratore_bordo(func):  # Decoratore per aggiungere un bordo decorativo
    def wrapper(*args, **kwargs):
        print("=" * 40)  # Stampa un bordo superiore
        func(*args, **kwargs)  # Esegui la funzione originale
        print("=" * 40)  # Stampa un bordo inferiore
    return wrapper

def decoratore_nascondi_password(func):  # Decoratore per nascondere la password
    def wrapper(*args, **kwargs):
        # Modifica la lista utenti nascondendo le password
        utenti = args[0]  # Prendi la lista di utenti passata come argomento
        utenti_modificati = []
        for user, pwd in utenti:
            # Nascondi la password con asterischi
            password_oculta = "*" * len(pwd)
            utenti_modificati.append((user, password_oculta))  # Salva l'utente con la password nascosta
        return func(utenti_modificati)  # Chiama la funzione originale con la lista modificata
    return wrapper

@decoratore_bordo  # Aggiungi il decoratore del bordo alla funzione di registrazione
def registrazione_utente():  # Funzione che gestisce la registrazione di un singolo utente
    username = input("Inserisci un username: ")  # Chiede all'utente di inserire il proprio username
    
    tentativi_password = 3  # Definisce una variabile che imposta il numero massimo di tentativi per inserire la password
    
    for i in range(tentativi_password):  # Avvia un ciclo che permette fino a 3 tentativi di inserire una password corretta
        password = input("Inserisci una password (min 6 caratteri, max 12 caratteri, almeno una lettera e un numero - Tentativo " + str(i+1) + " di " + str(tentativi_password) + "): ")  # Chiede la password
        conferma_password = input("Conferma la password: ")  # Chiede di confermare la password inserita

        conta_caratteri = 0  # Variabile che tiene conto dei caratteri della password
        ha_numero = False  # Variabile che indica se la password contiene almeno un numero
        ha_lettera = False  # Variabile che indica se la password contiene almeno una lettera

        for char in password:  # Ciclo per controllare la password
            conta_caratteri += 1  # Incrementa il contatore dei caratteri
            if "0" <= char <= "9":  # Se il carattere è un numero
                ha_numero = True  # La password contiene almeno un numero
            if ("a" <= char <= "z") or ("A" <= char <= "Z"):  # Se il carattere è una lettera
                ha_lettera = True  # La password contiene almeno una lettera

        if password == conferma_password:  # Verifica che la password e la conferma siano uguali
            if 6 <= conta_caratteri <= 12 and ha_lettera and ha_numero:  # Verifica i requisiti della password
                return (username, password)  # Ritorna la coppia username e password come una tupla
            else:
                print("La password non soddisfa i requisiti.")  # Messaggio di errore se la password non è valida
        else:
            print("Le password non coincidono.")  # Messaggio di errore se le password non coincidono

        if i == tentativi_password - 1:  # Se i tentativi sono esauriti
            print("Hai esaurito i tentativi di inserimento password.")  
            return None  # Se i tentativi sono esauriti, ritorna None

@decoratore_bordo  # Aggiungi il decoratore del bordo alla funzione di registrazione
def registra_utenti():  # Funzione che gestisce la registrazione di più utenti
    utenti = []  # Lista per memorizzare gli utenti registrati
    while True:  # Ciclo infinito per permettere la registrazione di più utenti
        print("Registrazione Account")  # Messaggio di benvenuto
        utente = registrazione_utente()  # Chiama la funzione per registrare un singolo utente
        if utente:  # Se l'utente è stato registrato con successo
            utenti.append(utente)  # Aggiungi l'utente alla lista
            print("Registrazione completata con successo!")
        else:
            print("Registrazione non completata.")  # Messaggio di errore se la registrazione fallisce

        scelta = input("Vuoi registrare un altro account? (sì/no): ").strip().lower()  # Chiede se si vuole registrare un altro utente
        if scelta == "no":  # Se l'utente risponde 'no'
            break  # Esce dal ciclo della registrazione
    return utenti  # Ritorna la lista degli utenti registrati

@decoratore_nascondi_password  # Aggiungi il decoratore per nascondere le password
def stampa_utenti(utenti):  # Funzione per stampare tutti gli utenti registrati
    print("Utenti registrati:")  # Intestazione per la lista degli utenti
    for user, pwd in utenti:  # Ciclo attraverso ogni utente nella lista
        print("Username: " + user + ", Password: " + pwd)  # Stampa lo username e la password (ora nascosta)

def main():  # Funzione principale per gestire l'intero processo
    utenti = registra_utenti()  # Chiama la funzione per registrare gli utenti
    stampa_utenti(utenti)  # Stampa la lista degli utenti registrati

main()  # Esegui la funzione principale
