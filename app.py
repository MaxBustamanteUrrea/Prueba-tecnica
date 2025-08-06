from flask import Flask
from routes.routes import status_bp,obtener_personajes_bp, history_ai_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

routes = [status_bp,obtener_personajes_bp,history_ai_bp]

for route in routes:
    app.register_blueprint(route)
    


