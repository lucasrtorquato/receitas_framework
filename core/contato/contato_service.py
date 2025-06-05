from core.contato.contato_repository import ContatoRepository
from core.contato.contato import Contato

class ContatoService:
    def __init__(self):
        self.repository = ContatoRepository()

    def atualizar_ou_inserir(self, contato: Contato):
        self.repository.salvar(contato)

    def obter_contato(self, id=1):
        contato = self.repository.buscar_por_id(id)
        if not contato:
            raise ValueError("Contato não encontrado.")
        return contato
