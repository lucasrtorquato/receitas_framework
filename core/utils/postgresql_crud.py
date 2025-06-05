import psycopg2
from psycopg2 import sql

# Internal database url (render)
DATABASE_URL = "postgresql://postgresql_usuario_user:sLsZ0dqBk1d7GAvsXzFTOyLIxnLbF2eN@dpg-cu9c183tq21c73ahm080-a/postgresql_usuario"

# External database url (render)
DATABASE_URL_EX = "postgresql://postgresql_usuario_user:sLsZ0dqBk1d7GAvsXzFTOyLIxnLbF2eN@dpg-cu9c183tq21c73ahm080-a.oregon-postgres.render.com/postgresql_usuario"


class PostgreSQLCRUD:
    def __init__(self):
        """Inicia a conexão com o banco de dados PostgreSQL."""
        try:
            self.connection = psycopg2.connect(DATABASE_URL_EX)
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão fechada.")
    
    def create(self, table, **fields):
        """Cria um novo registro na tabela especificada."""
        columns = fields.keys()
        values = fields.values()
        
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table),
            sql.SQL(", ").join(map(sql.Identifier, columns)),
            sql.SQL(", ").join(map(sql.Literal, values))
        )
        
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Registro inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir registro: {e}")
            self.connection.rollback()
    
    def read(self, table, **conditions):
        """Lê registros da tabela com base nas condições fornecidas."""
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table))
        
        if conditions:
            condition_str = " AND ".join([f"{k} = %s" for k in conditions])
            query = sql.SQL("{} WHERE {}").format(query, sql.SQL(condition_str))
            values = tuple(conditions.values())
        else:
            values = ()
        
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Erro ao ler registros: {e}")
            return []

    def update(self, table, set_fields, **conditions):
        """Atualiza registros na tabela com base nas condições fornecidas."""
        set_str = ", ".join([f"{k} = %s" for k in set_fields])
        condition_str = " AND ".join([f"{k} = %s" for k in conditions])
        
        query = sql.SQL("UPDATE {} SET {} WHERE {}").format(
            sql.Identifier(table),
            sql.SQL(set_str),
            sql.SQL(condition_str)
        )
        
        values = tuple(set_fields.values()) + tuple(conditions.values())
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Registro atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar registro: {e}")
            self.connection.rollback()
    
    def delete(self, table, **conditions):
        """Exclui registros da tabela com base nas condições fornecidas."""
        condition_str = " AND ".join([f"{k} = %s" for k in conditions])
        
        query = sql.SQL("DELETE FROM {} WHERE {}").format(
            sql.Identifier(table),
            sql.SQL(condition_str)
        )
        
        values = tuple(conditions.values())
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Registro excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir registro: {e}")
            self.connection.rollback()
