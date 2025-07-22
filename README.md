🤖 SimpleBot - Asistente de Ferretería con ChatGPT-4

Este proyecto es un chatbot de línea de comandos que responde consultas sobre productos de ferretería usando la API de OpenAI GPT-4. Es ideal como base para quienes desean crear soluciones conversacionales simples pero efectivas con IA generativa.

🧠 Funcionalidades
✅ Chatbot en consola usando Python
✅ Lectura de catálogo (productos_ferreteria.csv)
✅ Reglas de atención personalizada (reglas.txt)
✅ Conversación contextual con memoria
✅ Conexión a la API de OpenAI (modelo GPT-4)
✅ Generación de respuestas amigables con emoticones
✅ Soporte para delivery, pagos y códigos de pedido

🧱 Arquitectura
El bot sigue una arquitectura sencilla y funcional:
🧑‍💻 El usuario ingresa preguntas desde la terminal.
📦 Se leen las reglas de conversación (reglas.txt) y los productos (productos_ferreteria.csv).
🧠 Se construye un contexto con esta información.
🔁 Se envía el historial completo al modelo GPT-4 vía API de OpenAI (clave_api.txt).
💬 La respuesta del modelo se guarda y muestra.
⏱️ Todo esto ocurre en segundos, con una experiencia conversacional coherente y amigable.

<img width="782" height="422" alt="image" src="https://github.com/user-attachments/assets/274d03a4-7a89-4441-b2cb-9a3edf82b455" />

📂 Estructura del proyecto
├── chatbot_gen.py              # Código principal del bot
├── productos_ferreteria.csv    # Catálogo de productos
├── reglas.txt                  # Reglas de atención y lógica
├── Arquitectura_simpleBot_Ferreteria.png    # Imagen del diagrama de arquitectura
└── README.md                   # Este documento
