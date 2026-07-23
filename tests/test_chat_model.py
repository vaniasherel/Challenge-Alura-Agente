"""
test_chat_model.py
Pruebas de integración del pipeline completo (Retriever + Groq).
"""
from src.llm.chat_model import ask


def test_pregunta_con_informacion_disponible():
    """Verifica que el asistente responda correctamente cuando la información existe."""
    respuesta = ask("¿Cuál es el horario de atención?")
    assert "No encontré esa información" not in respuesta


def test_pregunta_sin_informacion_disponible():
    """Verifica que el asistente responda honestamente cuando no tiene la información."""
    respuesta = ask("¿Tienen servicio a domicilio en Cancún?")
    assert "No encontré esa información" in respuesta