"""
text_splitter.py
Divide los documentos en fragmentos (chunks)
para facilitar la generación de embeddings.
"""
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Divide una lista de documentos en chunks.
    Args:
        documents (list): Lista de Document.
    Returns:
        list: Lista de chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=350,
        chunk_overlap=60,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )
    chunks = splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    from src.loaders.pdf_loader import load_pdfs
    from src.loaders.csv_loader import load_csvs

    documentos = load_pdfs() + load_csvs()
    chunks = split_documents(documentos)
    print(f"\nSe generaron {len(chunks)} chunks a partir de {len(documentos)} documentos.\n")