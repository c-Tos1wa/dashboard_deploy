import pandas as pd
import plotly.express as px
import streamlit as st

db = pd.read_csv("/home/cristoshie/create_dashboard/database/vendas.csv")

st.title("Sistema de gestão de vendas")

# formulário de cadastro em um sidebar
st.sidebar.write("## Cadastro de Vendas")
employers_list = ["Ana", "Bruno", "Carla"]
products_list = ["Celular", "Fone", "Notebook"]
date = st.sidebar.date_input("Data")
employer = st.sidebar.selectbox("Vendedor", employers_list)
product = st.sidebar.selectbox("Produto", products_list)
quantity = st.sidebar.number_input("Quantidade", step = 1)
value = st.sidebar.number_input("Valor")
button = st.sidebar.button("cadastrar")

if button:
    if quantity == 0:
        st.warning("Cadastro incompleto, por favor, selecionar Quantidade")
    else:
        new_record = [date, employer, product, quantity, value]
        db.loc[len(db)] = new_record
        db.to_csv("/home/cristoshie/create_dashboard/database/vendas.csv", index = False)
        st.success("Venda cadastrada!")

# dataframe dos dados da tabela
st.write("## Vendas cadastradas")
st.dataframe(db)

# métricas e gráficos
st.write("## Dashboard")
total = db["valor"].sum()
st.metric("Faturamento Total", f"R${total:.2f}")

bar_chart = px.bar(
    db,
    x = "vendedor",
    y = "valor",
    color = "produto",
    #title = "Gráfico de vendas por vendedor e produto"
)
bar_chart.update_layout(
    title_text = "Gráfico de Vendas por vendedor e por produtos",
    xaxis_title_text = "",
    yaxis_title_text = "")
st.plotly_chart(bar_chart)

pie_chart = px.pie(
    db, 
    names = "produto",
    values = "valor",
    hole = 0.4,
    title = "Gráfico da porcentagem dos produtos nas vendas"
)
st.plotly_chart(pie_chart)
