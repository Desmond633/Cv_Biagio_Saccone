class Persona:
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome
    def get_eta(self):
        return self._eta
    def set_eta(self, eta):
        self._eta = eta
    def presentazione(self):
        print(f"Ciao, mi chiamo {self._nome} e ho {self._eta} anni.")

class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.voti = voti 
    
    def calcola_media(self):
        return sum(self.voti) / len(self.voti) if self.voti else 0
    
    def presentazione(self):
        media = self.calcola_media()
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. La mia media dei voti è {media:.2f}.")

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. Insegno {self.materia}.")

studente = Studente("Marco", 20, [28, 30, 25, 26])
professore = Professore("Prof. Rossi", 45, "Matematica")
studente.presentazione() 
professore.presentazione() 