# 💧 Asistente Virtual de Purificadora Río de Vida

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorStore-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

**Proyecto final — Challenge Alura Agente (Oracle Next Education / Alura Latam)**

Un asistente inteligente que responde preguntas en lenguaje natural sobre **Purificadora Río de Vida**, una empresa de purificación y distribución de agua en garrafones en Villahermosa, Tabasco, utilizando **RAG (Retrieval-Augmented Generation)** sobre su propia documentación (PDF y CSV).

---

## 📖 Visión general

En lugar de depender del conocimiento general de un modelo de lenguaje, este asistente **recupera información real** desde los documentos oficiales de la empresa (perfil, preguntas frecuentes, procesos internos, catálogo de productos y rutas de reparto) y genera respuestas basadas únicamente en esa información — evitando inventar datos que no existen en la documentación.

---

## ✨ Características principales

- 📄 Ingesta automática de documentos PDF y CSV
- ✂️ División inteligente de texto en fragmentos (chunking)
- 🧠 Embeddings semánticos multilingües con Hugging Face (100% local, sin costo)
- 🔍 Base de datos vectorial persistente con ChromaDB
- 🤖 Generación de respuestas mediante Groq API utilizando Llama 3.3 70B Versatile.
- 🚫 Prevención de alucinaciones: si la información no existe en la documentación, el asistente lo indica honestamente
- 🔀 Manejo de preguntas ambiguas: enumera todas las opciones relevantes en vez de elegir una al azar
- 💬 Interfaz web simple con Streamlit
- ✅ Suite de pruebas automatizadas (pytest) + casos de prueba documentados manualmente

---

## 🏛️ Arquitectura / Pipeline del sistema

```
Documentos de la empresa (PDF + CSV)
            │
            ▼
     PDF Loader / CSV Loader   (LangChain + Pandas)
            │
            ▼
     Text Splitter             (chunk_size=350, overlap=60)
            │
            ▼
     Embeddings                (Hugging Face · paraphrase-multilingual-MiniLM-L12-v2)
            │
            ▼
     ChromaDB                  (base vectorial persistente)
            │
            ▼
     Retriever           (Semantic Search, k=15)
            │
            ▼
     LLM (Groq · Llama 3.3 70B)
            │
            ▼
     Interfaz Streamlit
```

---

## ⚙️ Tecnologías utilizadas

| Categoría | Tecnología |
|---|---|
| Lenguaje | Python 3.11 |
| Orquestación IA | LangChain |
| Modelo de lenguaje (LLM) | Groq (Llama 3.3 70B Versatile) |
| Embeddings | Hugging Face (`paraphrase-multilingual-MiniLM-L12-v2`) |
| Base de datos vectorial | ChromaDB |
| Carga de documentos | PyPDFLoader (LangChain Community), Pandas |
| Interfaz web | Streamlit |
| Pruebas | Pytest |
| Gestión de secretos | python-dotenv |

---

## 📂 Estructura del proyecto

```
Challenge-Alura-Agente/
├── .env                        # Variables de entorno (no se sube al repo)
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── pytest.ini
│
├── data/
│   ├── pdf/                    # Documentos PDF de la empresa
│   ├── csv/                    # Catálogo de productos y rutas de reparto
│   └── chroma_db/               # Base vectorial persistente (generada localmente)
│
├── docs/                       # Documentación técnica del proyecto
│
├── src/
│   ├── loaders/                # Carga de PDF y CSV
│   ├── processing/             # División en chunks
│   ├── embeddings/             # Modelo de embeddings (Hugging Face)
│   ├── vectorstore/            # Conexión y persistencia con ChromaDB
│   ├── rag/                    # Recuperación semántica (retriever)
│   ├── llm/                    # Conexión con Groq y pipeline RAG + LLM
│   └── ui/                     # Interfaz Streamlit
│
└── tests/
    ├── test_cases.md           # Casos de prueba documentados manualmente
    ├── test_loaders.py
    ├── test_processing.py
    ├── test_rag.py
    └── test_chat_model.py
```

---

## 🚀 Cómo ejecutar el proyecto localmente

### Requisitos previos

- Python 3.11+
- Cuenta gratuita en [Groq](https://console.groq.com) (para la API Key del LLM)

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/challenge-alura-agente.git
cd challenge-alura-agente
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```
GROQ_API_KEY=tu_clave_de_groq
```

### 4. Generar la base vectorial (primera vez)

```bash
python -m src.vectorstore.chroma_store
```

### 5. Ejecutar la aplicación

```bash
streamlit run src/ui/app.py
```

La aplicación estará disponible en `http://localhost:8501`.

---

## 🧪 Pruebas

Actualmente la suite contiene 8 pruebas automatizadas, todas aprobadas.: carga de documentos, generación de chunks, embeddings, recuperación semántica e integración completa RAG + LLM.

```bash
pytest tests/ -v
```

Además, en [`tests/test_cases.md`](tests/test_cases.md) se documentan 7 casos de prueba manuales con preguntas reales, resultado esperado y resultado obtenido, incluyendo el manejo de preguntas sin información disponible y preguntas ambiguas.

---

## 🔐 Seguridad

Las claves de API nunca se almacenan en el código fuente ni se suben al repositorio. Se gestionan mediante variables de entorno en un archivo `.env`, excluido explícitamente en `.gitignore`.

---

## 🛠️ Decisiones de diseño y aprendizajes técnicos

Durante el desarrollo se enfrentaron y resolvieron varios retos técnicos reales, documentados con detalle en `docs/Challenge-Alura.md`:

- **Compatibilidad de PyTorch en macOS Intel:** se ajustaron versiones específicas de `sentence-transformers`, `transformers` y `numpy`, ya que PyTorch dejó de dar soporte a Mac Intel a partir de la versión 2.3.
- **Calidad del chunking:** se redujo `chunk_size` de 800 a 350 caracteres tras detectar que fragmentos grandes mezclaban varias secciones temáticas, afectando la precisión de la recuperación semántica.
- **Modelo de embeddings:** se reemplazó el modelo inicial (`all-MiniLM-L6-v2`) por uno multilingüe (`paraphrase-multilingual-MiniLM-L12-v2`) por mejor comprensión del español.
- **Ajuste de `k` en el retriever:** se incrementó de 6 a 15 tras detectar que preguntas que requieren listar todos los elementos de una categoría (ej. todas las colonias con cobertura) perdían información con valores bajos de `k`.
- **Manejo de ambigüedad:** se ajustó el prompt del LLM para que, ante preguntas con múltiples resultados relacionados, enumere todas las opciones en vez de elegir una al azar.

---

## 📌 Alcance y limitaciones conocidas

- La base documental fue elaborada específicamente para este proyecto educativo (documentos y datos representativos, no de una empresa operando actualmente).
- Algunos procedimientos internos mencionados en la documentación (ej. protocolo ante un garrafón dañado) están listados como tema, pero su procedimiento detallado no fue redactado — el asistente responde honestamente que no cuenta con esa información en vez de inventarla.
- El asistente responde únicamente con información contenida en la base documental.

---

## 👩‍💻 Autor

**Vania Sherel Cruz**

Proyecto desarrollado como parte del **Challenge Alura Agente** (Oracle Next Education / Alura Latam).

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Ver [`LICENSE`](LICENSE) para más detalles.

---

Desarrollado con 💜 usando Python, LangChain, Groq y Streamlit. 💧
