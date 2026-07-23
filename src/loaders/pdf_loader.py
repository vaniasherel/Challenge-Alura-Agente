"""
pdf_loader.py
Módulo encargado de cargar todos los documentos PDF
almacenados en la carpeta data/pdf.
"""
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Ruta calculada automáticamente, sin importar desde dónde ejecutes el script
PDF_FOLDER = Path(__file__).resolve().parents[2] / "data" / "pdf"


def load_pdfs():
    """
    Carga todos los archivos PDF de la carpeta data/pdf.
    Returns:
        list: Lista de documentos cargados por LangChain.
    """
    documents = []
    pdf_files = sorted(PDF_FOLDER.glob("*.pdf"))
    for pdf in pdf_files:
        print(f"Cargando: {pdf.name}")
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())
    return documents


if __name__ == "__main__":
    docs = load_pdfs()
    print(f"\nSe cargaron {len(docs)} páginas.\n")