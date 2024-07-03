import os
from cv2 import FileStorage

from exceptions.file_exception import NoFilePartError, NoSelectedFileError
class FileHelper:
    @staticmethod
    def validar_arquivo_requisicao(request):
        if 'file' not in request.files:
            raise NoFilePartError()

        file = request.files['file']
        if file.filename == '':
            raise NoSelectedFileError()
        return file
    
    @staticmethod
    def salvar_imagem_repositorio(diretorio: str, identificacao: str, file: FileStorage):
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        imagem = os.path.join(diretorio, f"{identificacao}.jpg")
        file.save(imagem)
        return imagem
    
    def remover_imagem(caminho_imagem: str):
        try:
            if os.path.exists(caminho_imagem):
                os.remove(caminho_imagem)
                return True 
            else:
                return False 
        except Exception as e:
            print(f"Erro ao remover a imagem: {e}")
            return False 
