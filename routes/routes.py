import os
from flask import Blueprint
from controllers.controllers import ObtenerStatus, GetData, ObtenerHistoria
from middelware.auth import basic_auth_required

status_bp = Blueprint('status_bp',__name__)
obtener_personajes_bp = Blueprint('obtener_personajes_bp',__name__)
history_ai_bp =  Blueprint('history_ai_bp',__name__)

@status_bp.route('/status', methods=['GET'])
@basic_auth_required
def obtenerStatus():
    return ObtenerStatus.status()

@obtener_personajes_bp.route('/data', methods=['GET'])
@basic_auth_required
def obtenerPersonajes():
    return GetData.obtener_data()

@history_ai_bp.route('/history_ai',methods=['POST'])
@basic_auth_required
def obtenerHisotira():
    return ObtenerHistoria.obtener_historia()




