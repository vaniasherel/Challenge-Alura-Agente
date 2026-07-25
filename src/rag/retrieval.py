"""
retrieval.py

Construye y devuelve el Retriever utilizado por el sistema RAG.
"""

from src.vectorstore.chroma_store import get_retriever as build_retriever

# Variable global donde se almacenará el vectorstore
_vectorstore = None


def set_vectorstore(vectorstore):
    """
    Guarda la instancia del vectorstore para que pueda
    ser utilizada por el resto de la aplicación.

    Args:
        vectorstore (Chroma): Base vectorial creada al iniciar la app.
    """
    global _vectorstore
    _vectorstore = vectorstore


def get_retriever(k=15):
    """
    Devuelve un retriever utilizando el vectorstore ya cargado.

    Args:
        k (int): Número de documentos a recuperar.

    Returns:
        BaseRetriever
    """

    if _vectorstore is None:
        raise RuntimeError(
            "La base vectorial aún no ha sido inicializada."
        )

    return build_retriever(
        _vectorstore,
        k=k,
    )


if __name__ == "__main__":

    print(
        "Este módulo requiere que el vectorstore sea inicializado "
        "desde la aplicación principal."
    )