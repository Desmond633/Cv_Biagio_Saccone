# Registrazione
nome = input("Inserisci un nome: ")
if nome != "":
    print("Puoi proseguire")
else:
    print("Devi inserire un nome")

password = input("Inserisci una password: ")
if password != "":
    print("Ti sei registrato con successo, Benvenuto", nome)
else:
    print("Devi inserire una password")

# Domande segrete
print("Scegli una domanda segreta:")
print("1. Qual è il tuo colore preferito?")
print("2. Qual è il tuo animale preferito?")
domanda_scelta = input("Scegli 1 o 2: ")

# Chiedi la risposta alla domanda scelta
if domanda_scelta == "1":
    risposta_color = input("Qual è il tuo colore preferito? ")
    print("Hai scelto la domanda sul colore, la tua risposta è:", risposta_color)
    domanda_correct = risposta_color  # Salviamo la risposta alla domanda
elif domanda_scelta == "2":
    risposta_animale = input("Qual è il tuo animale preferito? ")
    print("Hai scelto la domanda sull'animale, la tua risposta è:", risposta_animale)
    domanda_correct = risposta_animale  # Salviamo la risposta alla domanda
else:
    print("Scelta non valida, procediamo comunque.")
    domanda_correct = ""  # Se l'utente non sceglie 1 o 2, non avrà risposta alla domanda segreta

# Login
nome_registrato = nome  # Salviamo il nome che l'utente ha registrato
password_registrata = password  # Salviamo la password che l'utente ha registrato

# Effettua il login
nome_usato = input("Effettua il login, reinserisci il nome: ")
if nome_usato == nome_registrato:  # Confrontiamo il nome immesso con quello registrato
    print("Il nome è corretto")
    
    password_usata = input("Reinserisci la password: ")
    if password_usata == password_registrata:  # Confrontiamo la password immessa con quella registrata
        print("La password è corretta")
        
        # Ora chiediamo la domanda segreta
        domanda_scelta_login = input("Scegli la domanda segreta per il login: 1. Colore preferito  2. Animale preferito: ")
        if domanda_scelta_login == "1":
            risposta_color_login = input("Qual è il tuo colore preferito? ")
            if risposta_color_login == risposta_color:
                print("Risposta corretta, Bentornato", nome_usato)
            else:
                print("Risposta errata, accesso negato")
        elif domanda_scelta_login == "2":
            risposta_animale_login = input("Qual è il tuo animale preferito? ")
            if risposta_animale_login == risposta_animale:
                print("Risposta corretta, Bentornato", nome_usato)
            else:
                print("Risposta errata, accesso negato")
        else:
            print("Scelta non valida, accesso negato")
    else:
        print("La password è sbagliata")
else:
    print("Il nome è sbagliato")
    
modifica_scelta = input("Vuoi modificare il nome utente o la password? (nome/password) o digita 'no' per non fare modifiche: ").lower()

# Modifica nome
if modifica_scelta == "nome":
    nuovo_nome = input("Inserisci il nuovo nome utente: ")
    if nuovo_nome == nome:
        print("Il nuovo nome utente non può essere uguale al nome registrato.")
    else:
        nome = nuovo_nome
        print("Il nome utente è stato modificato con successo.")
elif modifica_scelta == "password":
    nuova_password = input("Inserisci la nuova password: ")
    if nuova_password == password:
        print("La nuova password non può essere uguale alla password registrata.")
    else:
        password = nuova_password
        print("La password è stata modificata con successo.")
elif modifica_scelta == "no":
    print("Nessuna modifica è stata fatta.")
else:
    print("Scelta non valida, nessuna modifica effettuata.")