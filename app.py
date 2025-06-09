import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Análisis de datos de anuncios de venta de coches')  # título
# descripción
st.write('Este es un análisis de datos de anuncios de venta de coches en EE.UU.', divider="gray")

st.subheader(
    "En este apartado puedes observar la información por kilometraje vehicular", divider="gray")
st.write('Selecciona la casilla de la grafica que deseas observar.')

build_histogram = st.checkbox('Construir un histograma')
build_dis = st.checkbox('Construir un gráfico de dispersión')
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
elif build_dis:  # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader(
    "Este apartado desarrolla algunos puntos considerables sobre la Venta de autos.", divider="gray")

avg_price_by_condition = car_data.groupby("condition")["price"].mean()
st.write('Este es un análisis agrupado por condicion y precio.')

# Mostrar el gráfico de área en Streamlit
st.area_chart(avg_price_by_condition)

avg_price_by_type = car_data.groupby("type")["price"].mean()
fig_avg_price_by_type = px.pie(avg_price_by_type, names=avg_price_by_type.index,
                               values=avg_price_by_type.values, title='Precio promedio por tipo de vehículo')
st.plotly_chart(fig_avg_price_by_type)
