from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from infra.configs.base import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'
    
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_nome: Mapped[str] = mapped_column(String(50), nullable=False)
    user_email: Mapped[str] = mapped_column(String(50), nullable=False)
    user_senha: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'