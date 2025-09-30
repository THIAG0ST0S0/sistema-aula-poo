import streamlit as st
import pandas as pd
import time
from views 
import View

class manterprofissionalUI:

    def main():
        st.header("Cadastro de profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])

        with tab1: manterprofissionalUI.listar()
        with tab2: manterprofissionalUI.inserir()
        with tab3: manterprofissionalUI.atualizar()
        with tab4: manterprofissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df) 

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho)
            st.success("profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()  

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissionais", profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Nova especialidade", op.get_email())
            conselho = st.text_input("Novo conselho", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho)
                st.success("profissional atualizado com sucesso")

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("profissional excluído com sucesso")