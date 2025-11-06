import json
from serviço import Servico
from DAO import DAO

class ServicoDAO(DAO):
    __objetos = []

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("serviços.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("serviços.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)