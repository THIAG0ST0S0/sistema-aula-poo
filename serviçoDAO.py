
class ServicoDAO(BaseDAO):
    def __init__(self):
        super().__init__(arquivo='servicos.json', classe_modelo=Servico)

    