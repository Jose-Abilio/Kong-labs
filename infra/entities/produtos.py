from sqlalchemy import String, Date, func
from sqlalchemy.orm import mapped_column, Mapped
from infra.configs.base import Base
from datetime import date

class Produtos(Base):
    __tablename__ = 'produtos'
    
    prod_id: Mapped[int] = mapped_column(primary_key=True)
    prod_nome: Mapped[str] = mapped_column(String(30), nullable=False)
    prod_preco: Mapped[float] = mapped_column(nullable=False)
    prod_descricao: Mapped[str] = mapped_column(String(100), nullable=False)    
    prod_data_criacao: Mapped[date] = mapped_column(Date, default=func.current_date() , nullable=False)
    
    def __repr__(self):
        return f'<Produto {self.nome}>'