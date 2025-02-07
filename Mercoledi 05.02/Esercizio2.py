class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        self.__titolare = titolare
        self.__saldo = saldo_iniziale

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo} effettuato. Nuovo saldo: {self.__saldo}")
        else:
            print("Errore: l'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo > 0:
            if importo <= self.__saldo:
                self.__saldo -= importo
                print(f"Prelievo di {importo} effettuato. Nuovo saldo: {self.__saldo}")
            else:
                print("Errore: saldo insufficiente.")
        else:
            print("Errore: l'importo del prelievo deve essere positivo.")

    def visualizza_saldo(self):
        return f"Il saldo attuale è: {self.__saldo}"

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
            print("Nome del titolare aggiornato con successo.")
        else:
            print("Errore: il nome del titolare deve essere una stringa non vuota.")

class Banca:
    def __init__(self, nome):
        self.nome = nome
        self.conti = []

    def crea_conto(self, titolare, saldo_iniziale=0.0):
        nuovo_conto = ContoBancario(titolare, saldo_iniziale)
        self.conti.append(nuovo_conto)
        print(f"Conto per {titolare} creato con successo.")
        return nuovo_conto

    def mostra_conti(self):
        if not self.conti:
            print("Nessun conto presente nella banca.")
        else:
            for conto in self.conti:
                print(f"Titolare: {conto.get_titolare()}, Saldo: {conto.visualizza_saldo()}")

# Esempio di utilizzo della classe
banca = Banca("Banca Centrale")
conto1 = banca.crea_conto("Mario Rossi", 1000)
conto2 = banca.crea_conto("Luigi Bianchi", 500)

conto1.deposita(500)
conto2.preleva(200)

banca.mostra_conti()
