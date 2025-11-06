import json
from horario import Horario
from DAO import DAO

class HorarioDAO(DAO):
  _objetos = []

  @classmethod
  def abrir (cls):
    cls._objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:
        list_dic = json.load(arquivo)
        for dic in list_dic:
          obj = Horario.from_json (dic)
          cls._objetos.append(obj)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:
      json.dump(cls._objetos, arquivo, default=Horario.to_json, indent=4)