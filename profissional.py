import json

class Profissional():
  def __init__(self, id, nome, especialidade, conselho, email, senha):
    self.set_id(id)
    self.set_nome(nome)
    self.set_especialidade(especialidade)
    self.set_conselho(conselho)
    self.set_email(email)
    self.set_senha(senha)

  def __str__(self):
    return f"{self.__nome} - {self.__especialidade}"

  def get_id(self):
    return self.__id
  def get_nome(self):
    return self.__nome
  def get_especialidade(self):
    return self.__especialidade
  def get_conselho(self):
    return self.__conselho
  def get_email(self):
    return self.__email
  def get_senha(self):
    return self.__senha

  def set_id(self, id):
    self.__id = id
  def set_nome(self, nome):
    if nome == "" or nome is None:
        raise Exception("Profissional deve possuir um nome.")
    self.__nome = nome
  def set_especialidade(self, especialidade):
    self.__especialidade = especialidade
  def set_conselho(self, conselho):
    self.__conselho = conselho
  def set_email(self, email):
    if email == "" or email is None:
        raise Exception("Profissional deve possuir um e-mail.")
    self.__email = email
  def set_senha(self, senha):
    if senha == "" or senha is None:
        raise Exception("Profissional deve possuir uma senha.")
    self.__senha = senha
  def to_json(self):
    return {
      "id": self.__id,
      "nome": self.__nome,
      "especialidade": self.__especialidade,
      "conselho": self.__conselho,
      "email": self.__email,
      "senha": self.__senha
    }

  @staticmethod
  def from_json(dic):
    return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])