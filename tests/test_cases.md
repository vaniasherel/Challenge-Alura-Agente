# Casos de prueba

## Objetivo

Validar el funcionamiento del asistente virtual "Purificadora Río de Vida" verificando la recuperación de información desde la base documental (PDF y CSV), la generación de respuestas mediante RAG y el manejo de consultas fuera del contexto.

---

# Caso 1 - Horario de atención

**Pregunta**

> ¿Cuál es el horario de atención?

**Resultado esperado**

El asistente debe responder:

- Lunes a viernes: 7:00 am - 6:00 pm
- Sábado: 7:00 am - 5:00 pm
- Domingo: 7:00 am - 3:00 pm

**Resultado obtenido**

✅ Correcto.

El asistente recuperó la información desde el PDF y respondió correctamente.

---

# Caso 2 - Productos

**Pregunta**

> ¿Qué productos ofrece Río de Vida?

**Resultado esperado**

El asistente debe mencionar:

- Agua purificada
- Garrafón de 20 litros

**Resultado obtenido**

✅ Correcto (ajustado).
Inicialmente el asistente solo mencionaba 1 producto por limitación de `k`. Tras aumentar k=6 a k=15, el asistente ahora menciona los 2 productos existentes como entradas distintas en `productos_servicios.csv` (Agua purificada y Garrafón vacío). Se detectó que el PDF original lista "Garrafón de 20 litros" y "Envase (Garrafón vacío)" como conceptos redundantes, no representados como filas separadas en el CSV.

---

# Caso 3 - Servicios

**Pregunta**

> ¿Qué servicios ofrecen?

**Resultado esperado**

El asistente debe listar los servicios disponibles.

**Resultado obtenido**

✅ Correcto. 

---

# Caso 4 - Cobertura

**Pregunta**

> ¿Qué colonias tienen cobertura?

**Resultado esperado**

El asistente debe recuperar la información desde el archivo `rutas_reparto.csv`.

**Resultado obtenido**

✅ Correcto (ajustado).

Inicialmente el asistente solo mencionaba 1 de 6 colonias por limitación de k=6. Se aumentó a k=15, tras lo cual el asistente enumeró correctamente las 6 colonias con cobertura.

---

# Caso 5 - Precios

**Pregunta**

> ¿Cuánto cuesta un garrafón?

**Resultado esperado**

El asistente debe utilizar la información almacenada en `productos_servicios.csv`.

**Resultado obtenido**

✅ Correcto.

---

# Caso 6 - Información inexistente

**Pregunta**

> ¿Tienen sucursal en Cancún?

**Resultado esperado**

El asistente debe indicar que la información no se encuentra disponible en la documentación.

**Resultado obtenido**

✅ Correcto.

No inventó información.

---

# Caso 7 - Procedimiento: Garrafón roto

**Pregunta**

> ¿Qué debo hacer si un garrafón llega roto?

**Resultado esperado**

El asistente debe recuperar el procedimiento operativo documentado para atender un garrafón dañado.

**Resultado obtenido**

✅ Correcto.

El asistente recuperó el procedimiento desde `DOC-004_Procedimientos_Operativos.pdf`, indicando que se debe:

- Pedir una disculpa al cliente.
- Verificar visualmente el daño.
- Tomar evidencia fotográfica cuando sea posible.
- Reemplazar inmediatamente el garrafón si existe disponibilidad.
- Reportar el incidente para su seguimiento.

---

# Caso 8 - Procedimiento: Llanta ponchada

**Pregunta**

> ¿Qué hago si una llanta se poncha durante una ruta?

**Resultado esperado**

El asistente debe recuperar el procedimiento correspondiente.

**Resultado obtenido**

✅ Correcto.

El asistente indicó correctamente:

- Detener el vehículo en un lugar seguro.
- Encender las luces intermitentes.
- Colocar los señalamientos preventivos.
- Cambiar la llanta únicamente si existen condiciones seguras.

---

# Caso 9 - Cliente ausente

**Pregunta**

> ¿Qué hacer si un cliente no está en su domicilio?

**Resultado esperado**

El asistente debe recuperar el procedimiento operativo.

**Resultado obtenido**

✅ Correcto.

El asistente respondió correctamente indicando:

- Intentar comunicarse por teléfono.
- Esperar un máximo de 10 minutos.
- Continuar la ruta si no hay respuesta.
- Registrar la entrega como "Cliente ausente".
- Informar al área de atención al cliente para reprogramar la entrega.

--- 

# Caso 10 - Solicitud de crédito

**Pregunta**

> ¿Qué hacer si un cliente quiere pagar después?

**Resultado esperado**

El asistente debe recuperar el procedimiento establecido para solicitudes de crédito.

**Resultado obtenido**

✅ Correcto.

El asistente respondió correctamente que:

- Solo los clientes autorizados cuentan con crédito.
- Debe verificarse la autorización con administración.
- Si no existe autorización, debe solicitarse el pago al momento de la entrega.

---

# Caso 11 - Información parcialmente disponible

**Pregunta**

> ¿Cómo actuar si un cliente se pone agresivo?

**Resultado esperado**

El asistente debe indicar que no encontró exactamente esa información y no debe inventar procedimientos.

**Resultado obtenido**

✅ Correcto.

El asistente indicó que no encontró esa información específica y, de manera complementaria, recuperó el procedimiento existente para la atención de quejas, dejando claro que no correspondía exactamente a la consulta realizada.

---

# Caso 12 - Información inexistente

**Pregunta**

> ¿Cómo se reporta un accidente de reparto?

**Resultado esperado**

El asistente debe indicar que esa información no se encuentra en la documentación disponible.

**Resultado obtenido**

✅ Correcto.

El asistente respondió que no encontró esa información en la documentación disponible y no generó información inventada.

--- 

# Conclusiones

Se validó el funcionamiento completo del sistema RAG:

- Carga de documentos PDF y CSV.
- División del contenido en chunks.
- Generación de embeddings mediante Hugging Face.
- Almacenamiento persistente en ChromaDB.
- Recuperación semántica mediante Retriever.
- Construcción del contexto para el modelo de lenguaje.
- Generación de respuestas utilizando Groq.

Las pruebas funcionales demostraron que el asistente responde correctamente tanto consultas comerciales (productos, servicios, horarios, precios y cobertura) como procedimientos operativos internos dirigidos a los colaboradores de la empresa. Asimismo, cuando la información solicitada no existe en la base documental, el sistema responde de forma transparente sin inventar contenido, garantizando la confiabilidad de las respuestas.