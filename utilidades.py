import streamlit as st
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def generarMenu():
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            image = Image.open('media/Logo_WattData.jpeg')
            st.image(image, use_container_width=False)
        with col2: 
            st.header('Movilidad Sustentable')

        st.page_link('app.py', label='Inicio')
        st.page_link('pages/Vehiculos_electricos.py', label='Vehículos Eléctricos')
        st.page_link('pages/calidad_aire.py', label='Calidad Aire')
        st.page_link('pages/resultados_modelo.py', label='Resultados Modelos')
        



# Función vehiculos Electricos

def modelo_Veh_Ele(df1):
    st.markdown('## Datos Vehiculos Electricos')
    st.write(df1.head())
    st.subheader('Informacion Inicial de la Fuente')
    st.write(df1.describe())
    # Mostrar Grafica
    figsize = (12, 1.2 * len(df1['COMBUSTIBLE'].unique()))
    plt.figure(figsize=figsize)
    sns.violinplot(df1, x='AÑO_REGISTRO', y='COMBUSTIBLE', inner='box', palette='Dark2')
    sns.despine(top=True, right=True, bottom=True, left=True)     
    st.pyplot()  


    

def modelo_cal_air(df2):
    st.markdown('## Datos calidad del Aire')
    st.write(df2.head())
    st.subheader('Informacion Inicial de la Fuente')
    st.write(df2.describe())
    # Mostrar Grafica
    plt.figure(figsize=(10,6))
    sns.barplot(x="Nombre del Departamento", y="Promedio", data=df2, palette="viridis")
    plt.xlabel("Nombre del Departamento")
    plt.ylabel("Promedio")
    plt.title("Promedio de contaminacion por departamento")
    plt.xticks(rotation=90)
    st.pyplot()