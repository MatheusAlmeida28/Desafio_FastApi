from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI,HTTPException
from schemas import Livroschemas,Livroschemas2
from database import SessionLocal
import models


app = FastAPI()

db = SessionLocal()

@app.get('/')
def bem_vindo():
    return ('Bem Vindo ao sistema de livros!')

@app.get('/livro/ {livro_codigo_magico}', response_model=Livroschemas)
def obter_um_livro (livro_codigo_magico):
    obter_livro_por_codigo = db.query(models.Livros).filter(models.Livros.codigo_magico == livro_codigo_magico).first()
    
    if obter_livro_por_codigo is None:
        raise HTTPException(status_code=400, detail='livro não existente')
    
    return jsonable_encoder(obter_livro_por_codigo)


@app.post('/livros')
async def catalogar_um_livro(livros:Livroschemas):
    resgistro_de_livro_no_db = db.query(models.Livros).filter(models.Livros.codigo_magico == livros.codigo_magico).first()
     
    if resgistro_de_livro_no_db is not None:
        raise HTTPException(status_code=409, detail='Um livro já foi catalogado pelo mesmo código mágico')
    
    novo_livro=models.Livros(
        codigo_magico = livros.codigo_magico,
        titulo = livros.titulo,
        autor = livros.autor,
        professor = livros.professor,
        texto1 = livros.texto1,
        texto2 = livros.texto2,
        texto3 = livros.texto3,
        texto4 = livros.texto4,
        texto5 = livros.texto5,
        texto6 = livros.texto6,
        )

    
    db.add(novo_livro)
    db.commit()

    raise HTTPException(status_code = 201, detail='Livro catalogado com Sucesso!!!')


#Funcionalidades Extras: Atualizar informações e delete informações pelo código mágico
'''
@app.put('/livros/atualizar_infomacao/{livro_codigo}', response_model=Livroschemas2)
def item_a_ser_atualizado(livro_codigo: str, livro: Livroschemas2,):
    livro_no_banco_de_dados = db.query(models.Livros).filter(models.Livros.codigo_magico == livro_codigo).first()
    
    if livro_no_banco_de_dados is None:
        raise HTTPException(status_code=400, detail='Não conseguimos encontar as informações pelo código')
    
    try:
        if livro.titulo:
            livro_no_banco_de_dados.titulo = livro.titulo
    except:
        pass

    try:
        if livro.autor:
            livro_no_banco_de_dados.autor = livro.autor
    except:
        pass
    
    try:
        if livro.professor:
            livro_no_banco_de_dados.professor = livro.professor
    except:
        pass
    
    try:
        if livro.texto1:
            livro_no_banco_de_dados.texto1 = livro.texto1
    except:
        pass
    
    try:
        if livro.texto2:
            livro_no_banco_de_dados.texto2 = livro.texto2
    except:
        pass

    try:
        if livro.texto3:
            livro_no_banco_de_dados.texto3 = livro.texto3
    except:
        pass

    try:
        if livro.texto4:
            livro_no_banco_de_dados.texto4 = livro.texto4
    except:
        pass

    try:
        if livro.texto5:
            livro_no_banco_de_dados.texto5 = livro.texto5
    except:
        pass

    try:
        if livro.texto6:
            livro_no_banco_de_dados.texto6 = livro.texto6
    except:
        pass
    
    db.commit()  
    raise HTTPException(status_code=201, detail = 'Dados do livro atualizado com sucesso!')

@app.delete('/livro/deletar/{livro_codigo_magico}')
def deletar_item(livro_codigo_magico: str):
    deletar_livro_por_codigo = db.query(models.Livros).filter(models.Livros.codigo_magico == livro_codigo_magico).first()

    if deletar_livro_por_codigo is None:
        raise HTTPException(status_code=404, detail='Livro não existente')
    
    db.delete(deletar_livro_por_codigo)
    db.commit()

    raise HTTPException(status_code=200, detail='Dados de um livro apagado com sucesso!')'''





