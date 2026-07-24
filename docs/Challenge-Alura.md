# Challenge Alura Agente
## Estado del Proyecto

**Proyecto:**
Asistente Inteligente para Purificadora Río de Vida

**Autor:**
Vania Sherel

**Última actualización:**
Julio 2026

---

# Objetivo del Challenge

Desarrollar un agente de Inteligencia Artificial capaz de responder preguntas en lenguaje natural utilizando información contenida en documentos (PDF y CSV), publicarlo en un repositorio público de GitHub y desplegarlo en una plataforma de alojamiento accesible mediante una URL pública.

---

# Requisitos del Challenge (Alura)

El Challenge se divide en tres grandes etapas:

## Etapa 1
Colecta y organización de documentos

Incluye:
- Seleccionar documentos
- Organizar la información
- Preparar la base documental

---

## Etapa 2
Desarrollo del agente

Incluye:
- Lectura de documentos
- Procesamiento del contenido
- Indexación
- Implementación de RAG
- Generación de respuestas

---

## Etapa 3
Deploy

Incluye:

- Publicar la aplicación.
- Obtener una URL pública.
- Documentar el despliegue.
- Actualizar el README.

---

# Organización del Proyecto

Actualmente el proyecto se organiza así:

```
Challenge-Alura-Agente/
├── .env
├── .gitignore
├── .venv
├── LICENSE
├── README.md
├── requirements.txt
├── data
├── docs
├── src
└── tests
```

---

# Documentación realizada

## 0. Planeación

Realizado

Incluye:
- Project Brief
- Roadmap
- Cronograma

---

## 1. Contexto de la Empresa

Realizado

Incluye:
- Perfil de la empresa
- Organización
- Áreas
- Productos
- Servicios
- Preguntas frecuentes
- Procesos internos
- Mapeo de documentos
- Categorías
- Curaduría
- Ownership
- Accesos
- Ingesta

---

## 2. Análisis del Sistema

Realizado

Documentos elaborados:
- Arquitectura del sistema
- SRS
- Diagrama de Flujo
- Especificación de Casos de Uso
- Diagrama UML de Casos de Uso
- Diagrama de Actividad
- Decisiones de Diseño

---

# Base documental

La base de conocimiento del agente está conformada por documentos PDF y archivos CSV.

## Documentos PDF

Ubicación:

```
data/pdf/
```

Documentos:

- ✅ DOC-001_Perfil_Empresa_Rio_de_Vida.pdf
- ✅ DOC-002_Preguntas_Frecuentes.pdf
- ✅ DOC-003_Procesos_Internos.pdf
- ✅ DOC-004_Procedimientos_Operativos.pdf

Resultado:

- 4 documentos PDF disponibles para el agente.

---

## Documentos CSV

Ubicación:

```
data/csv/
```

Documentos:

- ✅ productos_servicios.csv
- ✅ rutas_reparto.csv

Resultado:

- 2 archivos CSV disponibles para el agente.
- 12 registros estructurados.

---

# Desarrollo

## Preparación del entorno

Estado:

✅ Completado

Configuración realizada:

- Python 3.11
- Entorno virtual (.venv)
- requirements.txt
- .env
- .gitignore

Tecnologías y dependencias principales

- LangChain
- LangChain Community
- LangChain Chroma
- LangChain Groq
- ChromaDB
- Hugging Face Sentence Transformers
- PyTorch
- Pandas
- PyPDF
- Streamlit
- python-dotenv
- Pytest

---

# Arquitectura del proyecto

```
src/


├── loaders/
├── processing/
├── embeddings/
├── vectorstore/
├── rag/
├── llm/
├── ui/
└── utils/
```

---

# Estado actual

Actualmente el desarrollo funcional del proyecto se encuentra concluido.

Completado:

- ✅ Planeación
- ✅ Contexto de la empresa
- ✅ Análisis del sistema
- ✅ Configuración del entorno
- ✅ Organización del proyecto
- ✅ Base documental
- ✅ Capa de ingesta de documentos

---

# Desarrollo realizado

## Módulo 1 - PDF Loader

Archivo:

```
src/loaders/pdf_loader.py
```

Estado:

✅ Completado

Responsabilidad:

- Detectar automáticamente todos los archivos PDF ubicados en `data/pdf`.
- Cargar cada documento mediante LangChain.
- Convertir cada página en objetos `Document`.

Resultado de la prueba:

