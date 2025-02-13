import streamlit as st
import matplotlib.pyplot as plt

def area_circulo(radio):
    return 3.1416 * (radio ** 2)

def area_cuadrado(lado):
    return lado ** 2

#Título de la app
st.title("Calculadora del área sombreada")

#Input del usuario para el lado del cuadrado
lado = st.slider("Selecciona el tamaño del lado del cuadrado:", 1, 20, 10)

#Calcular áreas
radio = lado / 2
circulo = area_circulo(radio)
cuadrado = area_cuadrado(lado)
sombreada = cuadrado - circulo

#Mostrar resultados
st.write(f"Área del círculo: {circulo:.2f}")
st.write(f"Área del cuadrado: {cuadrado:.2f}")
st.write(f"Área sombreada: {sombreada:.2f}")

#Visualizar gráfico
fig, ax = plt.subplots()
square = plt.Rectangle((0, 0), lado, lado, edgecolor="blue", facecolor="none", linewidth=2)
circle = plt.Circle((lado/2, lado/2), radio, edgecolor="red", facecolor="none", linewidth=2)

ax.add_patch(square)
ax.add_patch(circle)
plt.xlim(-1, lado + 1)
plt.ylim(-1, lado + 1)
plt.gca().set_aspect("equal", adjustable="box")
plt.title("Visualización del cuadrado y círculo")

st.pyplot(fig)
