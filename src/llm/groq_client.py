"""
groq_client.py
Configura y expone el modelo de lenguaje de Groq
para ser reutilizado en otros módulos del proyecto.
"""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    """
    Crea y devuelve el modelo de lenguaje conectado a Groq.
    Returns:
        ChatGroq: instancia lista para usarse.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("No se encontró GROQ_API_KEY en el archivo .env")

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=api_key,
        temperature=0,
    )