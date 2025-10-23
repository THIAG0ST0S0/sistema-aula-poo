import streamlit as st
from view import View
import time

class ConfirmarServicoUI:
    def main():
        st.header("Minha Agenda")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        horarios = View.horario_listar()

        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            h_validos = []
            for obj in horarios:
                if not obj.get_confirmado() and obj.get_id_profissional() == op.get_id(): h_validos.append(obj)

            horario = st.selectbox("Informe o horário", h_validos)
            cliente = st.selectbox("Cliente", [horario], disabled=True)

            if st.button("Confirmar"):
                horario.set_confirmado(True)
                time.sleep(2)
                st.rerun()

