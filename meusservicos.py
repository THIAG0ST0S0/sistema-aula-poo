import streamlit as st
from view import View
import pandas as pd

class MeusservicosUI:
    def main():
        st.header("Minha Agenda")
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        horarios = View.horario_listar()

        if len(horarios) == 0: st.write("Nenhum serviço cadastrado")
        else:
            dic = []
            for obj in horarios:
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                servico = View.servico_listar_id(obj.get_id_servico())
                if servico != None: servico = servico.get_descricao()

                if obj.get_id_cliente() == op.get_id():
                    dic.append({"id" : obj.get_id_servico(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "serviço" : servico, "profissional": profissional.get_nome()})


            df = pd.DataFrame(dic)
            st.dataframe(df)