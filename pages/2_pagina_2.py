import streamlit as stm
import pandas as pd
import plotly.express as px

#stm.title("Página 2 de la presentación")
stm.sidebar.success("Actualmente visualizas la página 2")


stm.header("Fruit List")

_dic = {
'Name': ['Mango', 'Apple', 'Banana'],
'Quantity': [45, 38, 90]
}

_df = pd.DataFrame(_dic)

load = stm.button('Load Data')


if "load_state" not in stm.session_state:
    
     stm.session_state.load_state = False


if load or st.session_state.load_state:

    stm.session_state.load_state = True
    stm.write(_df)

opt = stm.radio('Plot type :', ['Bar', 'Pie'])

if opt == 'Bar':
     fig = px.bar(_df, x = 'Name', y = 'Quantity', title = 'Bar Chart')
     st.plotly_chart(fig)
else:
     fig = px.pie(_df, names = 'Name', values = 'Quantity', title = 'Pie Chart')
     stm.plotly_chart(fig)
