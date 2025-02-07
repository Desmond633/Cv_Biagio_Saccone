class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

def descrivi(self):
        print(f"Nome: {self.nome}, Età: {self.eta}")
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def gioca_partita(self):
        print(f"{self.nome}, che gioca come {self.ruolo} con il numero {self.numero_maglia}, è in campo!")

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    def dirige_allenamento(self):
        print(f"L'allenatore {self.nome}, con {self.anni_di_esperienza} anni di esperienza, sta dirigendo l'allenamento.")

class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def supporta_team(self):
        print(f"{self.nome}, specializzato in {self.specializzazione}, sta aiutando la squadra.")