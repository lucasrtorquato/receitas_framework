from core.receita.receita_repository import ReceitaRepository
from core.receita.receita import Receita

class ReceitaService:
    def __init__(self):
        self.repository = ReceitaRepository()

    def cadastrar_ou_atualizar(self, nome, ingredientes, modo_preparo, categoria, id=None):
        receita = Receita(nome, ingredientes, modo_preparo, categoria, id)
        print(nome, ingredientes, modo_preparo, categoria, id)
        if not receita.nome_receita.strip():
            raise ValueError("Nome da receita é obrigatório.")
        self.repository.salvar(receita)

    def listar_receitas(self):
        return self.repository.listar_todas()

    def obter_receita_por_id(self, id):
        receita = self.repository.buscar_por_id(id)
        if not receita:
            raise ValueError("Receita não encontrada.")
        return receita

    def excluir_receita(self, id):
        receita = self.repository.buscar_por_id(id)
        if not receita:
            raise ValueError("Receita não encontrada.")
        self.repository.remover_por_id(id)

    def filtrar_receitas(self, nome=None, categoria=None):
        return self.repository.filtrar_por_nome_e_categoria(nome, categoria)
