class NoFilePartError(Exception):
    def __init__(self, message="No file part."):
        self.message = message
        super().__init__(self.message)

class NoSelectedFileError(Exception):
    def __init__(self, message="No selected file."):
        self.message = message
        super().__init__(self.message)

class FileNotFoundError(Exception):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        super().__init__(f"Arquivo {nome_arquivo} não encontrado.")

class DeletarArquivoError(Exception):
    def __init__(self, nome_arquivo, erro):
        self.nome_arquivo = nome_arquivo
        self.erro = erro
        super().__init__(f"Erro ao deletar o arquivo {nome_arquivo}: {erro}")