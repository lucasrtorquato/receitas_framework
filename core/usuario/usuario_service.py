from core.usuario.usuario import Usuario
from core.usuario.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def cadastrar_usuario(self, nome, email, senha, situacao):
        #if self.repository.buscar_por_email(email):
        #    raise ValueError("Usuário já cadastrado com esse e-mail.")
        usuario = Usuario(nome, email, senha, situacao)
        return self.repository.salvar(usuario)

    def listar_usuarios(self):
        return self.repository.listar_todos()

    def excluir_usuario(self, email):
        if not self.repository.buscar_por_email(email):
            raise ValueError("Usuário não encontrado.")
        self.repository.remover_por_email(email)

    def excluir_usuario_por_id(self, id):
        if not self.repository.obter_por_id(id):
            raise ValueError("Usuário não encontrado.")
        self.repository.remover_por_id(id)

    def obter_usuario_por_id(self, id):
        usuario = self.repository.obter_por_id(id)
        if usuario is None:
            raise ValueError("Usuário não encontrado.")
        return usuario
