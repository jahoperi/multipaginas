import streamlit as stm
import pandas as pd
import plotly.express as px
  
stm.title("Página 1 de la presentación")
stm.sidebar.success("Actualmente visualizas la página 1")

st.header("Fruit List")

_dic = {
'Name': ['Mango', 'Apple', 'Banana'],
'Quantity': [45, 38, 90]
}

_df = pd.Dataframe(_dic)

load = st.button('Load Data')


if "load_state" not in st.session_state:
    st.session_state.load_state = False

if load or st.session_state.load_state:
    st.session_state.load_state = True
    st.write(_df)

    opt = st.radio('Plot type :', ['Bar', 'Pie'])
    if opt == 'Bar':
           fig = px.Bar(_df, x = 'Name', y = 'Quantity', title = 'Bar Chart')
           st.plotly_chart(fig)
    else:
           fig = px.pie(_df, x = 'Name', y = 'Quantity', title = 'Pie Chart')
           st.plotly_chart(fig)
