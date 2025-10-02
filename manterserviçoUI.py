class ManterServicoUI:
    def __init__(self, servico_dao):
        self.servico_dao = servico_dao

    def menu_principal(self):
        while True:
            print("\n--- Manter Cadastro de Serviços ---")
            print("1. Incluir Serviço")
            print("2. Listar Serviços")
            print("3. Alterar Serviço")
            print("4. Excluir Serviço")
            print("5. Voltar ao Menu Principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self._incluir_servico()
            elif opcao == '2':
                self._listar_servicos()
            elif opcao == '3':
                self._alterar_servico()
            elif opcao == '4':
                self._excluir_servico()
            elif opcao == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def _incluir_servico(self):
        print("\n--- Incluir Novo Serviço ---")
        try:
            descricao = input("Descrição do Serviço: ")
            valor = float(input("Valor do Serviço (Ex: 150.50): "))
            novo_servico = Servico(id=0, descricao=descricao, valor=valor)
            self.servico_dao.insert(novo_servico)
            
            print(f"\n Serviço incluído com sucesso! ID: {novo_servico.id}")
        except ValueError as e:
            print(f" Erro na entrada de dados: {e}")

    def _listar_servicos(self):
        servicos = self.servico_dao.select_all()
        if not servicos:
            print("\nNenhum serviço cadastrado.")
            return

        print("\n--- Lista de Serviços ---")
        for servico in servicos:
            print(servico)

    def _alterar_servico(self):
        self._listar_servicos()
        if not self.servico_dao.select_all():
            return
            
        try:
            servico_id = int(input("\nDigite o ID do serviço para alterar: "))
            servico = self.servico_dao.select_by_id(servico_id)
            
            if servico:
                print(f"Serviço atual: {servico}")
                nova_descricao = input(f"Nova descrição (atual: {servico.descricao}, deixe vazio para manter): ")
                novo_valor_str = input(f"Novo valor (atual: {servico.valor}, deixe vazio para manter): ")
                
                if nova_descricao:
                    servico.descricao = nova_descricao
                
                if novo_valor_str:
                    servico.valor = float(novo_valor_str)
                    
                self.servico_dao.update(servico)
                print(f" Serviço {servico_id} alterado com sucesso.")
            else:
                print(f" Serviço com ID {servico_id} não encontrado.")
        except ValueError as e:
            print(f" Erro: Entrada inválida ou {e}")

    def _excluir_servico(self):
        self._listar_servicos()
        if not self.servico_dao.select_all():
            return
            
        try:
            servico_id = int(input("\nDigite o ID do serviço para excluir: "))
            
            if self.servico_dao.delete(servico_id):
                print(f" Serviço {servico_id} excluído com sucesso.")
            else:
                print(f" Serviço com ID {servico_id} não encontrado.")
        except ValueError:
            print(" Erro: ID inválido.")



if __name__ == '__main__':
    servico_dao = ServicoDAO()
    manter_servico_ui = ManterServicoUI(servico_dao)
    
    print("--- Inicializando o Sistema de Agendamento ---")
    manter_servico_ui.menu_principal() 
    print("--- Fim da Simulação ---")