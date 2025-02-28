import pandas as pd
import utilidades as util
import streamlit as st
import statsmodels.api as sm
from matplotlib import pyplot as plt

util.generarMenu()

st.title('Modelos')
df = pd.read_csv("data/df7.csv")

def resultadomod(df7):
    col1, col2, col3 = st.columns([0.2,7,0.2])
    with col2:

        tipo = st.selectbox("Seleccione el modelo", ["Seleccionar","O3 (Ozono)","PM2.5 (Particulas en suspension)","PM10 (particulas en suspension)"])

        if (tipo=="Seleccionar"):
            st.write("Selecionar el tipo de modelo")


        elif (tipo=="O3 (Ozono)"):
            X = df7[['CANTIDAD']]
            y = df7['O3']
            X=sm.add_constant(X)
            model=sm.OLS(y,X).fit()
            predictions=model.predict(X)
            st.write(model.summary())

            # Graficar los valores reales vs. los valores proyectados
            plt.figure(figsize=(10, 6))
            plt.scatter(df7['CANTIDAD'], df7['O3'], color='blue', label='Valores Reales')
            plt.plot(df7['CANTIDAD'], df7['O3'], color='red', linewidth=2, label='Valores Proyectados')
            plt.xlabel('CANTIDAD')
            plt.ylabel('O3')
            plt.title('Regresión Lineal OLS: Efecto de la Cantidad de Vehículos en el Ozono')
            plt.legend()
            st.pyplot()

        elif (tipo=="PM2.5 (Particulas en suspension)"):
            X = df7[['CANTIDAD']]
            y = df7['PM2.5']
            X=sm.add_constant(X)
            model=sm.OLS(y,X).fit()
            predictions=model.predict(X)
            st.write(model.summary())

            # Graficar los valores reales vs. los valores proyectados
            plt.figure(figsize=(10, 6))
            plt.scatter(df7['CANTIDAD'], df7['PM2.5'], color='blue', label='Valores Reales')
            plt.plot(df7['CANTIDAD'], df7['PM2.5'], color='red', linewidth=2, label='Valores Proyectados')
            plt.xlabel('CANTIDAD')
            plt.ylabel('PM2.5')
            plt.title('Regresión Lineal OLS: Efecto de la Cantidad de Vehículos en particulas en suspension')
            plt.legend()
            st.pyplot()

        
        
        elif (tipo=="PM10 (particulas en suspension)"):
            X = df7[['CANTIDAD']]
            y = df7['PM10']
            X=sm.add_constant(X)
            model=sm.OLS(y,X).fit()
            predictions=model.predict(X)
            st.write(model.summary())

            # Graficar los valores reales vs. los valores proyectados
            plt.figure(figsize=(10, 6))
            plt.scatter(df7['CANTIDAD'], df7['PM10'], color='blue', label='Valores Reales')
            plt.plot(df7['CANTIDAD'], df7['PM10'], color='red', linewidth=2, label='Valores Proyectados')
            plt.xlabel('CANTIDAD')
            plt.ylabel('PM10')
            plt.title('Regresión Lineal OLS: Efecto de la Cantidad de Vehículos en particulas en suspension')
            plt.legend()
            st.pyplot()

resultadomod(df)
