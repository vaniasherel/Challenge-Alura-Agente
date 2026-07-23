"""
retriever.py

Carga la base vectorial de ChromaDB y realiza búsquedas semánticas.
"""

from pathlib import Path

from langchain_chroma import Chroma

from src.embeddings.embedding_model import get_embedding_model

# Ruta de la base vectorial
VECTOR_DB = Path(__file__).resolve().parents[2] / "data" / "chroma_db"


def get_retriever(k=15):
    """
    Devuelve un retriever configurado.

    Args:
        k (int): Número de documentos a recuperar.

    Returns:
        BaseRetriever
    """

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=str(VECTOR_DB),
        embedding_function=embedding_model
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )


if __name__ == "__main__":

    retriever = get_retriever()

    pregunta = "¿Cuál es el horario de atención?"

    resultados = retriever.invoke(pregunta)

    print(f"\nPregunta: {pregunta}\n")

    for i, doc in enumerate(resultados, start=1):

        print("=" * 60)
        print(f"Resultado {i}")
        print("=" * 60)

        print(doc.page_content)
        print() 