- 4 documentos PDF cargados.
- 14 páginas procesadas correctamente.

---

## Módulo 2 - CSV Loader

Archivo:

```
src/loaders/csv_loader.py
```

Estado:

✅ Completado

Responsabilidad:

- Detectar automáticamente todos los archivos CSV ubicados en `data/csv`.
- Leer la información utilizando Pandas.
- Convertir cada registro en objetos `Document`.

Resultado de la prueba:

- 2 archivos CSV cargados.
- 12 registros procesados correctamente.

---

## Módulo 3 - Text Splitter

Archivo:

```
src/processing/text_splitter.py
```

Estado:

✅ Completado

Responsabilidad:

- Recibir todos los documentos cargados por los loaders.
- Dividir el contenido en fragmentos (chunks).
- Preparar los datos para la generación de embeddings.

Configuración utilizada:

- Chunk Size: 350
- Chunk Overlap: 60

Resultado de la prueba:

- 26 documentos procesados.
- 53 chunks generados correctamente.

Ajuste realizado:

- La configuración inicial (Chunk Size: 800, Chunk Overlap: 150) generaba chunks demasiado grandes, mezclando varias secciones temáticas del PDF en un mismo fragmento (por ejemplo, Productos, Servicios y Horarios juntos en un solo chunk). Esto afectaba negativamente la precisión del retriever (Módulo 7) al buscar información específica.
- Se redujo el tamaño a 350/60, logrando chunks más enfocados por sección temática y mejorando significativamente la recuperación semántica.

---

## Módulo 4 - Conexión con LLM (Groq)

Archivo:

```
src/llm/groq_client.py
```

Estado:

✅ Completado

Responsabilidad:

- Verificar la conexión con la API de Groq.
- Confirmar la lectura de la variable `GROQ_API_KEY` desde el archivo `.env`.
- Validar la comunicación entre LangChain y el modelo de lenguaje.

Resultado de la prueba:

- Conexión exitosa.
- El modelo respondió correctamente a una solicitud de prueba.

---

## Módulo 5 - Embeddings (Hugging Face)

Archivo:

```
src/embeddings/embedding_model.py
```
Estado:

✅ Completado

Responsabilidad:

- Generar embeddings para cada chunk utilizando modelos de Hugging Face.

Resultado de la prueba:

- Modelo cargado correctamente: `paraphrase-multilingual-MiniLM-L12-v2`.
- Embedding de prueba generado correctamente.

Notas técnicas:

- Se ajustaron las versiones de `sentence-transformers`, `transformers` y `numpy` por incompatibilidad con PyTorch en macOS Intel (no soporta PyTorch ≥2.4).
- Se cambió el modelo inicial (`all-MiniLM-L6-v2`) por `paraphrase-multilingual-MiniLM-L12-v2`, ya que el primero mostraba comprensión semántica débil en español, afectando la precisión del retriever (Módulo 7).

---

## Módulo 6 - ChromaDB (Vector Store)

```
src/vectorstore/chroma_store.py
```

Estado:

✅ Completado

Responsabilidad:

- Almacenar de forma persistente los embeddings generados para cada chunk.
- Almacenar los vectores de forma persistente en ChromaDB.

Resultado de la prueba:

- 53 chunks convertidos en embeddings y almacenados correctamente.
- Base de datos persistente creada en `data/chroma_db`.

Notas:

- La base fue regenerada tras el ajuste de `chunk_size` (Módulo 3), el cambio de modelo de embeddings (Módulo 5), y la incorporación del documento `DOC-004_Procedimientos_Operativos.pdf`, que amplió la cobertura de procesos internos del agente.

---

## Módulo 7 - Retrieval (RAG)

Archivo:

```
src/rag/retrieval.py
```

Estado:

✅ Completado

Responsabilidad:

- Cargar la base vectorial de ChromaDB.
- Recuperar los k chunks más relevantes según la pregunta del usuario.

Resultado de la prueba:

- Pregunta de prueba: "¿Cuál es el horario de atención?"
- Con k=15, se recuperan correctamente los chunks que contienen el horario completo (lunes a viernes, sábado y domingo).

Ajustes realizados durante el desarrollo:

- Se redujo `chunk_size` de 800 a 350 en el Text Splitter (Módulo 3), ya que chunks grandes mezclaban varias secciones temáticas del PDF, dificultando la recuperación semántica precisa.
- Se cambió el modelo de embeddings a `paraphrase-multilingual-MiniLM-L12-v2` por mejor comprensión del español.
- El retriever utiliza actualmente k=15, permitiendo recuperar suficiente contexto para consultas que requieren enumerar múltiples elementos, como colonias con cobertura o catálogo de productos.

