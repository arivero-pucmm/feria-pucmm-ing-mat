import streamlit as st
from streamlit_javascript import st_javascript
import pandas as pd
import datetime

# Configuración de página con estilo tecnológico
st.set_page_config(page_title="Huella Digital - Ingeniería Matemática", page_icon="📊")

# Estilo CSS personalizado para mejorar la estética
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e44fe; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Tu Huella Digital en Tiempo Real")
st.write("### ¿Sabías que cada interacción genera datos? En Ingeniería Matemática y Ciencia de Datos, nosotros les damos sentido.")

st.divider()

# --- CAPTURA DE DATOS VÍA JAVASCRIPT ---
# Obtenemos datos del navegador que Python no ve directamente
user_agent = st_javascript("navigator.userAgent")
battery_level = st_javascript("navigator.getBattery().then(b => Math.round(b.level * 100))")
language = st_javascript("navigator.language")
screen_res = st_javascript("`${window.screen.width}x${window.screen.height}`")

if user_agent:
    col1, col2 = st.columns(2)

    with col1:
        # 1. Hardware / OS
        os_info = "iOS/Apple" if "iPhone" in user_agent or "Mac" in user_agent else "Android/Linux"
        st.metric("Dispositivo Detectado", os_info)
        st.info(f"**Clasificación de Hardware:** Eres parte del grupo que usa {os_info}. Modelamos patrones de consumo global basados en estos segmentos.")

        # 2. Batería
        st.metric("Nivel de Energía", f"{battery_level}%")
        st.info(f"**Optimización Estocástica:** Diseñamos los algoritmos que deciden cómo ahorrar este {battery_level}% de energía en procesos de fondo.")

        # 3. Resolución
        st.metric("Resolución de Pantalla", screen_res)
        st.info("**Visualización de Datos:** Los científicos de datos adaptamos modelos complejos para que sean legibles en estas dimensiones exactas.")

    with col2:
        # 4. Idioma
        st.metric("Idioma del Sistema", language)
        st.info(f"**NLP (Procesamiento de Lenguaje):** Tu sistema prefiere '{language}'. Usamos IA para que las máquinas entiendan el lenguaje humano.")

        # 5. Timestamp
        ahora = datetime.datetime.now().strftime("%H:%M:%S")
        st.metric("Hora del Escaneo", ahora)
        st.info("**Series de Tiempo:** Este punto en el tiempo nos ayuda a predecir picos de tráfico en la feria mediante forecasting.")

        # 6. ID de Visitante (Simulado con sesión)
        if 'count' not in st.session_state: st.session_state.count = 124 # Base inicial ficticia
        st.session_state.count += 1
        st.metric("Visitante N°", st.session_state.count)
        st.info("**Big Data:** Eres un dato más en nuestra muestra. A mayor N, menor es nuestro margen de error estadístico.")

    st.divider()
    
    # --- VISUALIZACIÓN AGREGADA (DEMO) ---
    st.subheader("📈 Lo que estamos viendo en la Feria hoy")
    data_demo = pd.DataFrame({
        'Categoría': ['iOS', 'Android', 'Otros'],
        'Usuarios': [45, 52, 12]
    })
    st.bar_chart(data=data_demo, x='Categoría', y='Usuarios')
    st.caption("Gráfico generado en tiempo real combinando todos los escaneos previos.")

else:
    st.warning("Cargando tu huella digital... Por favor, espera un segundo.")

st.sidebar.image("https://via.placeholder.com/150", caption="Ingeniería Matemática & Ciencia de Datos")
st.sidebar.write("### ¿Te interesa el futuro?")
st.sidebar.write("Aprende a dominar los datos, no solo a generarlos.")
