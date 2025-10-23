from cliente import Cliente
from clienteDAO import ClienteDAO
from serviço import Servico
from serviçoDAO import ServicoDAO
from horario import Horario
from horarioDAO import HorarioDAO
from profissional import Profissional
from profissionalDAO import ProfissionalDAO
from datetime import datetime

class View:

  def cliente_criar_admin():
    admin_existe = False
    for c in View.cliente_listar():
      if c.get_email() == "admin":
        admin_existe = True
        break
    if not admin_existe:
      View.cliente_inserir("admin", "admin", "0000", "1234")

  def cliente_autenticar(email, senha):
    for c in View.cliente_listar():
      if c.get_email() == email and c.get_senha() == senha:
        return c
    return None

  def cliente_listar():
    return ClienteDAO.listar()
  
  def cliente_listar_id(id):
    return ClienteDAO.listar_id(id)
    
  def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    ClienteDAO.inserir(cliente)
    
  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    ClienteDAO.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    ClienteDAO.excluir(cliente)

  def servico_listar():
    return ServicoDAO.listar()
  def servico_listar_id(id):
    return ServicoDAO.listar_id(id)
  def servico_inserir(descricao, valor):
    servico = Servico(0, descricao, valor)
    ServicoDAO.inserir(servico)
  def servico_atualizar(id, descricao, valor):
    servico = Servico(id, descricao, valor)
    ServicoDAO.atualizar(servico)
  def servico_excluir(id):
    servico = Servico(id, "", 0)
    ServicoDAO.excluir(servico)


  def horario_listar():
    return HorarioDAO.listar()
    
  def horario_listar_id(id):
    return HorarioDAO.listar_id(id)
    
  def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
    c = Horario(0, data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional) 
    HorarioDAO.inserir(c)
    
  def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
    c = Horario(id, data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional) 
    HorarioDAO.atualizar(c)
    
  def horario_excluir(id):

    c = Horario(id, datetime.now()) 
    HorarioDAO.excluir(c)


  def profissional_autenticar(email, senha):
    for p in View.profissional_listar():
      if p.get_email() == email and p.get_senha() == senha:
        return p 
    return None

  def profissional_listar():
    return ProfissionalDAO.listar()
    
  def profissional_listar_id(id):
    return ProfissionalDAO.listar_id(id)
    
  def profissional_inserir(nome, especialidade, conselho, email, senha):
    c = Profissional(0, nome, especialidade, conselho, email, senha)
    ProfissionalDAO.inserir(c)
    
  def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
    c = Profissional(id, nome, especialidade, conselho, email, senha)
    ProfissionalDAO.atualizar(c)
    
  def profissional_excluir(id):
    c = Profissional(id, "", "", "", "", "")
    ProfissionalDAO.excluir(c)