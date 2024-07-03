class PessoaCadastradaDto:
    def __init__(self, client_id, identificacao, data_criacao, data_atualizacao = None):
        self.client_id = client_id
        self.identificacao = identificacao
        self.data_criacao = data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        self.data_atualizacao = data_atualizacao.strftime('%Y-%m-%d %H:%M:%S') if data_atualizacao != None else None