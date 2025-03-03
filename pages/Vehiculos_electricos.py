import pandas as pd
import utilidades as util
import streamlit as st

util.generarMenu()

st.title('Vehículos Eléctricos')
df1 = pd.read_csv('data/Numero_de_Vehiculos_Electricos_Hibridos_20250217.csv')

util.modelo_Veh_Ele(df1)

## st.title('Variables estadisticas de los datos')
## st.write(df.describe())