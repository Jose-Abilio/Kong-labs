from infra.configs.connection import DBConnectionHandler
from infra.entities.usuarios import Usuarios

class UsersRepository:
    def select(self, email):
        with DBConnectionHandler() as db:
            data = db.session.query(Usuarios).filter(Usuarios.user_email == email).first()
            return data 

    def insert(self, nome, email, senha):
        with DBConnectionHandler() as db:
            data_insert = Usuarios(user_nome=nome, user_email=email, user_senha=senha)
            db.session.add(data_insert)
            db.session.commit()                                    

    def delete(self, nome):
        with DBConnectionHandler() as db:
            db.session.query(Usuarios).filter(Usuarios.user_nome == nome).delete()  
            db.session.commit()