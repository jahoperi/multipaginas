import streamlit as stm
  
stm.set_page_config(page_title = "inicio")
stm.title("Centros de Atención al Público")

stm.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

stm.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

stm.sidebar.success("Seleccione cualquier página desde aquí")
