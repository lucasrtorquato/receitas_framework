import sqlite3
from core.usuario.usuario import Usuario

class UsuarioRepository:
    def __init__(self, db_path='dbReceitas.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabela()

    def _criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            situacao TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()
    
    def salvar(self, usuario: Usuario):
        # Se usuário já existe (email), atualiza; senão insere
        cursor = self.conn.cursor()
        existente = self.buscar_por_email(usuario.email)
        if existente:
            sql = """
            UPDATE usuarios SET nome=?, senha=?, situacao=? WHERE email=?
            """
            cursor.execute(sql, (usuario.nome, usuario.senha, usuario.situacao, usuario.email))
        else:
            sql = """
            INSERT INTO usuarios (nome, email, senha, situacao) VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.situacao))
        self.conn.commit()
        return usuario

    def buscar_por_email(self, email):
        query = 'SELECT * FROM usuarios WHERE email = ?'
        cursor = self.conn.execute(query, (email,))
        row = cursor.fetchone()
        return Usuario(**row) if row else None

    def listar_todos(self):
        query = 'SELECT * FROM usuarios'
        cursor = self.conn.execute(query)
        return [Usuario(**row) for row in cursor.fetchall()]

    def remover_por_email(self, email):
        query = 'DELETE FROM usuarios WHERE email = ?'
        self.conn.execute(query, (email,))
        self.conn.commit()

    def remover_por_id(self, id):
        query = 'DELETE FROM usuarios WHERE id = ?'
        self.conn.execute(query, (id,))
        self.conn.commit()

    def obter_por_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                situacao=row["situacao"]
            )
        else:
            return None
