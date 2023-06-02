import streamlit as stm
import pandas as pd
import plotly.express as px

#stm.title("Página 2 de la presentación")
stm.sidebar.success("La página se visualiza correctamente")


stm.header("Índice resultante por entidad federativa")

_dic = {
'Entidad federativa': ['Nuevo León', 'Chihuahua', 'Baja California', 'Ciudad de México', 'Sinaloa', 'Baja California Sur', 'México', 'Tamaulipas', 'Quintana Roo', 'Sonora', 'Coahuila', 'Jalisco', 'Querétaro', 'Guanajuato', 'Hidalgo', 'Yucatán', 'Aguascalientes', 'Colima', 'Durango', 'San Luis Potosí', 'Michoacán', 'Veracruz', 'Guerrero', 'Oaxaca', 'Nayarit', 'Puebla', 'Morelos', 'Tlaxcala', 'Tabasco', 'Zacatecas', 'Campeche', 'Chiapas'],
'Indice': [99.0, 91.15, 90.6, 90.6, 85.4, 83.3, 77.1, 70.8, 70.3, 69.3, 64.6, 64.6, 63.0, 62.5,62.0, 60.9, 58.9, 55.2, 54.7, 53.6, 51.6, 51.6, 51.0, 49.5, 45.8, 43.8, 41.1, 40.1, 34.4, 33.3, 32.8, 22.4]
}

_df = pd.DataFrame(_dic)

load = stm.button('Cargar datos')


if "load_state" not in stm.session_state:
    
     stm.session_state.load_state = False


if load or stm.session_state.load_state:

    stm.session_state.load_state = True
    stm.write(_df)

opt = stm.radio('Tipo de gráfica :', ['Barras', 'Circular'])

if opt == 'Barras':
     fig = px.bar(_df, x = 'Entidad federativa', y = 'Indice', title = 'Gráfico de barras')
     stm.plotly_chart(fig)
else:
     fig = px.pie(_df, names = 'Entidad federativa', values = 'Indice', title = 'Gráfico circular')
     stm.plotly_chart(fig)
