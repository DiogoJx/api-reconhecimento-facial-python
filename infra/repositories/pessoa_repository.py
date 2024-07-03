import datetime
from dtos.pessoa_cadatrada_dto import PessoaCadastradaDto
from infra.configs.connection import DBConnectionHandler
from infra.entities.pessoa import Pessoa

class PessoaRepository:

    def buscar_todos(self):
        with DBConnectionHandler() as db:
            pessoas = db.session.query(Pessoa).all()
            return pessoas

    def buscar_por_identificacao(self, identificacao, client_id):
        with DBConnectionHandler() as db:
            pessoa = db.session.query(Pessoa).filter_by(identificacao=identificacao, client_id = client_id).first()
            return pessoa

    def salvar(self, identificacao, client_id, data_cadastro, url_imagem, face_encoding):
        with DBConnectionHandler() as db:
            pessoa = Pessoa(client_id=client_id, identificacao = identificacao, data_cadastro=data_cadastro, url_imagem=url_imagem, face_encoding=face_encoding)
            db.session.add(pessoa)
            db.session.commit()
            
            if pessoa.identificacao:
                return  PessoaCadastradaDto(pessoa.client_id, pessoa.identificacao, pessoa.data_cadastro)
            return None
            
    def delete(self, identificacao):
        with DBConnectionHandler() as db:
            db.session.query(Pessoa).filter(Pessoa.identificacao == identificacao).delete()
            db.session.commit()
            
    def atualizar(self, identificacao, client_id, data_atualizacao, url_imagem, face_encoding):
        with DBConnectionHandler() as db:
            pessoa = db.session.query(Pessoa).filter(
                Pessoa.identificacao == identificacao, 
                Pessoa.client_id == client_id).first()
            
            if pessoa: 
                pessoa.url_imagem = url_imagem
                pessoa.face_encoding = face_encoding
                pessoa.data_atualizacao = data_atualizacao
                
                db.session.commit() 
                
                return PessoaCadastradaDto(pessoa.client_id, pessoa.identificacao, pessoa.data_cadastro, pessoa.data_atualizacao)
            
            return None 
    