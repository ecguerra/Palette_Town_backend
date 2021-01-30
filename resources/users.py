import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

users = Blueprint('users','users')

@users.route('/',methods=['GET'])
def get_all_users():
    return 'users stub'