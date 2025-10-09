from horario import Horario
from horarioDAO import HorarioDAO
from cliente import Cliente

class View:
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def cliente_listar():
        return clienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
        
    def cliente_inserir(nome, email, fone):
        cliente = cliente(0, nome, email, fone)
        clienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone):
        cliente = cliente(id, nome, email, fone)
        clienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        cliente = cliente(id, "", "", "")
        clienteDAO.excluir(cliente)


    def profissional_listar():
        return profissionalDAO.listar()

    def profissional_listar_id(id):
        return profissionalockDAO.listar_id(id)
        
    def profissional_inserir(nome, email, fone):
        cliente = cliente(0, nome, email, fone)
        clienteDAO.inserir(cliente)

    def profissional_atualizar(id, nome, email, fone):
        cliente = cliente(id, nome, email, fone)
        clienteDAO.atualizar(cliente)

    def profissional_excluir(id):
        cliente = cliente(id, "", "", "")
        clienteDAO.excluir(cliente)    