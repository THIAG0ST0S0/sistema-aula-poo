from manterclienteUI import ManterClienteUI
from manterserviçoUI import ManterServicoUI
from manterhorarioUI import ManterHorarioUI
import streamlit as st 
from manterclienteUI import ManterClienteUI
from manterprofissionalUI import ManterprofissionalUI


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


IndexUI.main()