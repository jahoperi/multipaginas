import streamlit as stm
import pandas as pd
import plotly.express as px

#stm.title("Página 2 de la presentación")
stm.sidebar.success("Actualmente visualizas la página 2")


stm.header("Fruit List")

_dic = {
'Name': ['Nuevo León', 'Chihuahua', 'Baja California', 'Ciudad de México', 'Sinaloa', 'Baja California Sur', 'México', 'Tamaulipas', 'Quintana Roo', 'Sonora'. 'Coahuila', 'Jalisco', 'Querétaro', 'Guanajuato', 'Hidalgo', 'Yucatán', 'Aguascalientes', 'Colima', 'Durango', 'San Luis Potosí', 'Michoacán', 'Veracruz', 'Guerrero', 'Oaxaca', 'Nayarit', 'Puebla', 'Morelos', 'Tlaxcala', 'Tabasco', 'Zacatecas', 'Campeche', 'Chiapas'],
'Quantity': [45, 38, 90]
}

_df = pd.DataFrame(_dic)

load = stm.button('Load Data')


if "load_state" not in stm.session_state:
    
     stm.session_state.load_state = False


if load or stm.session_state.load_state:

    stm.session_state.load_state = True
    stm.write(_df)

opt = stm.radio('Plot type :', ['Bar', 'Pie'])

if opt == 'Bar':
     fig = px.bar(_df, x = 'Name', y = 'Quantity', title = 'Bar Chart')
     stm.plotly_chart(fig)
else:
     fig = px.pie(_df, names = 'Name', values = 'Quantity', title = 'Pie Chart')
     stm.plotly_chart(fig)
