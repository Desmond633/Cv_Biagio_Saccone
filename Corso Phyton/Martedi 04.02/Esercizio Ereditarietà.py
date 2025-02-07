# Creiamo una classe base chiamata "Animale".
class Animale:
    
    # Il costruttore (__init__) inizializza gli attributi comuni a tutti gli animali.
    def __init__(self, nome, eta):
        self.nome = nome  # Nome dell'animale
        self.eta = eta    # Età dell'animale

    # Metodo generico che stampa un suono generico.
    def fai_suono(self):
        print("L'animale fa un suono.")

# Creiamo la classe derivata "Elefante" che eredita dalla classe "Animale".
class Elefante(Animale):
    
    # Costruttore della classe Elefante.
    def __init__(self, nome, eta, peso):
        super().__init__(nome, eta)  # Richiama il costruttore della classe padre (Animale)
        self.peso = peso  # Nuovo attributo specifico per l'Elefante

    # Metodo specifico dell'Elefante che descrive l'uso della proboscide.
    def usa_proboscide(self):
        print(f"{self.nome} usa la proboscide per prendere acqua!")

    # Sovrascrive il metodo fai_suono per il barrito dell'elefante.
    def fai_suono(self):
        print("PRRR! L'elefante barrisce.")

# Creiamo la classe derivata "Aquila" che eredita da "Animale".
class Aquila(Animale):
    
    # Costruttore della classe Aquila.
    def __init__(self, nome, eta, apertura_alare):
        super().__init__(nome, eta)  # Richiama il costruttore della classe padre
        self.apertura_alare = apertura_alare  # Attributo specifico per l'Aquila

    # Metodo specifico dell'Aquila.
    def vola(self):
        print(f"{self.nome} sta volando con un'apertura alare di {self.apertura_alare} metri!")

    # Sovrascrive il metodo fai_suono per il verso dell'aquila.
    def fai_suono(self):
        print("L'aquila emette un fischio acuto.")

# Creiamo la classe derivata "Delfino" che eredita da "Animale".
class Delfino(Animale):
    
    # Costruttore della classe Delfino.
    def __init__(self, nome, eta, intelligenza):
        super().__init__(nome, eta)  # Richiama il costruttore della classe padre
        self.intelligenza = intelligenza  # Attributo specifico per il Delfino

    # Metodo specifico del Delfino.
    def salta_fuori_dall_acqua(self):
        print(f"{self.nome} salta fuori dall'acqua mostrando la sua intelligenza di livello {self.intelligenza}!")

    # Sovrascrive il metodo fai_suono per il suono del delfino.
    def fai_suono(self):
        print("Il delfino emette fischi e clic sonori.")

# Creiamo degli oggetti per testare il funzionamento delle classi.
dumbo = Elefante("Dumbo", 10, 5000)  # Creiamo un Elefante
dumbo.fai_suono()  # Simula il barrito
dumbo.usa_proboscide()  # Simula l'uso della proboscide

freccia = Aquila("Freccia", 4, 2.3)  # Creiamo un'Aquila
freccia.fai_suono()  # Simula il verso dell'aquila
freccia.vola()  # Simula il volo dell'aquila

flipper = Delfino("Flipper", 6, 9)  # Creiamo un Delfino
flipper.fai_suono()  # Simula il suono del delfino
flipper.salta_fuori_dall_acqua()  # Simula il salto del delfino
