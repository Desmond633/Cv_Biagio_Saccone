class MetodoPagamento:
    def __init__(self, importo):
        self.importo = importo

    def effettua_pagamento(self):
        raise NotImplementedError("Questo metodo deve essere sovrascritto dalle sottoclassi")

class CartaDiCredito(MetodoPagamento):
    def __init__(self, importo, numero_carta):
        super().__init__(importo)
        self.numero_carta = numero_carta

    def effettua_pagamento(self):
        print(f"Pagamento di {self.importo:.2f}€ effettuato con Carta di Credito n. {self.numero_carta}.")

class PayPal(MetodoPagamento):
    def __init__(self, importo, conto_paypal):
        super().__init__(importo)
        self.conto_paypal = conto_paypal

    def effettua_pagamento(self):
        print(f"Pagamento di {self.importo:.2f}€ effettuato tramite PayPal (conto: {self.conto_paypal}).")
        
class BonificoBancario(MetodoPagamento):
    def __init__(self, importo, conto_bancario):
        super().__init__(importo)
        self.conto_bancario = conto_bancario

    def effettua_pagamento(self):
        print(f"Pagamento di {self.importo:.2f}€ effettuato tramite Bonifico Bancario (conto: {self.conto_bancario}).")

class GestorePagamenti:
    def paga(self, pagamento):
        pagamento.effettua_pagamento()

def main():
    pagamento1 = CartaDiCredito(100, "1234-5678-9876-5432")
    pagamento2 = PayPal(200, "utente@example.com")
    pagamento3 = BonificoBancario(300, "IT000000789")

    gestore = GestorePagamenti()
    gestore.paga(pagamento1)
    gestore.paga(pagamento2)
    gestore.paga(pagamento3)

if __name__ == "__main__":
    main()
