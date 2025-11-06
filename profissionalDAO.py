import json
from profissional import Profissional
from DAO import DAO

class ProfissionalDAO(DAO):
  _objetos = []

  @classmethod
  def abrir(cls):
    cls._objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:
        list_dic = json.load(arquivo)
        for dic in list_dic:
          obj = Profissional.from_json(dic)
          cls._objetos.append(obj)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:
      json.dump(cls._objetos, arquivo, default=Profissional.to_json, indent=4)