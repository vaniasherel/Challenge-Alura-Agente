"""
embedding_model.py
Genera embeddings para los chunks usando un modelo
de Hugging Face que corre localmente.
"""
from langchain_huggingface import HuggingFaceEmbeddings

# Modelo ligero, rápido y muy usado para RAG en español/multilingüe
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def get_embedding_model():
    """
    Crea y devuelve el modelo de embeddings de Hugging Face.
    Returns:
        HuggingFaceEmbeddings: modelo listo para generar vectores.
    """
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    return embeddings


if __name__ == "__main__":
    modelo = get_embedding_model()
    vector_prueba = modelo.embed_query("Hola, esto es una prueba")
    print(f"Dimensión del embedding: {len(vector_prueba)}")
    print(f"Primeros 5 valores: {vector_prueba[:5]}")