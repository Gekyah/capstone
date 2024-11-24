from flask import Blueprint, jsonify, request
from models.aturan import get_all_aturan, get_aturan_by_id

aturan_bp = Blueprint('aturan', __name__)

@aturan_bp.route('/', methods=['GET'])
def get_aturan():
    aturan = get_all_aturan()
    if aturan:
        return jsonify(aturan)
    else:
        return jsonify({'message': 'No aturan found'}), 404

@aturan_bp.route('/<int:id>', methods=['GET'])
def get_aturan_by_id_route(id):
    aturan = get_aturan_by_id(id)
    if aturan:
        return jsonify(aturan)
    else:
        return jsonify({'message': 'aturan not found'}), 404

