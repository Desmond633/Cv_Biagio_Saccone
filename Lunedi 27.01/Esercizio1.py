posizione = (input("Vivi in Italia?"))
anni = int(input("Quanti anni hai?"))
diploma = (input("Sei diplomato?)"))

if posizione == "si":
    if anni >= 18:
        if diploma == "si":
            print("Candidatura inviata")
        else:
            print("Devi essere diplomato!")
    else:
        print("Devi avere almeno 18 anni!")
else:
    print("Devi vivere in Italia!")