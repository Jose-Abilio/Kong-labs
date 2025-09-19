from infra.configs.connection import DBConnectionHandler
from infra.entities.produtos import Produtos

class ProdutosRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Produtos).all()
            return data 
        
    def insert(self, id, nome, preco, descricao):
        with DBConnectionHandler() as db:
            data_insert = Produtos(prod_id=id, prod_nome=nome, prod_preco=preco, prod_descricao=descricao)
            db.session.add(data_insert)
            db.session.commit()                                    

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Produtos).filter(Produtos.prod_id == id).delete()  
            db.session.commit()

    def update(self, id, nome, preco, descricao):
        with DBConnectionHandler() as db:
            db.session.query(Produtos).filter(Produtos.prod_id == id).update({"prod_nome": nome, "prod_preco": preco, "prod_descricao": descricao})
            db.session.commit()