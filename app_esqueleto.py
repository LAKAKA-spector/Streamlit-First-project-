import streamlit as st
import pandas as pd

# ══════════════════════════════════════════════════════════════
# Mi App · Streamlit
# Ficha 3387591 · SENA CTM Itagüí · 2026
# Completá cada sección con los datos de tu proyecto
# ══════════════════════════════════════════════════════════════

# ── DATOS — copiá tu lista de diccionarios del s10 o s11 ──
sistema_mindhub = {
    "nombre_sistema": "MINDHUB Control Panel",
    "version": "3.0",
    "inventario": [
        {
            "id": 1,
            "nombre": "Suscripción Mensual - Plan Pyme",
            "categoria": "SaaS",
            "cantidad": 45,
            "precio": 150000,
        },
        {
            "id": 2,
            "nombre": "Suscripción Mensual - Plan Enterprise",
            "categoria": "SaaS",
            "cantidad": 12,
            "precio": 450000,
        },
        {
            "id": 3,
            "nombre": "Suscripción Anual - Plan Premium",
            "categoria": "SaaS",
            "cantidad": 8,
            "precio": 1200000,
        },
        {
            "id": 4,
            "nombre": "Módulo IA - Auditoría Contable",
            "categoria": "Software",
            "cantidad": 20,
            "precio": 80000,
        },
        {
            "id": 5,
            "nombre": "Módulo IA - Predictor Inventario",
            "categoria": "Software",
            "cantidad": 15,
            "precio": 95000,
        },
        {
            "id": 6,
            "nombre": "Módulo IA - Gestor Documental",
            "categoria": "Software",
            "cantidad": 30,
            "precio": 110000,
        },
        {
            "id": 7,
            "nombre": "Consultoría de Integración SQL",
            "categoria": "Servicios",
            "cantidad": 5,
            "precio": 600000,
        },
    ],
}

# ── SIDEBAR — filtros ──
st.sidebar.title("Filtros")

# Creamos el DataFrame usando la clave "inventario" de tu diccionario
df = pd.DataFrame(sistema_mindhub["inventario"])

# Extraemos las categorías de forma dinámica
categorias = ["Todas"] + list(df["categoria"].unique())

# Filtro en el sidebar
filtro_seleccionado = st.sidebar.selectbox("Seleccionar Categoría", categorias)

# Lógica de filtrado
if filtro_seleccionado == "Todas":
    df_filtrado = df
else:
    df_filtrado = df[df["categoria"] == filtro_seleccionado]


# ── TITULO ──
st.title("MINDHUB")
st.write(
    "MINDHUB nace para eliminar las barreras técnicas, permitiendo que cualquier persona interactúe con la información de su empresa usando IA."
)

# ── MÉTRICAS — mínimo 3 ──
col1, col2, col3 = st.columns(3)  # col1, col2, col3 = st.columns(3)

# 1. Cantidad de elementos (índems) en el filtro actual
col1.metric("Total Items", len(df_filtrado))

# 2. El valor máximo de stock (cantidad) en la selección actual
col2.metric("Stock Máximo", df_filtrado["cantidad"].max())

# 3. El precio promedio de los productos seleccionados
# Usamos :.0f para formatear sin decimales
precio_promedio = df_filtrado["precio"].mean()
col3.metric("Precio Promedio", f"${precio_promedio:,.0f}")


# ── TABLA ──
st.subheader("Registros")

# Usamos df_filtrado para que la tabla sea interactiva y cambie según el filtro
st.dataframe(df_filtrado, use_container_width=True)


# ── BOTÓN DE DESCARGA ──
# Convertimos el DataFrame a CSV
csv = df_filtrado.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Descargar datos como CSV",
    data=csv,
    file_name="inventario_mindhub.csv",
    mime="text/csv",
)


# ── GRÁFICA ──
st.subheader("Estadísticas de Inventario")
# Preparamos los datos: usamos el nombre como índice para que sea la etiqueta del gráfico
# y seleccionamos la columna 'cantidad' para mostrar los valores
grafica_datos = df_filtrado.set_index("nombre")["cantidad"]

# Creamos el gráfico de barras
st.bar_chart(grafica_datos)


# ── FOOTER ──
st.divider()
st.caption("MINDHUB · SENA CTM Itagüí · 2026")
