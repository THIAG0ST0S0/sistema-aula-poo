class Servico:
    def __init__(self, id: int, descricao: str, valor: float):
        self._id = id 
        self._descricao = descricao
        self._valor = valor

    def __str__(self) -> str:
        return f"Serviço [ID: {self._id}, Descrição: {self._descricao}, Valor: R${self._valor:.2f}]"
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, novo_id: int):
        self._id = novo_id

    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self._descricao = nova_descricao

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, novo_valor: float):
        if novo_valor >= 0:
            self._valor = novo_valor
        else:
            raise ValueError("O valor do serviço não pode ser negativo.")

    def to_json(self) -> dict:
        return {
            "id": self._id,
            "descricao": self._descricao,
            "valor": self._valor
        }

    @staticmethod
    def from_json(dados_json: dict):
        if 'id' not in dados_json or 'descricao' not in dados_json or 'valor' not in dados_json:
             raise ValueError("JSON inválido: faltando campos essenciais.")
             
        return Servico(
            id=dados_json['id'],
            descricao=dados_json['descricao'],
            valor=dados_json['valor']
        )

if __name__ == '__main__':
    servico1 = Servico(1, "Consulta Odontológica", 150.00)
    print(servico1)

    print(f"Descrição: {servico1.descricao}")

    servico1.valor = 180.50
    print(f"Novo Valor: R${servico1.valor:.2f}")

    dados_servico_json = servico1.to_json()
    print(f"JSON: {dados_servico_json}")

    servico2 = Servico.from_json(dados_servico_json)
    print(f"Serviço criado de JSON: {servico2}")