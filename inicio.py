import streamlit as stm
from PIL import Image

stm.set_page_config(page_title = "inicio")
#stm.title("Centros de Atención al Público")

stm.markdown("<h1 style='text-align: center; color: black;'>Centros de Atención al Público</h1>", unsafe_allow_html=True)

stm.markdown("<h2 style='text-align: center; color: black;'>CAP's</h2>", unsafe_allow_html=True)



stm.markdown("")
stm.markdown("")
stm.markdown("")
stm.markdown("")
stm.markdown("")
stm.markdown("")
stm.markdown("")

image = Image.open('afore1.jpg')

stm.image(image, caption='FONDO NACIONAL DE PENSIONES DE LOS TRABAJADORES AL SERVICIO DEL ESTADO')

stm.sidebar.success("Seleccione cualquier página desde aquí")
