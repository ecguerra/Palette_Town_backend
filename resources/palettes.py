import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

palettes = Blueprint('palettes','palettes')

# This might just be a dev route - something similar for 'published/public' palettes though
@palettes.route('/all', methods=['GET'])
def get_all_palettes():
    try:
        palettes = [model_to_dict(palettes) for palettes in models.Palette.select()]
        return jsonify(data=palettes, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={},status={"code": 404, "message": "Error - that model doesn\'t exist"})

# show the user their palettes
@palettes.route('/', methods=['GET'])
@login_required
def get_user_palettes():
    try:
        palettes = [model_to_dict(palettes) for palettes in \
                    models.Palette.select() \
                   .join_from(models.Palette, models.AppUser) \
                   .where(models.AppUser.id == current_user.id) \
                   .group_by(models.Palette.id)]
        # need something that will take the password out of the request
        return jsonify(data=palettes, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, \
                       status={"code": 401, "message": "Log in or sign up to view your palettes"})


@palettes.route('/new', methods=['POST'])
def create_palette():
    if current_user.id:
        payload = request.get_json()
        palette = models.Palette.create(**payload)
        palette_dict = model_to_dict(palette)
        del palette_dict['app_user']['password']
        return jsonify(data=palette_dict, status={"code": 201, "message": "Successfully created"})


@palettes.route('/<id>', methods=['GET'])
def get_palette(id):
    try:
        query = (models.ColorPalette.select()
                 .join(models.Palette)
                 .switch(models.ColorPalette)
                 .join(models.Color)
                 .where(models.ColorPalette.palette == id))
        palette = [model_to_dict(item) for item in query]

        return jsonify(data=palette, \
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