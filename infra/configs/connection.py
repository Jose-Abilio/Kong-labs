from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.configs.base import Base

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///kong_labs.db"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def create_db_tables(self):
        engine = self.get_engine()
        Base.metadata.create_all(engine)
        print("Tabelas do banco de dados criadas com sucesso!")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()