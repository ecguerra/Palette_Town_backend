import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

palettes = Blueprint('palettes','palettes')

# dev route - will need user-specific
@palettes.route('/',methods=['GET'])
def get_all_palettes():
    try:
        palettes = [model_to_dict(palettes) for palettes in models.Palette.select()]
        return jsonify(data=palettes, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={},status={"code": 404, "message": "Error - that model doesn\'t exist"})

@palettes.route('/new',methods=['POST'])
def create_palette():
    if current_user.id:
        payload = request.get_json()
        palette = models.Palette.create(**payload)
        # current_user.id (?)
        palette_dict = model_to_dict(palette)

        return jsonify(data=palette_dict, status={"code": 201, "message": "Successfully created"})

@palettes.route('/<id>', methods=['GET'])
def get_palette(id):
    try:
        palette = models.Palette.get_by_id(id)
        palette_dict = model_to_dict(palette)
        return jsonify(data=palette_dict, \
                       status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, \
                       status={"code": 404, "message": "resource not found"})

# update a palette. will mainly be to change the name
# will probably need some sort of auth to edit
@palettes.route('/<id>', methods=['PUT'])
def update_palette(id):
    try:
        payload = request.get_json()
        query = models.Palette.update(**payload).where(models.Palette.id==id)
        query.execute()
        updated_palette = model_to_dict(models.Palette.get_by_id(id))
        return jsonify(data=updated_palette, \
                       status={"code": 200, "message": "Successfully updated"})
    except models.DoesNotExist:
        return jsonify(data={}, \
                       status={"code": 404, "message": "resource not found"})

# delete a palette
@palettes.route('/<id>', methods=['Delete'])
def delete_palette(id):
    palette_to_delete = models.Palette.get_by_id(id)
    palette_to_delete.delete_instance()

    return jsonify(data={},status={"code": 200, "message": "Successfully deleted"})