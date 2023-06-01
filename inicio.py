import streamlit as stm
  
stm.set_page_config(page_title = "inicio")
#stm.title("Centros de Atención al Público")

stm.markdown("<h1 style='text-align: center; color: black;'>Centros de Atención al Público</h1>", unsafe_allow_html=True)

stm.markdown("<h2 style='text-align: center; color: black;'>CAP's</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("afore.jpeg")

with col3:
    st.write(' ')

stm.sidebar.success("Seleccione cualquier página desde aquí")