---

## Módulo 8 - Pipeline RAG (Retriever + Groq)

Archivos:

- src/llm/chat_model.py
- src/llm/groq_client.py

Estado:

✅ Completado

Responsabilidad:

- Integrar el Retriever (Módulo 7) con el modelo de lenguaje Groq.
- Construir el prompt utilizando el contexto recuperado desde ChromaDB y la pregunta del usuario.
- Generar respuestas en lenguaje natural basadas únicamente en la documentación disponible.
- Proporcionar un modo interactivo por terminal para realizar pruebas del asistente.

Resultado de las pruebas:

- Se validó correctamente el flujo completo de RAG:
  - Recuperación de documentos relevantes desde ChromaDB.
  - Construcción automática del contexto.
  - Generación de respuestas mediante Groq.

- Consulta con información disponible:
  - Pregunta: "¿Cuál es el horario de atención?"
  - Resultado: respuesta correcta utilizando la información recuperada de los documentos.

- Consulta sin información disponible:
  - Pregunta: "¿Tienen servicio a domicilio en Cancún?"
  - Resultado: el modelo indicó correctamente que esa información no se encuentra en la documentación disponible, sin inventar datos.

Observaciones:

- Durante las pruebas se observó que el Retriever recupera algunos chunks adicionales provenientes de los archivos CSV debido a la similitud semántica de ciertos términos (por ejemplo, "Horario"). Aun así, el modelo logró identificar correctamente la información relevante y generar la respuesta esperada.

---

## Módulo 9 - Interfaz Streamlit

Archivo:

```
src/ui/app.py
```

Estado:

✅ Completado

Responsabilidad:

- Proporcionar una interfaz web para interactuar con el asistente sin necesidad de utilizar la terminal.
- Permitir al usuario escribir preguntas mediante un campo de texto y enviarlas al pipeline RAG.
- Mostrar las respuestas generadas por el modelo de lenguaje de forma sencilla y amigable.
- Integrar la interfaz con el backend del proyecto mediante la función `ask()` del Módulo 8.

Resultado de las pruebas:

- La aplicación se ejecuta correctamente mediante Streamlit.
- La interfaz se conecta sin errores al backend del proyecto.
- Las preguntas son enviadas correctamente al pipeline RAG.
- Las respuestas generadas por Groq se muestran correctamente en la interfaz web.
- Se validó el funcionamiento con consultas sobre horarios, productos, servicios y cobertura.
- Se validó también el comportamiento ante preguntas sin información disponible (el modelo responde honestamente que no cuenta con esa información) y ante preguntas ambiguas con múltiples resultados relacionados (el modelo enumera todas las opciones aplicables).

Ajustes realizados:

- Se agregó una regla al prompt del Módulo 8 para que, cuando una consulta sea ambigua y existan varios productos o servicios relacionados en el contexto, el modelo enumere todas las opciones disponibles en lugar de seleccionar una de forma arbitraria.
- Se añadió la columna `Precio` al archivo `productos_servicios.csv`, incorporando información que originalmente no estaba presente en la base documental. Esto permitió que el asistente respondiera correctamente consultas relacionadas con precios utilizando datos estructurados.

Observaciones:

- La interfaz actual corresponde a una primera versión funcional enfocada en validar el funcionamiento del pipeline RAG.
- En futuras mejoras puede incorporarse una interfaz conversacional utilizando `st.chat_input()` y `st.chat_message()` para ofrecer una experiencia similar a ChatGPT, sin modificar la lógica del backend.

Mejoras posteriores

- Se migró la interfaz a un formato conversacional utilizando `st.chat_input()` y `st.chat_message()`.
- Se rediseñó la interfaz utilizando `layout="wide"`.
- Se añadió un tema oscuro personalizado mediante `.streamlit/config.toml`.
- Se incorporó una identidad visual con una mascota representativa del proyecto.
- Se agregó un botón para reiniciar la conversación.
- Se reorganizó la interfaz para mejorar la experiencia del usuario.

---

## Módulo 10 - Pruebas (test)

Archivos:
```
tests/test_cases.md
tests/test_loaders.py
tests/test_processing.py
tests/test_rag.py
tests/test_chat_model.py
pytest.ini
```
Estado:

