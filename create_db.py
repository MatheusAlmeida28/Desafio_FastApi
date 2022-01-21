from database import Base,engine
from sqlalchemy import String,Column,Text

class Item(Base):
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


Base.metadata.create_all(engine)

print('Criando banco de dados......')
