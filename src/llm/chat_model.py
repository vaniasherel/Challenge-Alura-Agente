"""
chat_model.py

Conecta el Retriever con Groq para implementar
un flujo básico de Retrieval-Augmented Generation (RAG).
"""

from langchain_core.prompts import ChatPromptTemplate

from src.llm.groq_client import get_llm
from src.rag.retrieval import get_retriever


PROMPT = ChatPromptTemplate.from_template("""
Eres el asistente virtual de la empresa Río de Vida.
Tu tarea es responder preguntas utilizando únicamente la información proporcionada en el contexto.

Reglas:
- No inventes información.
- Si la respuesta no aparece en el contexto, responde exactamente:
"No encontré esa información en la documentación disponible."
- Si la pregunta es general o ambigua y el contexto contiene varios productos o servicios relacionados (por ejemplo, distintos tipos de garrafón), menciona TODOS los que apliquen con su precio correspondiente, en vez de elegir uno solo.
- Responde siempre en español.
- Sé claro, amable y profesional.

Contexto:
{context}

Pregunta:
{question}

Responde utilizando únicamente la información del contexto.
""")


def ask(question: str):
    """
    Recupera el contexto más relevante desde ChromaDB
    y genera una respuesta utilizando Groq.
    """

    # Obtener retriever
    retriever = get_retriever()

    # Recuperar documentos relacionados
    docs = retriever.invoke(question)

    # Mostrar documentos recuperados (para depuración)
    print("\n================ DOCUMENTOS RECUPERADOS ================\n")

    for i, doc in enumerate(docs, start=1):
        print(f"Documento {i}")
        print("-" * 60)
        print(doc.page_content)
        print()

    print("=" * 60)

    # Construir contexto
    context = "\n\n".join(doc.page_content for doc in docs)

    # Obtener modelo
    llm = get_llm()

    # Crear cadena
    chain = PROMPT | llm

    # Obtener respuesta
    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response.content


if __name__ == "__main__":

    print("=" * 60)
    print("Asistente Virtual - Río de Vida")
    print("Escribe 'salir' para terminar.")
    print("=" * 60)

    while True:

        question = input("\nPregunta: ")

        if question.lower() in ["salir", "exit"]:
            print("\nHasta luego.\n")
            break

        answer = ask(question)

        print("\n=================== RESPUESTA ===================\n")
        print(answer)
        print()