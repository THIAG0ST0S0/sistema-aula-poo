import streamlit as st
from view import View
import pandas as pd

class MinhaAgendaUI:
    def main():
        st.header("Minha Agenda")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        horarios = View.horario_listar()

        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()

                if obj.get_id_profissional() == op.get_id():
                    dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "serviço" : servico})


            df = pd.DataFrame(dic)
            st.dataframe(df)