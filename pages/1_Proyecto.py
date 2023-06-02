import streamlit as stm

#stm.title("Página 1 de la presentación")

stm.markdown("<h1 style='text-align: center; color: black;'>Estudios de ubicación de CAP’s</h1>", unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

original_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">1.- Introducción</p>'
stm.markdown(original_title, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")


a = '<p style="text-align: justify","font-family:Courier; color:Black; font-size: 30px;">En PENSIONISSSTE es necesario contar con excelentes instalaciones, así como tener el personal capacitado para dar un servicio con la mejor calidad.</p>'
stm.markdown(a, unsafe_allow_html=True)

b = '<p style="font-family:Courier; color:Black; font-size: 30px;">PENSIONISSSTE pretende realizar un estudio para asentar nuevos Centros de Atención al Público conocidos como CAP’s en el espacio geográfico de las 32 entidades federativas, lo que implicaría que en las ciudades más concurridas, toda persona pueda tener acceso a un CAP cerca de su domicilio o del lugar donde labora; y poder así incorporar a más trabajadores a AFORE PENSIONISSSTE.</p>'
stm.markdown(b, unsafe_allow_html=True)

c = '<p style="font-family:Courier; color:Black; font-size: 30px;">De igual manera, este estudio permitirá a PENSIONISSSTE saber si un CAP es rentable en su ubicación actual para así poder añadir nuevo personal, servicios y/o tecnologías, en caso contrario, si un CAP no es rentable este debe cerrar.</p>'
stm.markdown(c, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

original_objetivo = '<p style="font-family:Courier; color:Blue; font-size: 40px;">2.- Objetivo</p>'
stm.markdown(original_objetivo, unsafe_allow_html=True)

d = '<p style="font-family:Courier; color:Black; font-size: 30px;">Realizar trabajo de investigación y aplicar técnicas estadísticas para el análisis de datos que permita tomar las mejores decisiones para ubicar, reubicar o cerrar los Centros de Atención al Público (CAP´s) de PENSIONISSSTE a lo largo del país.</p>'
stm.markdown(d, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")


original_requerimientos = '<p style="font-family:Courier; color:Blue; font-size: 40px;">3.- Requerimientos</p>'
stm.markdown(original_requerimientos, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

#stm.markdown("<h1 style='text-align: justify; color: black;'>3.-Requerimientos</h1>", unsafe_allow_html=True)

e = '<p style="font-family:Courier; color:Black; font-size: 30px;">a) a) Localización de cada CAP con latitud y longitud</p>'  
stm.markdown(e, unsafe_allow_html=True)

f = '<p style="font-family:Courier; color:Black; font-size: 30px;">b) Número de personas atendidas en cada CAP por semana o en su caso por mes</h1></p>' 
stm.markdown(f, unsafe_allow_html=True)

g = '<p style="font-family:Courier; color:Black; font-size: 30px;">c) Número de personas que trabajan en cada CAP</h1></p>' 
stm.markdown(g, unsafe_allow_html=True)

h = '<p style="font-family:Courier; color:Black; font-size: 30px;">d) Número de traspasos por entidad</h1></p>' 
stm.markdown(h, unsafe_allow_html=True)

i = '<p style="font-family:Courier; color:Black; font-size: 30px;">e) Monto de traspasos</h1></p>'
stm.markdown(i, unsafe_allow_html=True)

j = '<p style="font-family:Courier; color:Black; font-size: 30px;">f) Número de habitantes por municipio</h1></p>' 
stm.markdown(j, unsafe_allow_html=True)

k = '<p style="font-family:Courier; color:Black; font-size: 30px;">g) Número de personas en el municipio con una Cuenta Individual CI</h1></p>'
stm.markdown(k, unsafe_allow_html=True)

l = '<p style="font-family:Courier; color:Black; font-size: 30px;">h) Número de personas en el municipio afiliados a AFORE PENSIONISSSTE</h1></p>'
stm.markdown(l, unsafe_allow_html=True)

m = '<p style="font-family:Courier; color:Black; font-size: 30px;">i) Ubicar los CAP’s de la competencia</h1></p>'
stm.markdown(m, unsafe_allow_html=True)

stm.sidebar.success("La página se visualiza correctamente")

