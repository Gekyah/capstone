from flask import Blueprint, jsonify, request
from models.penyakit import get_all_penyakit, get_penyakit_by_id, create_penyakit, update_penyakit, delete_penyakit

penyakit_bp = Blueprint('penyakit', __name__)

@penyakit_bp.route('/', methods=['GET'])
def get_penyakit():
    penyakit = get_all_penyakit()  # Call model to fetch data
    if penyakit:
        return jsonify(penyakit)
    else:
        return jsonify({'message': 'No penyakit found'}), 404

@penyakit_bp.route('/', methods=['POST'])
def add_penyakit():
    data = request.get_json()
    nama_penyakit = data.get('nama_penyakit')

    if create_penyakit(nama_penyakit):  # Call model to insert data
        return jsonify({'message': 'Penyakit added successfully!'}), 201
    else:
        return jsonify({'message': 'Error while adding penyakit'}), 400

@penyakit_bp.route('/<int:id>', methods=['GET'])
def get_penyakit_by_id_route(id):
    penyakit = get_penyakit_by_id(id)  # Call model to fetch a specific disease
    if penyakit:
        return jsonify(penyakit)
    else:
        return jsonify({'message': 'Penyakit not found'}), 404

@penyakit_bp.route('/<int:id>', methods=['PUT'])
def update_penyakit_route(id):
    data = request.get_json()
    nama_penyakit = data.get('nama_penyakit')

    if update_penyakit(id, nama_penyakit):  # Call model to update disease
        return jsonify({'message': 'Penyakit updated successfully!'})
    else:
        return jsonify({'message': 'Error while updating penyakit'}), 400

@penyakit_bp.route('/<int:id>', methods=['DELETE'])
def delete_penyakit_route(id):
    if delete_penyakit(id):  # Call model to delete disease
        return jsonify({'message': 'Penyakit deleted successfully!'})
    else:
        return jsonify({'message': 'Error while deleting penyakit'}), 400
