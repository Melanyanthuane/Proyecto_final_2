import streamlit as st

st.write("""
## TABLA DE DATOS
""")

#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd

# nos ayuda a realizar graficas de calor
import seaborn as sns

# otra manera de grafic
import matplotlib.pyplot as plt

#archivo CSV separado por comas
data = pd.read_csv('Formulario PIF.csv')

#leer  lineas
data


st.write("""
## TABLA DE DATOS CON IMPUTACIÓN EJECUTADA
""")

data.describe()
data["Desierto la Tatacoa"] = data["Desierto la Tatacoa"].replace(np.nan, 3)
data["Chichen Itza"] = data["Chichen Itza"].replace(np.nan, 4)
data["Laguna Azul"] = data["Laguna Azul"].replace(np.nan, 4)
data[" Angkor Wat"] = data[" Angkor Wat"].replace(np.nan, 4)
data_1=data
data_1


st.write("""
## TABLA DE CORRELACIÓN PEARSON (PANDAS)
""")


n = data[data.columns[1:]].to_numpy()
m = data[data.columns[0]].to_numpy()

n.T


respuestas = pd.DataFrame(n.T, columns = m)

panda = respuestas.corr()


st.write(""" ## GRAFICA DE CALOR POR PANDAS """)
st.write(""" ![imagen1.png](https://i.ibb.co/pL9vnHh/Whats-App-Image-2022-12-19-at-9-53-36-AM.jpg) """)


