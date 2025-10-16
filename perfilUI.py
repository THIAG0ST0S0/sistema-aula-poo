import streamlit as st
from view import View

class PerfilUI:
    def main(usuario, tipo):
        st.header("Meu Perfil")

        nome = st.text_input("Nome", usuario.get_nome())
        email = st.text_input("E-mail", usuario.get_email())
        fone = st.text_input("Fone", usuario.get_fone() if tipo == "cliente" else "")
        senha = st.text_input("Senha", usuario.get_senha(), type="password")

        if st.button("Salvar Alterações"):
            if tipo == "cliente":
                View.cliente_atualizar(usuario.get_id(), nome, email, fone, senha)
            else:
                View.profissional_atualizar(usuario.get_id(), nome, email, senha)
            st.success("Dados atualizados com sucesso!")