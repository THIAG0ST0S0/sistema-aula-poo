import json
from cliente import Cliente

class ClienteDAO():
  _objetos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls._objetos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls._objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls._objetos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls._objetos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux != None:
      cls._objetos.remove(aux)
      cls._objetos.append(obj)
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir() 
    aux = cls.listar_id(obj.get_id())
    if aux != None:
      cls._objetos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls): 
    cls._objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:
        list_dic = json.load(arquivo)
        for dic in list_dic:
          obj = Cliente.from_json(dic)
          cls._objetos.append(obj)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls._objetos, arquivo, default=Cliente.to_json, indent=4)