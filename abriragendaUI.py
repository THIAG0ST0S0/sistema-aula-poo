import streamlit as st
from view import View
import datetime
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        op = View.profissional_listar_id(st.session_state["usuario_id"])
        data = st.text_input("Informe a data (dd/mm/yyyy)") 
        hora_inicial = st.text_input("Informe o horário inicial no formato HH:MM")
        hora_final = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")

        if st.button("Abrir Agenda"):
            id = op.get_id()

            hora_final = datetime.datetime.strptime(data + " " + hora_final, "%d/%m/%Y %H:%M")
            horario = datetime.datetime.strptime(data + " " + hora_inicial, "%d/%m/%Y %H:%M")
            intervalo = datetime.timedelta(minutes=int(intervalo))

            while horario <= hora_final:
                View.horario_inserir(horario, False, None, None, id)
                horario += intervalo

            st.success("Agenda aberta com sucesso")
            time.sleep(2)
            st.rerun()