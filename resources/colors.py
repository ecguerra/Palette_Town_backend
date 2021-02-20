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


@colors.route('/new',methods=['GET','POST'])
def find_or_create_color():
    payload = request.get_json()
    try:
        color = models.Color.get(models.Color.hex_name == payload['hex_name'])
        color_dict = model_to_dict(color)
        return jsonify(data=color_dict, status={"code": 200, "message": "Successfully found"})
    except models.Color.DoesNotExist:
        new_color = models.Color.create(**payload)
        new_color_dict = model_to_dict(new_color)
        return jsonify(data=new_color_dict, status={"code": 200, "message": "Successfully created"})


