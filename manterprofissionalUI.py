import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfissionalUI:
  def main():
    st.header("Cadastro de Profissionais")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

    with tab1: ManterProfissionalUI.listar()
    with tab2: ManterProfissionalUI.inserir()
    with tab3: ManterProfissionalUI.atualizar()
    with tab4: ManterProfissionalUI.excluir()

  def listar():
    profissionais = View.profissional_listar()
    if len(profissionais) == 0:
      st.write("Nenhum profissional cadastrado")
    else:
      list_dic = []
      for obj in profissionais:
          list_dic.append({
              "id": obj.get_id(),
              "nome": obj.get_nome(),
              "especialidade": obj.get_especialidade(),
              "conselho": obj.get_conselho(),
              "email": obj.get_email()
          })
      df = pd.DataFrame(list_dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    especialidade = st.text_input("Informe a especialidade")
    conselho = st.text_input("Informe o conselho")
    email = st.text_input("Informe o e-mail") 
    senha = st.text_input("Informe a senha", type="password") 
    
    if st.button("Inserir"):
      if not nome or not email or not senha:
          st.warning("Nome, e-mail e senha são obrigatórios.")
      else:
          View.profissional_inserir(nome, especialidade, conselho, email, senha)
          st.success("Profissional inserido com sucesso")
          time.sleep(2)
          st.rerun()
      try:
        View.profissional_inserir(...)
        st.success("profissional criado com sucesso!")
      except Exception as e:
        st.error(str(e))

  def atualizar():
    profissionais = View.profissional_listar()
    if len(profissionais) == 0:
      st.write("Nenhum profissional cadastrado")
    else:
      op = st.selectbox("Atualização de Profissionais", profissionais, format_func=lambda x: x.get_nome())
      
      nome = st.text_input("Novo nome", op.get_nome())
      especialidade = st.text_input("Nova especialidade", op.get_especialidade()) 
      conselho = st.text_input("Novo conselho", op.get_conselho())
      email = st.text_input("Novo e-mail", op.get_email())
      senha = st.text_input("Nova senha", op.get_senha(), type="password") 
      
      if st.button("Atualizar"):
        if not nome or not email or not senha:
            st.warning("Nome, e-mail e senha são obrigatórios.")
        else:
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Profissional atualizado com sucesso")
            time.sleep(2)
            st.rerun()

  def excluir():
    profissionais = View.profissional_listar()
    if len(profissionais) == 0:
      st.write("Nenhum profissional cadastrado") 
    else:
      op = st.selectbox("Exclusão de Profissionais", profissionais, format_func=lambda x: x.get_nome()) # Corrigido
      if st.button("Excluir"):
        id = op.get_id()
        View.profissional_excluir(id)
        st.success("Profissional excluído com sucesso")
        time.sleep(2)
        st.rerun()