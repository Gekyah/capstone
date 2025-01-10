from flask import Blueprint, jsonify, request
from models.gejala import get_all_gejala, get_gejala_by_id, create_gejala, update_gejala, delete_gejala

gejala_bp = Blueprint('gejala', __name__)

@gejala_bp.route('/', methods=['GET'])
def get_gejala():
    gejala = get_all_gejala()
    if gejala:
        return jsonify(gejala)
    else:
        return jsonify({'message': 'No gejala found'}), 404

@gejala_bp.route('/', methods=['POST'])
def add_gejala():
    data = request.get_json()
    nama_gejala = data.get('nama_gejala')

    if create_gejala(nama_gejala):
        return jsonify({'message': 'gejala added successfully!'}), 201
    else:
        return jsonify({'message': 'Error while adding gejala'}), 400

@gejala_bp.route('/<int:id>', methods=['GET'])
def get_gejala_by_id_route(id):
    gejala = get_gejala_by_id(id)
    if gejala:
        return jsonify(gejala)
    else:
        return jsonify({'message': 'gejala not found'}), 404

@gejala_bp.route('/<int:id>', methods=['PUT'])
def update_gejala_route(id):
    data = request.get_json()
    nama_gejala = data.get('nama_gejala')

    if update_gejala(id, nama_gejala):
        return jsonify({'message': 'gejala updated successfully!'})
    else:
        return jsonify({'message': 'Error while updating gejala'}), 400

@gejala_bp.route('/<int:id>', methods=['DELETE'])
def delete_gejala_route(id):
    if delete_gejala(id):
        return jsonify({'message': 'gejala deleted successfully!'})
    else:
        return jsonify({'message': 'Error while deleting gejala'}), 400
