stringhe = []  # creo una lista vuota per le stringhe
stringa_pre = ""  # variabile per le stringhe precedenti

while True:  # ciclo infinito
    nuova_stringa = input("Inserisci una stringa")  # 
    
    lunghezza_nuova_stringa = 0 
    for carattere in nuova_stringa:  # ciclo per contare i caratteri nella nuova stringa
        lunghezza_nuova_stringa += 1  # incremento di 1 carattere sulla nuova stringa
    
    lunghezza_stringa_pre = 0  
    for carattere in stringa_pre:  # ciclo per i caratteri della stringa precedente
        lunghezza_stringa_pre += 1  
        
    if lunghezza_nuova_stringa > lunghezza_stringa_pre: 
        stringhe.append(nuova_stringa)  # se è più lunga si aggiunge alla lista
        stringa_pre = nuova_stringa  # e la sovrascriviamo
    else:
        break  # se la nuova è più corta il ciclo si interrompe

stringhe_finali = ""  # variabile vuota del contatore di stringhe
contatore = 0  # contatore numero di stringhe

for stringa in stringhe:  # ciclo"
    if contatore > 0:  # se il contatore è maggiore di 0 (vuol dire che non è la prima stringa)
        stringhe_finali += ", "  # virgola e spazio per separare
    stringhe_finali += stringa  # aggiunta della stringa finale alle altre stringhe
    contatore += 1  # incremento di 1 del contatore

print("stringhe inserite", stringhe_finali)  # stampa di tutte le stringhe
print("numero di stringhe inserite", contatore)  # stampa del numero delle stringhe
