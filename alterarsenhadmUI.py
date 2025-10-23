import streamlit as st
from view import View
import time

class AlterarsenhaUI:
    def main():
        op = View.cliente_listar_id(st.session_state["usuario_id"])

        st.header("Alterar senha de admin")
        senha_antiga = st.text_input("Informe a senha atual")
        senha_nova = st.text_input("Informe a nova senha", type="password")
        if st.button("Confirmar"):

            if senha_antiga != op.get_senha():
                st.write("Senha atual incorreta.")

            elif senha_nova == senha_antiga:
                st.write("As senhas têm que ser diferentes.")

            else:
                View.cliente_atualizar(op.get_id(), op.get_nome(), op.get_email(), op.get_fone(), senha_nova)
                st.success("Senha alterada com sucesso.")
                time.sleep(2)
                st.rerun()