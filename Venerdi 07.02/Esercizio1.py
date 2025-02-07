class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
    def muovi(self):
        return f"{self.nome}: L'unità si sta spostando."
    def attacca(self):
        return f"{self.nome}: L'unità sta eseguendo l'attacco."
    def ritira(self):
        return f"{self.nome}: L'unità si sta ritirando."

class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_arma):
        super().__init__(nome, numero_soldati)
        self.tipo_arma = tipo_arma
    def attacca(self):
        return f"{self.nome}: Attacco con {self.tipo_arma} in corso."
    def costruisci_trincea(self):
        return f"{self.nome}: Inizia la costruzione di difese temporanee."

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        return f"{self.nome}: Regolazione dei cannoni per una maggiore precisione."

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        return f"{self.nome}: Esplorazione delle zone circostanti in corso."

class UnitaMista(Fanteria, Artiglieria):
    def __init__(self, nome, numero_soldati, tipo_arma):
        super().__init__(nome, numero_soldati, tipo_arma)
    
    def attacca(self):
        return f"{self.nome}: Attacco combinato di fanteria e artiglieria in corso."

class ControlloMilitare:
    def __init__(self):
        self.unita_registrate = {}

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome.lower()] = unita
        print(f"Unità {unita.nome} è stata registrata.")
    def mostra_unita(self):
        print("Unità registrate:")
        for nome in self.unita_registrate:
            print(f"- {nome.capitalize()}")
    def scegli_unita(self):
        unita_scelta = input("Seleziona un'unità: ").lower()
        if unita_scelta in self.unita_registrate:
            print(f"Hai selezionato l'unità: {unita_scelta.capitalize()}")
            return self.unita_registrate[unita_scelta]
        else:
            print(f"Unità {unita_scelta} non trovata.")
            return None
    def scegli_azione(self, unita):
        print(f"Le azioni disponibili per {unita.nome} sono:")
        print("- muovi")
        print("- attacca")
        print("- ritira")
        
        if type(unita) == Fanteria:
            print("costruisci_trincea")
        if type(unita) == Artiglieria:
            print("calibra_artiglieria")
        if type(unita) == Cavalleria:
            print("esplora_terreno")
        
        azione = input("Seleziona l'azione da eseguire: ").lower()
        if azione == "muovi":
            print(unita.muovi())
        elif azione == "attacca":
            print(unita.attacca())
        elif azione == "ritira":
            print(unita.ritira())
        elif type(unita) == Fanteria and azione == "costruisci_trincea":
            print(unita.costruisci_trincea())
        elif type(unita) == Artiglieria and azione == "calibra_artiglieria":
            print(unita.calibra_artiglieria())
        elif type(unita) == Cavalleria and azione == "esplora_terreno":
            print(unita.esplora_terreno())
        else:
            print(f"Azione {azione} non disponibile per questa unità.")

fanteria = Fanteria("Fanteria", 100, "fucile")
artiglieria = Artiglieria("Artiglieria", 30)
cavalleria = Cavalleria("Cavalleria", 40)

unita_mista = UnitaMista("Unita Mista", 50, "fucile e cannoni")

comando = ControlloMilitare()
comando.registra_unita(fanteria)
comando.registra_unita(artiglieria)
comando.registra_unita(cavalleria)
comando.registra_unita(unita_mista)

comando.mostra_unita()

unita_scelta = comando.scegli_unita()
if unita_scelta:
    comando.scegli_azione(unita_scelta)