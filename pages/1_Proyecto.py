import streamlit as stm

#stm.title("Página 1 de la presentación")

stm.markdown("<h1 style='text-align: center; color: black;'>Estudio de ubicación de CAP’s</h1>", unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

original_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">1.- Introducción</p>'
stm.markdown(original_title, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")


a = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">En PENSIONISSSTE es necesario contar con excelentes instalaciones y personal capacitado para dar un servicio con la mejor calidad en la administración de fondos para el retiro de los trabajadores.</p>'
stm.markdown(a, unsafe_allow_html=True)

b = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">Por ello, PENSIONISSSTE pretende realizar un estudio para asentar nuevos Centros de Atención al Público conocidos como CAP’s en el espacio geográfico de las 32 entidades federativas bien ubicados, lo que implicaría que todo trabajador pueda tener acceso a un CAP cerca de su domicilio o lugar donde labora; y poder así incorporar a quienes decidan tener su afore en PENSIONISSSTE.</p>'
stm.markdown(b, unsafe_allow_html=True)

c = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">De igual manera, este estudio permitirá a PENSIONISSSTE concluir si un CAP es rentable en su ubicación actual y añadir nuevos servicios y tecnologías, personal etc. En caso contrario se debe cerrar el CAP. </p>'
stm.markdown(c, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

original_objetivo = '<p style="font-family:Courier; color:Blue; font-size: 40px;">2.- Objetivos</p>'
stm.markdown(original_objetivo, unsafe_allow_html=True)

#d = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">Realizar trabajo de investigación y aplicar técnicas estadísticas para el análisis de datos que permita tomar las mejores decisiones para ubicar, reubicar o cerrar los Centros de Atención al Público (CAP´s) de PENSIONISSSTE a lo largo del país.</p>'
#stm.markdown(d, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")


p = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">i)	Implementar una herramienta cuantitativa utilizando técnicas de Geomarketing y Machine Learnig con el fin de identificar oportunidades de negocio para afore PENSIONISSSTE y contribuir a la ubicación de los CAP´s, seleccionando regiones potenciales de alta demanda de trabajadores en el país.</p>' 
stm.markdown(p, unsafe_allow_html=True)

q = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">ii)	Con esta herramienta tomar las mejores decisiones para reubicar o cerrar los Centros de Atención al Público CAP´s que no son rentables en sus puntos georreferenciados.</p>' 
stm.markdown(q, unsafe_allow_html=True)

r = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">iii)	Elaborar un mapa en QGIS con las ubicaciones actuales de los CAP´s de PENSIONISSSTE.</p>' 
stm.markdown(r, unsafe_allow_html=True)

s = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">iv)	Elaborar un mapa en QGIS con las ubicaciones actuales de las afores restantes.</p>' 
stm.markdown(s, unsafe_allow_html=True)

t = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">v)	Cruzar la información de los puntos iii) y iv) para verificar los resultados obtenidos en el punto i) y ii).</p>' 
stm.markdown(t, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

original_requerimientos = '<p style="font-family:Courier; color:Blue; font-size: 40px;">3.- Requerimientos</p>'
stm.markdown(original_requerimientos, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

#stm.markdown("<h1 style='text-align: justify; color: black;'>3.-Requerimientos</h1>", unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")

u = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">Para llevar a cabo este estudio, se necesitan las siguientes bases de datos que contengan la lista de variables mencionadas a continuación. Contar con estos datos reales, nos dará la pauta para tener el modelo óptimo cuantitativo que nos indicará los puntos georreferenciados y con ello, la presencia estatal y municipal de los CAP´s de afore PENSIONISSSTE. La ubicación de los CAP´s es decisivo para que afore PENSIONISSSTE absorba más afiliados.</p>' 
stm.markdown(u, unsafe_allow_html=True)

stm.markdown("")
stm.markdown("")
stm.markdown("")


#e = '<p style=style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">a) Localización de cada CAP con latitud y longitud</p>'  
#stm.markdown(e, unsafe_allow_html=True)

e = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">a) Localización de cada CAP con latitud y longitud</p>' 
stm.markdown(e, unsafe_allow_html=True)

f = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">b) Número de personas atendidas en cada CAP por semana o en su caso por mes</p>' 
stm.markdown(f, unsafe_allow_html=True)

g = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">c) Número de personas que trabajan en cada CAP</p>' 
stm.markdown(g, unsafe_allow_html=True)

h = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">d) Número de traspasos por entidad</p>' 
stm.markdown(h, unsafe_allow_html=True)

i = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">e) Monto de traspasos</p>'
stm.markdown(i, unsafe_allow_html=True)

j = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">f) Número de habitantes por municipio</p>' 
stm.markdown(j, unsafe_allow_html=True)

k = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">g) Número de personas en el municipio con una Cuenta Individual CI</p>'
stm.markdown(k, unsafe_allow_html=True)

l = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">h) Número de personas en el municipio afiliados a AFORE PENSIONISSSTE</p>'
stm.markdown(l, unsafe_allow_html=True)

m = '<p style="text-align: justify; font-family:Courier; color:Black; font-size: 30px;">i) Ubicar los CAP’s de la competencia</p>'
stm.markdown(m, unsafe_allow_html=True)

stm.sidebar.success("La página se visualiza correctamente")

