import face_recognition as fr
from datetime import datetime
import pickle
from dtos.pessoa_autenticada_dto import PessoaAutenticadaDTO
from infra.repositories.pessoa_repository import PessoaRepository
from infra.entities.pessoa import Pessoa
from exceptions.service_exception import ErroLeituraImagemError, PessoaJaCadastradaError, RostoNaoEncontradoError, PessoaNaoEncontradaError

class ReconhecimentoService:
    
    pessoa_repository: PessoaRepository
    
    def __init__(self):
        self.pessoa_repository =  PessoaRepository()

    def reconhecer_rosto(self, url_foto):
        foto = fr.load_image_file(url_foto)
        face_encoding = fr.face_encodings(foto)

        if face_encoding:
            return face_encoding[0] 
        return None

    def cadastrar_pessoa_com_reconhecimento(self, client_id, identificacao, url_imagem):
        face_encoding = self.reconhecer_rosto(url_imagem)
        
        if not face_encoding.any():
            raise RostoNaoEncontradoError()
        
        buscar_pessoa = self.pessoa_repository.buscar_por_identificacao(identificacao, client_id)
        
        if buscar_pessoa:
            raise PessoaJaCadastradaError()
            
        data_cadastro = datetime.now()
        face_encoding_serialized = pickle.dumps(face_encoding)
        
        pessoa = self.pessoa_repository.salvar(
            client_id=client_id,
            identificacao=identificacao,
            data_cadastro=data_cadastro,
            url_imagem=url_imagem,
            face_encoding=face_encoding_serialized
        )
            
        return pessoa
    
    def atualizar_cadastro(self, client_id, identificacao, url_imagem):
        face_encoding = self.reconhecer_rosto(url_imagem)
        
        if not face_encoding.any():
            raise RostoNaoEncontradoError()
        
        pessoa_existente = self.pessoa_repository.buscar_por_identificacao(identificacao, client_id)
        
        if not pessoa_existente:
            raise PessoaNaoEncontradaError()

        data_atualizacao = datetime.now()
        face_encoding_serialized = pickle.dumps(face_encoding)
        
        pessoa_atualizada = self.pessoa_repository.atualizar(
            identificacao=identificacao,
            client_id=client_id,
            data_atualizacao=data_atualizacao,
            url_imagem=url_imagem,
            face_encoding=face_encoding_serialized
        )
            
        return pessoa_atualizada
             
    def autenticar_pessoa(self, identificacao, url_imagem, client_id):
        face_encoding = self.reconhecer_rosto(url_imagem)
        if not face_encoding.any():
            raise ErroLeituraImagemError()
        pessoa: Pessoa = self.pessoa_repository.buscar_por_identificacao(identificacao=identificacao, client_id=client_id)
        if not pessoa:
            raise PessoaNaoEncontradaError()
        face_encoding_from_db = pickle.loads(pessoa.face_encoding)       
        autenticado = fr.compare_faces([face_encoding], face_encoding_from_db)[0]
        face_distances = fr.face_distance([face_encoding], face_encoding_from_db)[0]
     
        pessoa_autenticada = PessoaAutenticadaDTO(pessoa.client_id, pessoa.identificacao, autenticado, face_distances)
        return pessoa_autenticada
     