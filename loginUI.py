import streamlit as st
from view import View


class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            p = View.profissional_autenticar(email, senha)
            if p:
                st.session_state["usuario_nivel"] = "profissional"
                usuario = p
            if c:
                st.session_state["usuario_nivel"] = "cliente"
                usuario = c
            if c == None and p == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = usuario["id"]
                st.session_state["usuario_nome"] = usuario["nome"]
                st.rerun()