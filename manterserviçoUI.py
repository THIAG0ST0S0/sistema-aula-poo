import streamlit as st
import pandas as pd
import time
from view import View

class ManterServicoUI:

    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])

        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        serviços = View.serviço_listar()
        if len(serviços) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in serviços: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df) 

    def inserir():
        id = st.text_input("Informe o id")
        descriçao = st.text_input("adicione uma descrição")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.serviço_inserir(id, descriçao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()  

    def atualizar():
        serviços = View.serviço_listar()
        if len(serviços) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox ("Atualização de Serviços")
            id = st.text_input("id do serviço", op.get_nome())
            descriçao = st.text_input("descrição", op.get_email())
            valor = st.text_input("valor do serviço", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.serviço_atualizar(id, descriçao, valor)
                st.success("Serviço atualizado com sucesso")

    def excluir():
        serviços = View.serviço_listar()
        if len(serviços) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviço", serviços)
            if st.button("Excluir"):
                id = op.get_id()
                View.serviço_excluir(id)
                st.success("Serviço excluído com sucesso")