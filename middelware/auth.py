import functools
from flask import request, jsonify
import base64
import os

def basic_auth_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        USERNAME = os.getenv('AUTH_USER')
        PASSWORD = os.getenv('AUTH_PASSWORD')

        if not auth or not auth.startswith('Basic '):
            return jsonify({
                "status": "error",
                "message": "No se ha proporcionado autenticación"
            }), 401
        try:
            encoded_credentials = auth.split(' ')[1]
            decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
            username, password = decoded_credentials.split(':', 1)
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
        if username != USERNAME or password != PASSWORD:
            return jsonify({
                "status": "error",
                "message": "Credenciales incorrectas",                
            }), 401
        return f(*args, **kwargs)
    return decorated