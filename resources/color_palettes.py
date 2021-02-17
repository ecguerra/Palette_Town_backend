import models

from flask import Blueprint, jsonify, request 
from playhouse.shortcuts import model_to_dict

color_palettes = Blueprint('color_palettes', 'color_palettes')

@color_palettes.route('/', methods=['POST'])
def create_color_palette():
    payload = request.get_json()
    color_palette = models.ColorPalette.create(**payload)
    color_palette_dict = model_to_dict(color_palette)
    return jsonify(data=color_palette_dict, status={"code": 201, "message": "Successfully created"})

@color_palettes.route('/<id>', methods=['Delete'])
def delete_color_palette(id):
    cp_to_delete = models.ColorPalette.get_by_id(id)
    cp_to_delete.delete_instance()
    return jsonify(data={},status={"code": 200, "message": "Successfully deleted"})