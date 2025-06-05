class Usuario:
    def __init__(self, nome, email, senha, situacao, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.situacao = situacao
