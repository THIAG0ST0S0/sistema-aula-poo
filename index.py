from manterclienteUI import ManterClienteUI
from manterserviçoUI import ManterServicoUI
from manterhorarioUI import ManterHorarioUI
from manterprofissionalUI import ManterProfissionalUI


from abrircontaUI import AbrirContaUI
from loginUI import LoginUI
from perfilclienteUI import PerfilClienteUI
from perfilprofissionalUI import PerfilProfissionalUI
from view import View


import streamlit as st


class IndexUI:


    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
        "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()


    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()


    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilProfissionalUI.main()


    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()


    def sidebar():
        if "usuario_id" not in st.session_state: IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            if st.session_state["usuario_nivel"] == "cliente": IndexUI.menu_cliente()
            if st.session_state["usuario_nivel"] == "profissional": IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()


    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()


    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()


IndexUI.main()