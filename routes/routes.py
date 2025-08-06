import os
from flask import Blueprint
from controllers.controllers import ObtenerStatus, GetData, ObtenerHistoria

status_bp = Blueprint('status_bp',__name__)
obtener_personajes_bp = Blueprint('obtener_personajes_bp',__name__)
history_ai_bp =  Blueprint('history_ai_bp',__name__)

@status_bp.route('/status', methods=['GET'])
def obtenerStatus():
    return ObtenerStatus.status()

@obtener_personajes_bp.route('/data', methods=['GET'])
def obtenerPersonajes():
    return GetData.obtener_data()

@history_ai_bp.route('/history_ai',methods=['POST'])
def obtenerHisotira():
    return ObtenerHistoria.obtener_historia()




