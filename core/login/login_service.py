from core.login.login import Login
from core.login.login_repository import LoginRepository

class LoginService:
    def __init__(self):
        self.repository = LoginRepository()

    def autenticar(self, login: Login):
        usuario = self.repository.buscar_usuario_por_email(login.email)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        if usuario.senha != login.senha:
            raise ValueError("Senha incorreta.")
        if usuario.situacao.lower() != "ativo":
            raise ValueError("Usuário inativo.")
        return usuario
