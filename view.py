from horario import Horario
from horarioDAO import HorarioDAO
from clienteDAO import ClienteDAO
from profissionalDAO import ProfissionalDAO

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
        return ClienteDAO()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
        
    def cliente_inserir(nome, email, fone):
        cliente = cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone):
        cliente = cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        cliente = cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)


    def profissional_listar():
        return ProfissionalDAO.listar()

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
        
    def profissional_inserir(nome, email, fone):
        cliente = cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    def profissional_atualizar(id, nome, email, fone):
        cliente = cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    def profissional_excluir(id):
        cliente = cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)  

  
    @staticmethod
    def autenticar_cliente(email, senha):
        clientes = ClienteDAO.listar()
        for c in clientes:
            if c.get_email() == email and hasattr(c, "get_senha") and c.get_senha() == senha:
                return c
        return None

    @staticmethod
    def autenticar_profissional(email, senha):
        profissionais = ProfissionalDAO.listar()
        for p in profissionais:
            if hasattr(p, "get_email") and p.get_email() == email and hasattr(p, "get_senha") and p.get_senha() == senha:
                return p
        return None

