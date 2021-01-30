import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

palettes = Blueprint('palettes','palettes')

@palettes.route('/',methods=['GET'])
def get_all_palettes():
    try:
        palettes = [model_to_dict(palettes) for palettes in models.Palette.select()]
        return jsonify(data=palettes, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={},status={"code": 404, "message": "Error - that model doesn\'t exist"})

@palettes.route('/new',methods=['POST'])
def create_palette():
    payload = request.get_json()
    palette = models.Palette.create(**payload)
    palette_dict = model_to_dict(palette)
    return jsonify(data=palette_dict, status={"code": 201, "message": "Successfully created"})