"""
app.py

Interfaz web del asistente utilizando Streamlit.
"""

import sys
from pathlib import Path

# Agrega la raíz del proyecto al path para que los imports de src.* funcionen
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st

from src.llm.chat_model import ask

st.set_page_config(
    page_title="Asistente Río de Vida",
    page_icon="💧",
    layout="centered",
)

st.title("💧 Asistente Virtual de Purificadora Río de Vida")

st.write(
    """
    Realiza preguntas sobre:

    - Productos
    - Servicios
    - Horarios
    - Cobertura
    - Procesos internos
    - Preguntas frecuentes
    """
)

question = st.text_input(
    "Escribe tu pregunta:",
    placeholder="Ejemplo: ¿Cuál es el horario de atención?"
)

if st.button("Consultar"):
    if question.strip():
        with st.spinner("Consultando documentación..."):
            answer = ask(question)
        st.success(answer)
    else:
        st.warning("Escribe una pregunta.")
