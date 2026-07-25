"""
chroma_store.py

Crea y administra la base vectorial utilizando ChromaDB.
Compatible con ejecución local y Streamlit Cloud.
"""

from langchain_chroma import Chroma


def create_vectorstore(chunks, embedding_model):
    """
    Crea una base vectorial en memoria.

    Esta función se utiliza tanto en desarrollo local como en
    Streamlit Cloud. No depende de una carpeta persistente,
    por lo que evita problemas de permisos y despliegue.
    """

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
    )

    return vectorstore


def get_retriever(vectorstore, k=15):
    """
    Devuelve un retriever configurado a partir de un
    vectorstore ya existente.

    Args:
        vectorstore (Chroma): Base vectorial creada previamente.
        k (int): Número de documentos relevantes a recuperar.

    Returns:
        BaseRetriever
    """

    return vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )


if __name__ == "__main__":

    from src.loaders.pdf_loader import load_pdfs
    from src.loaders.csv_loader import load_csvs
    from src.processing.text_splitter import split_documents
    from src.embeddings.embedding_model import get_embedding_model

    documentos = load_pdfs() + load_csvs()

    chunks = split_documents(documentos)

    modelo = get_embedding_model()

    vectorstore = create_vectorstore(
        chunks,
        modelo,
    )

    retriever = get_retriever(vectorstore)

    resultados = retriever.invoke(
        "¿Cuál es el horario de atención?"
    )

    print(f"Documentos recuperados: {len(resultados)}")