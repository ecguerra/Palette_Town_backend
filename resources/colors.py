import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

colors = Blueprint('colors','colors')

#dev route - will need to be modified for frontend
@colors.route('/',methods=['GET'])
def get_all_colors():
    try:
        colors = [model_to_dict(colors) for colors in models.Color.select()]
        return jsonify(data=colors, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={},status={"code": 404, "message": "Error - that model doesn\'t exist"})


# dev route - will be using API from frontend
@colors.route('/new',methods=['POST'])
def create_color():
    payload = request.get_json()
    color = models.Color.create(**payload)
    color_dict = model_to_dict(color)
    return jsonify(data=color_dict, status={"code": 201, "message": "Successfully created"})