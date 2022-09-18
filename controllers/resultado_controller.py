from urllib import response
from wsgiref import headers
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request
import requests

config= dotenv_values('.env')

class ResultadoController():
    def __init__(self):
        pass
    
    def create_resultado(self,mesa_id,candidato_id,data):
        headers= {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULT']}/resultados/mesa/{mesa_id}/candidatos/{candidato_id}",json=data, headers=headers)
        if response.status_code==201:
            return response.json(),201
        return {
            "message": "Error"
        },400
        
    def get_resultado(self,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultados", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return response.json()
    
    def get_resultado_id(self,args,id):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.get(url=f"{config['URL_RESULT']}/resultados/{id}", headers= headers)
        if response.status_code ==200:
            return response.json(),200
        return {
            "messagge":"Id no encotrado"
        }
    
    def update_partido(self,id,data):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.put(url=f"{config['URL_RESULT']}/resultados/{id}", json=data, headers=headers)
        if response.status_code == 204:
            return {},204
        return {
            "messagge":"Id no encontrado"
        },400
        
    def delete_partido(self,id,args):
        headers = {
         "Content-Type": "application/json"
        }
        response= requests.delete(url=f"{config['URL_RESULT']}/resultados/{id}", headers=headers)
        print(response.status_code)
        if response.status_code == 204:
            return{
                "message":"Eliminación exitosa"
                },204
        return{
            "message":"Id no encontrado"
        },400
    
        
   
    