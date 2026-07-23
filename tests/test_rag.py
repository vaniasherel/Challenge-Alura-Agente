"""
test_rag.py
Pruebas automatizadas para embeddings y recuperación semántica (retrieval).
"""

from src.embeddings.embedding_model import get_embedding_model
from src.rag.retrieval import get_retriever


def test_embedding_model_genera_vector():
    """Verifica que el modelo de embeddings genere un vector válido."""
    modelo = get_embedding_model()
    vector = modelo.embed_query("Prueba de embedding")

    assert isinstance(vector, list)
    assert len(vector) > 0


def test_retriever_encuentra_horario():
    """Verifica que el retriever encuentre información sobre horarios."""
    retriever = get_retriever(k=15)
    resultados = retriever.invoke("¿Cuál es el horario de atención?")

    contenido_total = " ".join(doc.page_content for doc in resultados)

    assert "7 am" in contenido_total


def test_retriever_encuentra_informacion_de_cobertura():
    """
    Verifica que el retriever recupere información relevante
    sobre la cobertura de reparto.
    """
    retriever = get_retriever(k=25)
    resultados = retriever.invoke("¿Qué colonias tienen cobertura?")

    contenido_total = " ".join(doc.page_content for doc in resultados)

    # Debe recuperar información de cobertura
    assert "Cobertura" in contenido_total

    colonias_esperadas = [
        "Centro",
        "Atasta",
        "Tamulté",
        "Gaviotas",
        "Carrizal",
        "Deportiva",
    ]

    colonias_encontradas = [
        c for c in colonias_esperadas if c in contenido_total
    ]

    # En una base documental creciente el ranking puede variar.
    # Lo importante es recuperar la mayor parte de la información relevante.
    assert len(colonias_encontradas) >= 5