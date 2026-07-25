"""
app.py

Interfaz web del asistente utilizando Streamlit.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from PIL import Image

from src.llm.chat_model import ask

from src.loaders.pdf_loader import load_pdfs
from src.loaders.csv_loader import load_csvs
from src.processing.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from src.vectorstore.chroma_store import create_vectorstore
from src.rag.retrieval import set_vectorstore

# --------------------------------------------------
# Configuración
# --------------------------------------------------

st.set_page_config(
    page_title="Asistente Río de Vida",
    page_icon="💧",
    layout="wide",
)

# --------------------------------------------------
# Inicialización del sistema RAG
# --------------------------------------------------

@st.cache_resource(show_spinner="Preparando la base de conocimiento...")
def initialize_rag():
    """
    Construye la base vectorial una sola vez al iniciar
    la aplicación y la comparte con todo el proyecto.
    """

    documentos = load_pdfs() + load_csvs()

    chunks = split_documents(documentos)

    embedding_model = get_embedding_model()

    vectorstore = create_vectorstore(
        chunks,
        embedding_model,
    )

    set_vectorstore(vectorstore)

    return True


initialize_rag()

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

Este proyecto utiliza un sistema **Retrieval-Augmented Generation (RAG)** para responder únicamente con información contenida en la documentación oficial de la empresa.

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
    st.caption("Villahermosa, Tabasco")

# --------------------------------------------------
# Encabezado
# --------------------------------------------------

col_texto, col_mascota = st.columns([2, 1])

with col_texto:

    st.title("💧 Asistente Virtual de Purificadora Río de Vida")

    st.write(
        "Asistente corporativo basado en Inteligencia Artificial y Retrieval-Augmented Generation (RAG)."
    )

with col_mascota:

    imagen = Image.open("assets/gotita.png")

    st.image(
        imagen,
        width=320,
    )

st.divider()

# --------------------------------------------------
# Historial del chat
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

# --------------------------------------------------
# Entrada del usuario
# --------------------------------------------------

if prompt := st.chat_input("Escribe tu pregunta..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🔎 Consultando documentación..."):

            answer = ask(prompt)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

# --------------------------------------------------
# Botón borrar conversación
# --------------------------------------------------

col1, col2 = st.columns([6, 1])

with col2:

    if st.button(
        "🗑️ Borrar chat",
        help="Borrar toda la conversación",
    ):

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