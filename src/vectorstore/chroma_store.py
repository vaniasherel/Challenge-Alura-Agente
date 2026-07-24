"""
chroma_store.py
Crea y administra la base de datos vectorial utilizando ChromaDB.
"""
from pathlib import Path
import tempfile
from langchain_chroma import Chroma

# Carpeta donde se guardará la base vectorial (uso local)
VECTOR_DB = Path(tempfile.gettempdir()) / "chroma_db"


def create_vectorstore(chunks, embedding_model, persist=True):
    """
    Crea la base vectorial. Si persist=True, la guarda en disco (uso local).
    Si persist=False, la crea en memoria (uso en Streamlit Cloud, evita
    problemas de permisos de escritura en el servidor).
    """
    if persist:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=str(VECTOR_DB)
        )
    else:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
        )
    return vectorstore


def load_vectorstore(embedding_model):
    """
    Carga una base vectorial ya existente, sin regenerar embeddings.
    """
    vectorstore = Chroma(
        persist_directory=str(VECTOR_DB),
        embedding_function=embedding_model
    )
    return vectorstore


if __name__ == "__main__":
    from src.loaders.pdf_loader import load_pdfs
    from src.loaders.csv_loader import load_csvs
    from src.processing.text_splitter import split_documents
    from src.embeddings.embedding_model import get_embedding_model

    documentos = load_pdfs() + load_csvs()
    chunks = split_documents(documentos)
    modelo = get_embedding_model()

    print(f"Generando embeddings para {len(chunks)} chunks...")
    vectorstore = create_vectorstore(chunks, modelo)
    print(f"\nBase vectorial creada y guardada en: {VECTOR_DB}")
    print(f"Total de chunks almacenados: {len(chunks)}")