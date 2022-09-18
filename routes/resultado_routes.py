from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.resultado_controller import ResultadoController
from decorators.token_decorator import token, role

resultado_module= Blueprint("resultados",__name__)
controller= ResultadoController()    

@resultado_module.post('/mesa/<string:mesa_id>/candidatos/<string:candidato_id>')
@token
@role("Admin")
def create(mesa_id,candidato_id):
    response, code = controller.create_resultado(mesa_id,candidato_id,request.get_json())
    return jsonify(response),code
      
@resultado_module.get('/')
@token
@role("Admin")
def get_resultado():
    response,code= controller.get_resultado(request.args)
    return jsonify(response),code

@resultado_module.get('/<string:id>')
@token
@role("Admin")
def get_resultado_id(id):
    response,code = controller.get_resultado_id(request.args,id)
    return jsonify(response),code

@resultado_module.put('/<string:id>')
@token
@role("Admin")
def upd_resultado(id):
    response,code = controller.update_resultado(id,request.get_json())
    return jsonify(response),code

@resultado_module.delete('/<string:id>')
@token
@role("Admin")
def delete_resultado(id):
    response,code = controller.delete_resultado(id,request.args)
    return jsonify(response),code