✅ Completado

Responsabilidad:

- Verificar lectura de documentos.
- Verificar generación de chunks.
- Verificar recuperación RAG.
- Validar respuestas del asistente.

Resultado de las pruebas automatizadas:

- 8 de 8 pruebas pasaron correctamente (`pytest tests/ -v`).
- Cobertura: carga de PDF/CSV, generación de chunks, embeddings, recuperación semántica (horarios y cobertura completa de colonias), y respuestas del asistente (con y sin información disponible).

Resultado de las pruebas manuales (test_cases.md):

- 12 casos de prueba documentados con preguntas reales, resultado esperado y resultado obtenido.
- Se identificaron y corrigieron 2 limitaciones durante las pruebas: listado incompleto de colonias con cobertura y de productos disponibles, ambas resueltas ajustando `k` de 6 a 15 en el retriever.
- Se identificó inicialmente una limitación de la base documental (Caso 7): la pregunta sobre reporte de garrafón dañado no tenía procedimiento redactado. Se incorporó el documento `DOC-004_Procedimientos_Operativos.pdf`, resolviendo la limitación; el asistente ahora recupera y expone el procedimiento real.

Ajustes derivados de las pruebas:

- Se aumentó `k` de 6 a 15 en `src/rag/retrieval.py`, tras detectar que preguntas que requieren listar TODOS los elementos de una categoría (colonias, productos) perdían información con valores bajos de k.
- Se creó `pytest.ini` con `pythonpath = .` en la raíz del proyecto, para resolver errores de importación de módulos internos (`src.*`) al ejecutar pytest.

---

## Módulo 11

Deploy

Estado:

⏳ En preparación

Responsabilidad:

- Publicar la aplicación en Oracle Cloud Infrastructure.

---

## Módulo 12

Documentación final

Estado:

🟡 En progreso

Entregables:

- README: 🔄 En actualización (pendiente agregar evidencia del deploy una vez publicado)
- Repositorio GitHub: ✅ Completado (repositorio público creado y subido)
- Licencia MIT: ✅ Completado
- Evidencias del deploy: ⏳ Pendiente (depende del Módulo 11)
- Capturas del proyecto: 🟡 En preparación (depende del Módulo 11)

---

# Pipeline del sistema

```
Empresa
│
├── Documentos PDF ✅
├── Documentos CSV ✅
│
▼
PDF Loader ✅
│
▼
CSV Loader ✅
│
▼
Documentos LangChain ✅
│
▼
Text Splitter ✅
│
▼
Embeddings ✅ (Hugging Face)
│
▼
ChromaDB ✅
│
▼
Retriever (RAG) ✅
│
▼
LLM ✅ (Groq)
│
▼
Interfaz Streamlit ✅
│
▼
Deploy ⏳
```

---

# Correspondencia con las fases de Alura

| Fase | Estado |
|-------|--------|
| Colecta y organización de documentos | ✅ Completada |
| Procesos y extracción de contenido | ✅ Completada |
| Indexación | ✅ Completada  |
| Capa de recuperación (RAG) | ✅ Completada  |
| Producción y validación de respuestas | ✅ Completada  |
| Implantación, interfaz y mantenimiento | ✅ Completada  |
| Deploy | ⏳ Pendiente |
| Registrar ejecución del proyecto | ⏳ Pendiente |
| README | 🔄 En actualización |
| Finalizar curso en Alura Page | ⏳ Pendiente |

# Notas

Las decisiones de diseño (estructura modular con `loaders`, `processing`, `embeddings`, `vectorstore`, `rag`, `llm`, `ui` y `utils`, uso de `.env`, organización del proyecto y documentación técnica) son mejoras de ingeniería adoptadas para mantener el proyecto ordenado. Complementan el Challenge, pero no sustituyen sus requisitos oficiales.

# Estado actual del proyecto

Actualmente el proyecto cuenta con:

- ✅ Agente RAG funcional.
- ✅ Repositorio público en GitHub.
- ✅ Interfaz conversacional desarrollada en Streamlit.
- ✅ Base vectorial con ChromaDB.
- ✅ Recuperación semántica optimizada.
- ✅ Pruebas automatizadas aprobadas.
- 🔄 Mejoras visuales en progreso.
- ⏳ Deploy en Streamlit Cloud pendiente.

---

Versión del documento: 1.1
Última actualización: Julio 2026

--- 