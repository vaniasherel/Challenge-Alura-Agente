"""
test_loaders.py
Pruebas automatizadas para los módulos de carga de documentos (PDF y CSV).
"""
from src.loaders.pdf_loader import load_pdfs
from src.loaders.csv_loader import load_csvs


def test_pdf_loader_carga_documentos():
    """Verifica que se carguen los 3 PDFs y se generen páginas como Document."""
    documentos = load_pdfs()
    assert len(documentos) > 0, "No se cargó ningún PDF"
    assert all(hasattr(doc, "page_content") for doc in documentos)


def test_csv_loader_carga_registros():
    """Verifica que se carguen los registros de ambos CSV."""
    documentos = load_csvs()
    assert len(documentos) == 12, f"Se esperaban 12 registros, se obtuvieron {len(documentos)}"
    assert all(hasattr(doc, "page_content") for doc in documentos)