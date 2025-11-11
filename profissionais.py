import streamlit as st
from view import View

class exibir_profissionais:
    def main():
            profissionais = View.profissional_listar()
            st.title("👥 Profissionais disponíveis")
            for i in profissionais:
                st.subheader(i.get_nome())
                st.write("biografia:", i.get_bio())
                st.write("conselho:", i.get_conselho())
                st.divider()
                  