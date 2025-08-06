# Prueba Técnica: Servicio de Historias de Rick y Morty con IA

Este proyecto implementa un servicio en **Flask** que permite gestionar historias basadas en la serie _Rick y Morty_ integrando capacidades de Inteligencia Artificial.

---

## 📦 Requisitos

El proyecto utiliza las siguientes dependencias (listadas en `requirements.txt`):

- annotated-types==0.7.0
- anyio==4.10.0
- blinker==1.9.0
- cachetools==5.5.2
- certifi==2025.8.3
- charset-normalizer==3.4.2
- click==8.2.1
- colorama==0.4.6
- exceptiongroup==1.3.0
- Flask==3.1.1
- google-auth==2.40.3
- google-genai==1.28.0
- h11==0.16.0
- httpcore==1.0.9
- httpx==0.28.1
- idna==3.10
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- pyasn1==0.6.1
- pyasn1_modules==0.4.2
- pydantic==2.11.7
- pydantic_core==2.33.2
- python-dotenv==1.1.1
- requests==2.32.4
- rsa==4.9.1
- sniffio==1.3.1
- tenacity==8.5.0
- typing-inspection==0.4.1
- typing_extensions==4.14.1
- urllib3==2.5.0
- websockets==15.0.1
- Werkzeug==3.1.3

## ⚙️ Instalación

1. Clona el proyecto o descarga el código.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crea un archivo .env con tus variables de entorno (AUTH_USER y AUTH_PASSWORD es donde deben ir las credenciales):
   FLASK_DEBUG=1
   FLASK_ENV=development

   GEMINI_API_KEY= KEY

   AUTH_USER="123"
   AUTH_PASSWORD="abc"

## ▶️ Uso

flask run
Por defecto se ejecuta en:
http://localhost:5000

## 📂 Arquitectura del Proyecto

El proyecto sigue una arquitectura modular para mantener el código limpio y escalable:

project/
├── app.py # Punto de entrada (inicializa Flask)
├── routes/ # Rutas (Blueprints)
├── controllers/ # Lógica del proyecto
├── .env # Variables de entorno
└── requirements.txt # Dependencias
