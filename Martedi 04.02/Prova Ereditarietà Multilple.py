# Creiamo una classe chiamata "Veicolo" che rappresenta un generico veicolo.
class Veicolo:
    
    # Il metodo __init__ è il costruttore della classe. Viene eseguito automaticamente quando creiamo un nuovo oggetto "Veicolo".
    def __init__(self, marca, modello):
        
        # "self.marca" memorizza il valore della marca del veicolo.
        self.marca = marca
        
        # "self.modello" memorizza il valore del modello del veicolo.
        self.modello = modello

    # Questo metodo serve per mostrare le informazioni del veicolo.
    def mostra_informazioni(self):
        
        # Stampa il messaggio con marca e modello del veicolo.
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

# Creiamo una classe chiamata "DotazioniSpeciali" che rappresenta le dotazioni extra di un veicolo.
class DotazioniSpeciali:
    
    # Il costruttore della classe prende una lista di dotazioni speciali e le memorizza.
    def __init__(self, dotazioni):
        
        # "self.dotazioni" memorizza l'elenco delle dotazioni speciali del veicolo.
        self.dotazioni = dotazioni

    # Questo metodo serve per mostrare le dotazioni speciali del veicolo.
    def mostra_dotazioni(self):
        
        # Il metodo stampa le dotazioni speciali separandole con una virgola.
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}") 
