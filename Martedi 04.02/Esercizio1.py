# 1 definizione della classe Prodotto
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome  # nome del prodotto
        self.costo_produzione = costo_produzione  # costo di produzione
        self.prezzo_vendita = prezzo_vendita  # prezzo di vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione  # restitutzione profitto
# classe parallela Elettronica che eredita da Prodotto
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # Iattributi della classe base
        self.garanzia = garanzia  # nuovo attributo specifico per elettronica

# classe parallela Abbigliamento che eredita da Prodotto
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # attributi della classe base
        self.materiale = materiale  # nuovo attributo specifico per abbigliamento
        # classe Fabbrica 
    def __init__(self):
        self.inventario = {}  # dizionario che memorizza i prodotti e le loro quantità
    
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita  # aggiunge alla quantità esistente
        else:
            self.inventario[prodotto.nome] = quantita 
        print(f"Aggiunti {quantita} {prodotto.nome} all'inventario.")
    
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantita:
            self.inventario[prodotto.nome] -= quantita  
            profitto_totale = prodotto.calcola_profitto() * quantita 
            print(f"Venduti {quantita} {prodotto.nome}. Profitto totale: {profitto_totale}€")
        else:
            print(f"Errore: {prodotto.nome} non disponibile in quantità sufficiente.")
    
    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita  
        else:
            self.inventario[prodotto.nome] = quantita  
        print(f"Restituiti {quantita} {prodotto.nome} all'inventario.")
