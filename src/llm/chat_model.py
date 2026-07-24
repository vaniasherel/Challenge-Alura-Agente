"""
chat_model.py

Conecta el Retriever con Groq para implementar
un flujo básico de Retrieval-Augmented Generation (RAG).
"""

from langchain_core.prompts import ChatPromptTemplate

from src.llm.groq_client import get_llm
from src.rag.retrieval import get_retriever


PROMPT = ChatPromptTemplate.from_template("""
Eres el asistente virtual de Purificadora Río de Vida.

Tu única fuente de información es el contexto proporcionado.

Reglas obligatorias:

- Nunca inventes información.
- Si la información no aparece en el contexto responde exactamente:

"No encontré esa información en la documentación disponible."

- Responde siempre en español.

- Utiliza formato Markdown para que la respuesta sea agradable de leer.

- Cuando exista una lista de elementos (colonias, productos, servicios, procesos, horarios, preguntas frecuentes, etc.) preséntala como lista con viñetas.

- Cuando tenga sentido utiliza títulos en Markdown (## o ###).

- Destaca en **negritas** los datos importantes como horarios, precios, nombres de productos o colonias.

- Si una pregunta tiene varias respuestas en el contexto, incluye TODAS.

- No agregues explicaciones que no estén en la documentación.

- Mantén un tono amable, claro y profesional.

Contexto:
{context}

Pregunta:
{question}

Respuesta:
""")


def ask(question: str):
    """
    Recupera documentos relevantes y genera una respuesta
    utilizando RAG.
    """

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    llm = get_llm()

    chain = PROMPT | llm

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