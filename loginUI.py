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
      
      usuario = None
      
    
      if c and c.get_email() == "admin":
        st.session_state["usuario_nivel"] = "admin"
        usuario = c
    
      elif p:
        st.session_state["usuario_nivel"] = "profissional"
        usuario = p
    
      elif c:
        st.session_state["usuario_nivel"] = "cliente"
        usuario = c
      
      if usuario is None:
        st.error("E-mail ou senha inválidos")
      else:
        st.session_state["usuario_id"] = usuario.get_id()
        st.session_state["usuario_nome"] = usuario.get_nome()
        st.rerun()