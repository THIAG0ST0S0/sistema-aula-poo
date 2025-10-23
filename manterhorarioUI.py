import streamlit as st
import pandas as pd
from view import View
import time
from datetime import datetime

class ManterHorarioUI:
  def main():
    st.header("Cadastro de Horários")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

    with tab1: ManterHorarioUI.listar()
    with tab2: ManterHorarioUI.inserir()
    with tab3: ManterHorarioUI.atualizar()
    with tab4: ManterHorarioUI.excluir()

  def listar():
    horarios = View.horario_listar()
    horarios.sort(key=lambda x: x.get_data())
    
    if len(horarios) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in horarios:
        cliente = View.cliente_listar_id(obj.get_id_cliente())
        servico = View.servico_listar_id(obj.get_id_servico())
        profissional = View.profissional_listar_id(obj.get_id_profissional())

        dic.append({
          "id": obj.get_id(),
          "data": obj.get_data().strftime("%d/%m/%Y %H:%M"),
          "confirmado": obj.get_confirmado(),
          "cliente": cliente.get_nome() if cliente else "Nenhum",
          "serviço": servico.get_descricao() if servico else "Nenhum",
          "profissional": profissional.get_nome() if profissional else "Nenhum"
        })
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    data_str = st.text_input("Informe a data e horário (dd/mm/aaaa HH:MM)")
    clientes = [None] + View.cliente_listar()
    servicos = [None] + View.servico_listar()
    profissionais = [None] + View.profissional_listar()

    cliente = st.selectbox("Selecione o cliente (opcional)", clientes, format_func=lambda x: x.get_nome() if x else "Nenhum")
    servico = st.selectbox("Selecione o serviço (opcional)", servicos, format_func=lambda x: x.get_descricao() if x else "Nenhum")
    profissional = st.selectbox("Selecione o profissional (opcional)", profissionais, format_func=lambda x: x.get_nome() if x else "Nenhum")
    
    if st.button("Inserir"):
      try:
        data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        id_cliente = cliente.get_id() if cliente else 0
        id_servico = servico.get_id() if servico else 0
        id_profissional = profissional.get_id() if profissional else 0
        
        View.horario_inserir(data, False, id_cliente, id_servico, id_profissional)
        st.success("Horário inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.error("Formato de data inválido. Use dd/mm/aaaa HH:MM")
      except Exception as e:
        st.error(f"Ocorreu um erro: {e}")


  def atualizar():
    horarios = View.horario_listar()
    if len(horarios) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      horarios.sort(key=lambda x: x.get_data())
      
      clientes = View.cliente_listar()
      servicos = View.servico_listar()
      profissionais = View.profissional_listar() 

      op = st.selectbox("Atualização de Horários", horarios)
      
      data = st.text_input("Informe a nova data e horário", op.get_data().strftime("%d/%m/%Y %H:%M"))
      confirmado = st.checkbox("Confirmado", op.get_confirmado())

      idx_cliente = next((i for i, c in enumerate(clientes) if c.get_id() == op.get_id_cliente()), None)
      idx_servico = next((i for i, s in enumerate(servicos) if s.get_id() == op.get_id_servico()), None)
      idx_profissional = next((i for i, p in enumerate(profissionais) if p.get_id() == op.get_id_profissional()), None) 

      cliente = st.selectbox("Informe o novo cliente", clientes, index=idx_cliente, format_func=lambda x: x.get_nome())
      servico = st.selectbox("Informe o novo serviço", servicos, index=idx_servico, format_func=lambda x: x.get_descricao())
      profissional = st.selectbox("Informe o novo profissional", profissionais, index=idx_profissional, format_func=lambda x: x.get_nome()) # Adicionado

      if st.button("Atualizar"):
        try:
          id_cliente = cliente.get_id() if cliente else 0
          id_servico = servico.get_id() if servico else 0
          id_profissional = profissional.get_id() if profissional else 0 
          data_dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
          
          View.horario_atualizar(op.get_id(), data_dt, confirmado, id_cliente, id_servico, id_profissional) 
          st.success("Horário atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except ValueError:
          st.error("Formato de data inválido. Use dd/mm/aaaa HH:MM")
        except Exception as e:
          st.error(f"Ocorreu um erro: {e}")

  def excluir():
    horarios = View.horario_listar()
    if len(horarios) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      horarios.sort(key=lambda x: x.get_data())
      
      op = st.selectbox("Exclusão de Horários", horarios)
      if st.button("Excluir"):
        View.horario_excluir(op.get_id())
        st.success("Horário excluído com sucesso")
        time.sleep(2)
        st.rerun()