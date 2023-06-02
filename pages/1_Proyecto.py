import streamlit as stm

#stm.title("Página 1 de la presentación")

stm.markdown("<h1 style='text-align: center; color: black;'>Estudios de ubicación de CAP’s</h1>", unsafe_allow_html=True)

original_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">1.- Introducción</p>'
stm.markdown(original_title, unsafe_allow_html=True)

#stm.markdown("<h1 style='text-align: justify; color: black;'>"I.-Introducción</h1>", unsafe_allow_html=True)

stm.markdown("<h1 style='text-align: justify; color: black;'>En PENSIONISSSTE es necesario contar con excelentes instalaciones, así como tener el personal capacitado para dar un servicio con la mejor calidad.</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>PENSIONISSSTE pretende realizar un estudio para asentar nuevos Centros de Atención al Público conocidos como CAP’s en el espacio geográfico de las 32 entidades federativas, lo que implicaría que en las ciudades más concurridas, toda persona pueda tener acceso a un CAP cerca de su domicilio o cerca del lugar donde labora; y poder así incorporar a más trabajadores a AFORE PENSIONISSSTE.</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>De igual manera, este estudio permitirá a PENSIONISSSTE saber si un CAP es rentable en su ubicación actual para así poder añadir nuevo personal, servicios y/o tecnologías, en caso contrario, si un CAP no es rentable este debe cerrar.</h1>", unsafe_allow_html=True)

#stm.markdown("<h1 style='text-align: justify; color: black;'>2.-Objetivo</h1>", unsafe_allow_html=True)

original_objetivo = '<p style="font-family:Courier; color:Blue; font-size: 40px;">2.- Objetivo</p>'
stm.markdown(original_objetivo, unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>Realizar trabajo de investigación y aplicar técnicas estadísticas para el análisis de datos que permita tomar las mejores decisiones para ubicar, reubicar o cerrar los Centros de Atención al Público (CAP´s) de PENSIONISSSTE a lo largo del país.</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>3.-Requerimientos</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>a) Localización de cada CAP con latitud y longitud</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>b) Número de personas atendidas de cada CAP por semana o en su caso por mes</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>c) Número de personas que trabajan en cada CAP</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>d) Número de habitantes por municipio</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>e) Ubicar los CAP’s de la competencia</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>f) Número de personas en el municipio con una CI</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>g) Número de personas en el municipio afiliados a AFORE PENSIONISSSTE</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>h) Número de traspasos por entidad</h1>", unsafe_allow_html=True)
stm.markdown("<h1 style='text-align: justify; color: black;'>i) Monto de traspasos</h1>", unsafe_allow_html=True)


stm.sidebar.success("La página se visualiza correctamente")

