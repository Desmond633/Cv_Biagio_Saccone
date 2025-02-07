def decoratore_con_argomenti(funzione):
    def wrapper(*args,**kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a,b):
    return a+b

print(somma(3,4))