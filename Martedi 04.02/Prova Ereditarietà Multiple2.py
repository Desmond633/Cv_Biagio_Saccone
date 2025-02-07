class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)  
        # Alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni()  
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()  
        # Possiamo chiamare metodi di entrambe le superclassi