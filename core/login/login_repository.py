import sqlite3
from core.usuario.usuario import Usuario  

class LoginRepository:
    def __init__(self, db_path='dbReceitas.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def buscar_usuario_por_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return Usuario(row["nome"], row["email"], row["senha"], row["situacao"])
        return None
