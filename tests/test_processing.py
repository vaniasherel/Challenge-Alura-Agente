"""
test_processing.py
Pruebas automatizadas para la división de documentos en chunks.
"""
from src.loaders.pdf_loader import load_pdfs
from src.loaders.csv_loader import load_csvs
from src.processing.text_splitter import split_documents


def test_split_documents_genera_chunks():
    """Verifica que los documentos se dividan correctamente en chunks."""
    documentos = load_pdfs() + load_csvs()
    chunks = split_documents(documentos)

    assert len(chunks) > len(documentos), "El splitter no generó más fragmentos que documentos originales"
    assert all(len(chunk.page_content) > 0 for chunk in chunks)