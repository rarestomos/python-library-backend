import logging

from flask import Blueprint, request

from library_backend.api import UserApi, app_response

logger = logging.getLogger(__name__)

users = Blueprint("users", __name__)


@users.route('/users', methods=['POST'])
def create_user():
    user = request.get_json(force=True)
    user_api = UserApi()
    response = user_api.create_user(user)
    return app_response(response)


@users.route('/users', methods=['GET'])
def list_users():
    user_api = UserApi()
    response = user_api.list_users()
    return app_response(response)


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_api = UserApi()
    response = user_api.delete_user(user_id)
    return app_response(response)


@users.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    new_user = request.get_json(force=True)
    user_api = UserApi()
    response = user_api.update_user(new_user=new_user, user_id=user_id)
    return app_response(response)


@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_api = UserApi()
    response = user_api.get_user(user_id)
    return app_response(response)
