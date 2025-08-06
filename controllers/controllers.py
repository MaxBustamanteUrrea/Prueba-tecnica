from flask import request,jsonify
import os
import requests
import random
import base64
from google import genai

class ObtenerStatus():
    def status():
        try:
            return jsonify({
                "status": "OK",
                "message":  "Service is running"
            })
        except Exception as e:
            return jsonify({
                "status":"error",
                "message": str(e)
            }),500
        
class GetData():
    def obtener_data():
        try:
            url ="https://rickandmortyapi.com/api/character"
            response = requests.get(url)
            data = response.json()            
            lista_personajes = data['results']
            personajes = [{"name":personaje["name"],"status":personaje["status"],"species":personaje["species"]} for personaje in lista_personajes]
            lista_personajes_random = random.sample(personajes,5)            
            return jsonify({"data":lista_personajes_random})
        except Exception as e:
            return jsonify({
                    "status":"error",
                    "message": str(e)
                }),500 
        
class ObtenerHistoria():
    def obtener_historia():
        try:
            data = GetData.obtener_data()
            client = genai.Client()
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents="Explain how AI works in a few words"
            )
            return jsonify({
                "status": "OK",
                "message":  "success",
                "data":response.text
            })
        except Exception as e:
            return jsonify({
                "status":"error",
                "message": str(e)
            }),500
