import streamlit as st

st.write("""###  ¿Se valido o no los resultados? """)

st.write("""Sí se validaron los resultados. """)

st.write("""###  Los resultados validados son: """)
st.write("""Al hallar la "matriz de correlación" y compararlo con la validación de los resultados hechos manualmente, ambos nos brindan los mismos resultados. Otra manera de saber los resultados validados es comparando las graficas de calor de ambas matrices. """)

st.write("""###   ¿Es efectivo el método de correlación de Pearson?""")
st.write("""Sí es efectivo usar el método de correlación de Pearson porque los resultados siempre tiene un valor entre -1 y 1 al igual que la covarianza, si fuera 1 la correlación de pearson seria una correlación irrealmente perfecta  """)

st.write("""###   Correlación de Pearson y Regresión Lineal, ¿cuál es su relación? """)
st.write(""" La correlación lineal nos permite conocer la relación entre dos variables y la correlación de person nos permite calcular la relación entre dos variablessiempre que sean variables cuantitativas y continuas.  """)
