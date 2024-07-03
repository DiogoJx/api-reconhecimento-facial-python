class RostoNaoEncontradoError(Exception):
    def __init__(self, message="Nenhum rosto encontrado na imagem."):
        self.message = message
        super().__init__(self.message)

class PessoaJaCadastradaError(Exception):
    def __init__(self, message="Pessoa já cadastrada na base de dados."):
        self.message = message
        super().__init__(self.message)
        
class ErroLeituraImagemError(Exception):
    def __init__(self, message="Erro ao ler imagem."):
        self.message = message
        super().__init__(self.message)

class PessoaNaoEncontradaError(Exception):
    def __init__(self, message="Pessoa não encontrada."):
        self.message = message
        super().__init__(self.message)