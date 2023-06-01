import streamlit as stm
import pandas as pdm
import plotly.express as pxm
  
stm.title("Página 1 de la presentación")
stm.sidebar.success("Actualmente visualizas la página 1")

stm.header("Fruit List")

_dict = {
'Name': ['Mango', 'Apple', 'Banana'],
'Quantity': [45, 38, 90]
}

_df = pdm.Dataframe(_dict)

load = stm.button('Load Data')


if "load_state" not in st.session_state:
    stm.session_state.load_state = False

if load or st.session_state.load_state:
    stm.session_state.load_state = True
    stm.write(_df)

    opt = stm.radio('Plot type :', ['Bar', 'Pie'])
    if opt == 'Bar':
           fig = pxm.Bar(_df, x = 'Name', y = 'Quantity', title = 'Bar Chart')
           stm.plotly_chart(fig)
    else:
           fig = pxm.pie(_df, x = 'Name', y = 'Quantity', title = 'Pie Chart')
           stm.plotly_chart(fig)
