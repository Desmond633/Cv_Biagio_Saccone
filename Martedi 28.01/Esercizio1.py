lista_dei_film = ["Esorcista", "The Mask", "Le colline hanno gli occhi"]

età = int(input("Qual è la tua età?"))
if età < 18:
    print("Non puoi vedere questi film.")
else:
    print("Puoi vedere questi film:")
    print("1 -", lista_dei_film[0])
    print("2 -", lista_dei_film[1])
    print("3 -", lista_dei_film[2])

    scelta = int(input("Inserisci il numero del film che vuoi vedere (1, 2 o 3): "))
    if scelta == 1:
        print("Hai scelto di vedere:", lista_dei_film[0])
    elif scelta == 2:
        print("Hai scelto di vedere:", lista_dei_film[1])
    elif scelta == 3:
        print("Hai scelto di vedere:", lista_dei_film[2])
    else:
        print("Scelta non valida. Riprova.")
