from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    
    @abstractmethod
    def calcola_stipendio(self):
        pass

class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

class ImpiegatoAProvvigione(Impiegato):
    """
    Classe derivata per gli impiegati a provvigione.
    """
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale):
        super().__init__(nome, cognome, stipendio_base) 
        self.vendite = vendite 
        self.percentuale = percentuale 
    
    def calcola_stipendio(self):
        return self.stipendio_base + (self.vendite * self.percentuale)

def stampa_dettagli_impiegato(impiegato):
    """
    Funzione per stampare le informazioni di un impiegato e il suo stipendio calcolato.
    """
    print(f"Impiegato: {impiegato.nome} {impiegato.cognome}")
    print(f"Stipendio: {impiegato.calcola_stipendio()}")

impiegato1 = ImpiegatoFisso("Mario", "Rossi", 2000)
impiegato2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1500, 5000, 0.1)

stampa_dettagli_impiegato(impiegato1)
stampa_dettagli_impiegato(impiegato2)
