import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, truncnorm

st.write("# Parámetros y funciones de la distribución normal")
st.write("Aquí establecemos los parámetros de la distribución normal y calculamos la función de densidad de probabilidad (PDF) y la función de distribución acumulada (CDF).")
st.write("Los parámetros de la distribución normal son la media **(mu) = 12** y la desviación estándar **(sigma) = 2**.")



# Parametros y funciones de la distribución	
mu = 12
sigma = 2
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)

codigo = '''
mu = 12
sigma = 2
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)
'''

st.code(codigo, language='python')


st.write("**Nota:** x es un array de valores para los que calculamos la PDF y la CDF.")

###############################################

# Gráfica de la distribución normal completa
import streamlit as st
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from scipy.stats import norm

st.write(" ")
st.write("### Gráficas de la distribución normal")

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=("Función de Densidad de Probabilidad (PDF)",
                                    "Función de Distribución Acumulada (CDF)"))

# Agregar traza para la PDF
fig.add_trace(go.Scatter(x=x, y=pdf,
                         mode='lines',
                         name='PDF',
                         line=dict(color='blue')),
              row=1, col=1)

# Agregar traza para la CDF
fig.add_trace(go.Scatter(x=x, y=cdf,
                         mode='lines',
                         name='CDF',
                         line=dict(color='red')),
              row=1, col=2)

# Actualizar layout para estilo e interactividad
fig.update_layout(hovermode="x unified",
                  template="plotly_white")

# Mostrar la figura en Streamlit
st.plotly_chart(fig, use_container_width=True)


###############################################

# Truncamiento
# --- Distribución truncada ---
# Definimos los límites de truncamiento (modificalos según lo que necesites)
a, b = -1, 1

# Para truncnorm, los parámetros a y b deben estar estandarizados: (limite - mu) / sigma
a_std, b_std = (a - mu) / sigma, (b - mu) / sigma
print(f"Límites estandarizados: a={a_std}, b={b_std}")

# Creamos la distribución normal truncada
trunc_dist = truncnorm(a_std, b_std, loc=mu, scale=sigma) # loc=mu (media), scale=sigma (desviación estándar) son los parámetros de la normal
print(trunc_dist.mean(), trunc_dist.std())

# Valores para la gráfica en el rango truncado
x_trunc = np.linspace(a, b, 1000)
pdf_trunc = trunc_dist.pdf(x_trunc)
cdf_trunc = trunc_dist.cdf(x_trunc)

###############################################

# Crear figura con subplots
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=("PDF de la Normal Truncada", "CDF de la Normal Truncada"))

# Agregar traza para la PDF truncada
fig.add_trace(go.Scatter(x=x_trunc, y=pdf_trunc,
                         mode='lines',
                         name='PDF truncada',
                         line=dict(color='purple')),
              row=1, col=1)

# Agregar traza para la CDF truncada
fig.add_trace(go.Scatter(x=x_trunc, y=cdf_trunc,
                         mode='lines',
                         name='CDF truncada',
                         line=dict(color='green')),
              row=1, col=2)

# Actualizar layout para un mejor estilo e interactividad
fig.update_layout(title_text="Gráficas de la Normal Truncada",
                  hovermode="x unified",
                  template="plotly_white")

# Mostrar la figura en Streamlit
st.plotly_chart(fig, use_container_width=True)

###############################################

# Calculos de probabilidad
# Calcular probabilidad de que x esté entre 0.5 y 1 para la distribución normal completa
p_normal = norm.cdf(1, mu, sigma) - norm.cdf(0.5, mu, sigma)
print("Probabilidad en la distribución normal entre 0 y 1:", p_normal)

# Calcular probabilidad de que x esté entre 0.5 y 1 para la distribución truncada
p_trunc = trunc_dist.cdf(1) - trunc_dist.cdf(0.5)
print("Probabilidad en la distribución truncada entre 0 y 1:", p_trunc)
