from infra.configs.base import Base
from sqlalchemy import Column, LargeBinary, String, DateTime, Integer

import datetime

class Pessoa(Base):
    __tablename__ = 'pessoas'

    identificacao = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    data_cadastro = Column(DateTime, default=datetime.datetime.now)
    data_atualizacao = Column(DateTime)
    url_imagem = Column(String)
    face_encoding = Column(LargeBinary)

    def __repr__(self):
        return f"<Pessoa(client_id='{self.client_id}', identifificacao='{self.identificacao}, 'data_cadastro='{self.data_cadastro}', url_imagem='{self.url_imagem}')>"


