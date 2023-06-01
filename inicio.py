import streamlit as stm
  
stm.set_page_config(page_title = "inicio")
#stm.title("Centros de Atención al Público")

stm.markdown("<h1 style='text-align: center; color: black;'>Centros de Atención al Público</h1>", unsafe_allow_html=True)

stm.markdown("<h2 style='text-align: center; color: black;'>CAP's</h2>", unsafe_allow_html=True)

from PIL import Image

image = Image.open('afore1.jpg')

stm.image(image, caption='Sunrise by the mountains')

stm.sidebar.success("Seleccione cualquier página desde aquí")
