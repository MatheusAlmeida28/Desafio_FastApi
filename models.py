from sqlalchemy import String,Column,Text
from database import Base


class Livros(Base):
    __tablename__ = 'livros'
    codigo_magico = Column(String(8), primary_key=True)
    titulo = Column(String(255))
    autor = Column(String(255))
    professor = Column(String(255))
    texto1 = Column(Text)
    texto2 = Column(Text)
    texto3 = Column(Text)
    texto4 = Column(Text)
    texto5 = Column(Text)
    texto6 = Column(Text)
    
    def __repr__(self):
        return f"<livro autor={self.autor} preco={self.professor}>"