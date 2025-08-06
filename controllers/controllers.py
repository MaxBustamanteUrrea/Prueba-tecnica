from flask import request,jsonify
import os
import requests
import random
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
            if response.status_code != 200:
                return jsonify({
                    "status":"error",
                    "message":"Error al obtener la data"
                })
            data = response.json().get("results", [])            
            lista_personajes_random = random.sample(data,3)            
            personajes = [{"name":personaje["name"],"status":personaje["status"],"species":personaje["species"]} for personaje in lista_personajes_random]

            return jsonify({"data":personajes,"status":"success"})
        except Exception as e:
            return jsonify({
                    "status":"error",
                    "message": str(e)
                }),500 
        
class ObtenerHistoria():
    def obtener_historia():
        try:
            data = GetData.obtener_data()
            res = data.get_json()
            if res["status"] != "success":
                return jsonify({
                    "status":"error",
                    "message": "Error al obtener personajes"
                })
            personajes = res["data"]

            # descripcion = ", ".join([f"{personaje["name"],personaje["status"],personaje["species"]}" for personaje in personajes])
            prompt = f"""
                        Escribe una historia corta y diviertida que incluya a estos personajes de la serie Rick and Morty {personajes},
                        tendrá que tomar en cuenta el status para ver si esta vivo o muerto, la especie para inventar algo especifico de la especie y el nombre para nombrarlo en la historia. 
                        la historia debe ser en español y no tener mas de 120 palabras.
                      """
            client = genai.Client()
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents = prompt
            )
            return jsonify({
                "status": "OK",
                "message":  "success",
                "data":response.text,
                "personajes": personajes
            })
        except Exception as e:
            return jsonify({
                "status":"error",
                "message": str(e)
            }),500
