import streamlit as st

st.write("# Definicion Y concepto de truncamiento en Distribuciones ")
st.write("El **truncamiento** de una distribución consiste en restringir su dominio a un intervalo específico, $[a, b]$, de modo que sólo se consideren los valores de la variable aleatoria que se encuentren en ese rango, descartando todos los demás valores fuera de él.")

st.markdown("""
## ¿En qué consiste el truncamiento?

Cuando truncamos una distribución, hacemos lo siguiente:

1. **Selección del intervalo:**  
   Se define un intervalo $[a, b]$ donde la distribución es considerada. Los valores de la variable que se encuentren fuera de este rango se eliminan.

2. **Re-normalización:**  
   Debido a que se han eliminado algunas partes de la distribución original, la función de densidad debe ser ajustada para que la probabilidad total en el intervalo $[a, b]$ sea igual a 1. Esto se logra dividiendo la densidad original por la probabilidad acumulada en el intervalo, es decir, $( F(b) - F(a) )$.
""")

st.markdown("## Fórmulas del truncamiento")

st.latex(r'''
f_{\text{trunc}}(x) = \begin{cases}
\frac{f(x)}{F(b) - F(a)} & \text{si } a \leq x \leq b, \\
0 & \text{en otro caso.}
\end{cases}
''')

st.markdown("y la función de distribución acumulada truncada es:")

st.latex(r'''
F^*(x) = \begin{cases}
0 & \text{si } x < a, \\
\frac{F(x) - F(a)}{F(b) - F(a)} & \text{si } a \leq x \leq b, \\
1 & \text{si } x > b.
\end{cases}
''')

st.markdown("""
## ¿Por qué utilizar el truncamiento?

- **Limitaciones físicas o de observación:**  
  En muchos casos, la variable de interés sólo puede tomar valores dentro de un rango específico.
- **Eliminación de colas extremas:**  
  Puede ser útil para evitar el efecto de colas muy largas o valores atípicos en el análisis.
- **Mejora en el modelado:**  
  Al concentrarse en el rango de interés, se pueden obtener modelos más precisos para ciertos fenómenos.

A continuación se harán varios ejercicioos con diferentes distribuciones.
""")
