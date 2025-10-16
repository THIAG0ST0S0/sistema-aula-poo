from manterclienteUI import ManterClienteUI
from manterserviçoUI import ManterServicoUI
from manterhorarioUI import ManterHorarioUI
import streamlit as st 
from manterclienteUI import ManterClienteUI
from manterprofissionalUI import ManterprofissionalUI
from view import View


class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de profissionais", "Cadastro de Serviços", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de profissionais": ManterprofissionalUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Profissionais", "Cadastro de Serviços", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Profissionais": ManterprofissionalUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()

    def main():
        st.title("Sistema de Agendamento de Serviços")
        st.subheader("Login no Sistema")

        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            cliente = View.autenticar_cliente(email, senha)
            profissional = View.autenticar_profissional(email, senha)

            if cliente:
                st.success(f"Bem-vindo, {cliente.get_nome()} (Cliente)")
                IndexUI.menu_admin()
            elif profissional:
                st.success(f"Bem-vindo, {profissional.get_nome()} (Profissional)")
                IndexUI.menu_admin()
            else:
                st.error("E-mail ou senha incorretos.")    


IndexUI.main()