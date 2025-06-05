class Receita:
    def __init__(self, nome_receita="", ingredientes="", modo_preparo="", categoria="", id=None):
        self.id = id
        self.nome_receita = nome_receita
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.categoria = categoria