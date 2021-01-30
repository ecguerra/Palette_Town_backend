import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

palettes = Blueprint('palettes','palettes')

@palettes.route('/',methods=['GET'])
def get_all_palettes():
    return 'palettes stub'