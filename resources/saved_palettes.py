import models

from flask import Blueprint, jsonify,request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

saved_palettes = Blueprint('saved_palettes', 'saved_palettes')

@saved_palettes.route('/', methods=['POST'])
def create_saved_palette():
    payload = request.get_json()
    saved_palette = models.SavedPalette.create(**payload)
    saved_palette_dict = model_to_dict(saved_palette)
    return jsonify(data=saved_palette_dict, status={"code": 201, "message": "Successfully created"})