from flask import Blueprint, jsonify, request
from models.konsultasi import get_all_konsultasi, get_konsultasi_by_id, create_konsultasi, update_konsultasi, delete_konsultasi

konsultasi_bp = Blueprint('konsultasi', __name__)

@konsultasi_bp.route('/', methods=['GET'])
def get_konsultasi():
    konsultasi = get_all_konsultasi()
    if konsultasi:
        return jsonify(konsultasi)
    else:
        return jsonify({'message': 'No konsultasi found'}), 404

@konsultasi_bp.route('/', methods=['POST'])
def add_konsultasi():
    data = request.get_json()
    id_user = data.get('id_user')
    nama = data.get('nama')
    email = data.get('email')
    usia = data.get('usia')
    pesan = data.get('pesan')

    if create_konsultasi(id_user,nama,email,usia,pesan):
        return jsonify({'message': 'konsultasi added successfully!'}), 201
    else:
        return jsonify({'message': 'Error while adding konsultasi'}), 400

@konsultasi_bp.route('/<int:id>', methods=['GET'])
def get_konsultasi_by_id_route(id):
    konsultasi = get_konsultasi_by_id(id)
    if konsultasi:
        return jsonify(konsultasi)
    else:
        return jsonify({'message': 'konsultasi not found'}), 404

@konsultasi_bp.route('/<int:id>', methods=['PUT'])
def update_konsultasi_route(id):
    data = request.get_json()
    data = request.get_json()
    id_user = data.get('id_user')
    nama = data.get('nama')
    email = data.get('email')
    usia = data.get('usia')
    pesan = data.get('pesan')

    if update_konsultasi(id, id_user,nama,email,usia,pesan):
        return jsonify({'message': 'konsultasi updated successfully!'})
    else:
        return jsonify({'message': 'Error while updating konsultasi'}), 400

@konsultasi_bp.route('/<int:id>', methods=['DELETE'])
def delete_konsultasi_route(id):
    if delete_konsultasi(id):
        return jsonify({'message': 'konsultasi deleted successfully!'})
    else:
        return jsonify({'message': 'Error while deleting konsultasi'}), 400
