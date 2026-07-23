"""
debug_retrieval.py
Busca en qué chunk específico vive el texto de horarios,
y en qué posición del ranking quedó.
"""
from src.rag.retrieval import get_retriever

pregunta = "¿Qué colonias tienen cobertura?"

retriever = get_retriever(k=25)
resultados = retriever.invoke(pregunta)

print(f"Total de chunks: {len(resultados)}\n")

for i, doc in enumerate(resultados, start=1):
    if "Colonia" in doc.page_content or "Cobertura" in doc.page_content:
        fuente = doc.metadata.get("source", "desconocida")
        print(f"✅ ENCONTRADO en posición {i} de {len(resultados)}")
        print(f"Fuente: {fuente}")
        print("--- Contenido completo del chunk ---")
        print(doc.page_content)
        print()