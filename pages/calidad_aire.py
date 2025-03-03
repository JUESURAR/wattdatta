import pandas as pd
import utilidades as util
import streamlit as st

util.generarMenu()

st.title('Calidad Del aire en colombia')
df2 = pd.read_csv('data/CALIDAD_DEL_AIRE_EN_COLOMBIA__PROMEDIO_ANUAL__20250217.csv')



util.modelo_cal_air(df2)

