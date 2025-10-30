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
    if email == "admin":
        raise Exception("E-mail 'admin' é reservado.")

    for c in View.cliente_listar() + View.profissional_listar():
        if c.get_email() == email:
            raise Exception("Já existe um usuário com este e-mail.")
    cliente = Cliente(0, nome, email, fone, senha)
    ClienteDAO.inserir(cliente)
    
  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    ClienteDAO.atualizar(cliente)
    
  def cliente_excluir(id):
    for h in View.horario_listar():
        if h.get_id_cliente() == id:
            raise Exception("Cliente possui horário agendado. Não pode ser excluído.")
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
    for h in View.horario_listar():
        if h.get_data() == data and h.get_id_profissional() == id_profissional:
            raise Exception("Profissional já possui horário cadastrado nesse horário.")
    h = Horario(0, data)
    h.set_confirmado(confirmado)
    h.set_id_cliente(id_cliente)
    h.set_id_servico(id_servico)
    h.set_id_profissional(id_profissional)
    HorarioDAO.inserir(h)
    
  def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
    c = Horario(id, data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional) 
    HorarioDAO.atualizar(c)
    
  def horario_excluir(id):

    h = View.horario_listar_id(id)
    if h.get_id_cliente() != 0:
        raise Exception("Horário já agendado por um cliente. Não pode ser excluído.")
    HorarioDAO.excluir(h)


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
    if email == "admin":
        raise Exception("E-mail 'admin' é reservado.")

    for p in View.profissional_listar() + View.cliente_listar():
        if p.get_email() == email:
            raise Exception("Já existe um usuário com este e-mail.")
    c = Profissional(0, nome, especialidade, conselho, email, senha)
    ProfissionalDAO.inserir(c)
    
  def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
    c = Profissional(id, nome, especialidade, conselho, email, senha)
    ProfissionalDAO.atualizar(c)
    
  def profissional_excluir(id):
    for h in View.horario_listar():
        if h.get_id_profissional() == id:
            raise Exception("Profissional possui horários cadastrados. Não pode ser excluído.")
    c = Profissional(id, "", "", "", "", "")
    ProfissionalDAO.excluir(c)