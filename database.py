from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

engine=create_engine("postgresql://postgres:postgres@localhost/livros_db", #postgres(é o usuário e a senha do programa que eu configurei,então vai de acordo com cada pessoa)
    echo=True               
)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
