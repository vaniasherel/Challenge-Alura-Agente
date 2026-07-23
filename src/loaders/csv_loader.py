"""
csv_loader.py

Módulo encargado de cargar todos los archivos CSV
almacenados en la carpeta data/csv.
"""

from pathlib import Path

import pandas as pd
from langchain_core.documents import Document


CSV_FOLDER = Path(__file__).resolve().parents[2] / "data" / "csv"


def load_csvs():
    """
    Carga todos los archivos CSV de la carpeta data/csv.

    Returns:
        list: Lista de documentos de LangChain.
    """

    documents = []

    csv_files = sorted(CSV_FOLDER.glob("*.csv"))

    for csv_file in csv_files:

        print(f"Cargando: {csv_file.name}")

        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():

            content = "\n".join(
                [f"{column}: {value}" for column, value in row.items()]
            )

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": csv_file.name
                    }
                )
            )

    return documents


if __name__ == "__main__":

    docs = load_csvs()

    print(f"\nSe cargaron {len(docs)} registros.\n")