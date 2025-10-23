from datetime import datetime

class Horario:
  def __init__(self, id, data):
    self.set_id(id)
    self.set_data(data)
    self.set_confirmado(False)
    self.set_id_cliente(0)
    self.set_id_servico(0)
    self.set_id_profissional(0)

  def __str__(self):
    return f"{self.get_id()} - {self.get_data().strftime('%d/%m/%Y %H:%M')} - Confirmado: {self.get_confirmado()}"

  def get_id(self):
    return self._id
  def get_data(self):
    return self._data
  def get_confirmado(self):
    return self._confirmado
  def get_id_cliente(self):
    return self._id_cliente
  def get_id_servico(self):
    return self._id_servico
  def get_id_profissional(self):
    return self._id_profissional

  def set_id(self, id):
    self._id = id
  def set_data(self, data):
    self._data = data
  def set_confirmado(self, confirmado):
    self._confirmado = confirmado
  def set_id_cliente(self, id_cliente):
    self._id_cliente = id_cliente
  def set_id_servico(self, id_servico):
    self._id_servico = id_servico
  def set_id_profissional(self, id_profissional):
    self._id_profissional = id_profissional

  def to_json(self):
    dic = {
      "id": self._id,
      "data": self._data.strftime("%d/%m/%Y %H:%M"),
      "confirmado": self._confirmado,
      "id_cliente": self._id_cliente,
      "id_servico": self._id_servico,
      "id_profissional": self._id_profissional  
    }
    return dic

  @staticmethod
  def from_json(dic):
    horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
    horario.set_confirmado(dic["confirmado"])
    horario.set_id_cliente(dic["id_cliente"])
    horario.set_id_servico(dic["id_servico"])
    if "id_profissional" in dic:
      horario.set_id_profissional(dic["id_profissional"])
    else:
      horario.set_id_profissional(0)
    return horario