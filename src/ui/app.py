"""
app.py

Interfaz web del asistente utilizando Streamlit.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from src.llm.chat_model import ask
from PIL import Image

# --------------------------------------------------
# Configuración
# --------------------------------------------------

st.set_page_config(
    page_title="Asistente Río de Vida",
    page_icon="💧",
    layout="wide",
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.markdown("## 💧 Río de Vida")
    st.caption("Agua pura, vida sana.")

    st.markdown("### Puedes preguntarme sobre:")
    st.markdown("""
- 🚚 Cobertura
- 🕒 Horarios
- 💧 Productos
- 🛒 Servicios
- 📄 Procesos
- ❓ Preguntas frecuentes
""")

    st.divider()

    st.markdown("""
### 🤖 Asistente con IA

Este proyecto utiliza un sistema **RAG (Retrieval-Augmented Generation)** para responder preguntas utilizando únicamente la documentación oficial de la empresa.

### Tecnologías

- Python
- LangChain
- ChromaDB
- Hugging Face
- Groq
- Streamlit
""")

    st.divider()
    st.markdown("📍 **Purificadora Río de Vida**")
    st.caption("Villahermosa, Tabasco.")

# --------------------------------------------------
# Encabezado con mascota grande
# --------------------------------------------------

col_texto, col_mascota = st.columns([2, 1])

with col_texto:
    st.title("💧 Asistente Virtual de Purificadora Río de Vida")
    st.write("Asistente corporativo basado en Inteligencia Artificial y Retrieval-Augmented Generation (RAG).")

with col_mascota:
    imagen = Image.open("assets/gotita.png")
    st.image(imagen, width=320)

st.divider()

# --------------------------------------------------
# Chat
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 ¡Hola! Soy el asistente virtual de **Purificadora Río de Vida**.\n\n"
                "Puedes preguntarme sobre horarios, cobertura, productos, servicios o procesos internos."
            ),
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu pregunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🔎 Consultando documentación..."):
            answer = ask(prompt)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# --------------------------------------------------
# Botón nueva conversación
# --------------------------------------------------

col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🗑️ Borrar chat", help="Borrar toda la conversación"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 ¡Hola! Soy el asistente virtual de **Purificadora Río de Vida**.\n\n"
                    "¿En qué puedo ayudarte hoy?"
                ),
            }
        ]
        st.rerun()