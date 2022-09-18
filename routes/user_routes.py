from urllib import request, response
from flask import Blueprint, jsonify, request
from controllers.user_controller import UserController
from decorators.token_decorator import token, role

user_module= Blueprint("users",__name__)
controller= UserController()

@user_module.post('/')
@token
def create():
    response, code = controller.create_user(request.get_json())
    return jsonify(response),code
      
@user_module.get('/')
@token
@role("Admin")
def get_user():
    response,code= controller.get_user(request.args)
    return jsonify(response),code

@user_module.get('/<string:id>')
@token
@role("Admin")
def get_user_id(id):
    response,code = controller.get_user_id(request.args,id)
    return jsonify(response),code

@user_module.get('/role/<string:role>')
@token
@role("Admin")
def get_user_role(role):
    response,code = controller.get_user_role(request.args,role)
    return jsonify(response),code

@user_module.put('/<string:id>')
@token
@role("Admin")
def update_user(id):
    response,code = controller.upd_user(id,request.get_json())
    return jsonify(response),code

@user_module.delete('/<string:id>')
@token
@role("Admin")
def delete_user(id):
    response,code = controller.delete_user(id,request.args)
    return jsonify(response),code