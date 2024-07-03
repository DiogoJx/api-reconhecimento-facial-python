class PessoaAutenticadaDTO:
    def __init__(self, client_id, identificacao, autenticado, distancia_da_face):
        self.client_id = client_id
        self.identificacao = identificacao
        self.autenticado =bool(autenticado)
        self.distancia_da_face = distancia_da_face

