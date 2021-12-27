from pydantic import BaseModel
import string
import random

codigo_aleatorio = (''.join(random.choice(string.ascii_letters).upper() for letras in range(8)))


class Livroschemas(BaseModel):
    codigo_magico:str = codigo_aleatorio
    titulo:str = None
    autor:str = None
    professor:str = None
    texto1:str = None
    texto2:str = None
    texto3:str = None
    texto4:str = None
    texto5:str = None
    texto6:str = None
    

    class config:
        orm_mode = True

class Livroschemas2(BaseModel): #Esse Schema serve apenas caso o método update seja usado
    titulo:str = None
    autor:str = None
    professor:str = None
    texto1:str = None
    texto2:str = None
    texto3:str = None
    texto4:str = None
    texto5:str = None
    texto6:str = None
    

    class config:
        orm_mode = True

