from flask import Blueprint, jsonify, request
from models.aturan import (get_all_aturan, get_aturan_by_id, create_aturan, update_aturan,delete_aturan, get_penyakit_by_gejala)

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

@aturan_bp.route('/', methods=['POST'])
def add_aturan():
    data = request.get_json()
    id_gejala = data.get('id_gejala')
    id_penyakit = data.get('id_penyakit')

    if create_aturan(id_gejala, id_penyakit):
        return jsonify({'message': 'gejala added successfully!'}), 201
    else:
        return jsonify({'message': 'Error while adding gejala'}), 400

@aturan_bp.route('/aturan/<int:id_aturan>', methods=['PUT'])
def edit_aturan(id_aturan):
    data = request.get_json()
    id_gejala = data.get('id_gejala')
    id_penyakit = data.get('id_penyakit')
    result = update_aturan(id_aturan, id_gejala, id_penyakit)
    return jsonify(result)

# DELETE Aturan
@aturan_bp.route('/aturan/<int:id_aturan>', methods=['DELETE'])
def remove_aturan(id_aturan):
    result = delete_aturan(id_aturan)
    return jsonify(result)

@aturan_bp.route('/diagnosa', methods=['POST'])
def diagnosa():
    try:
        # Get gejala from the request body
        gejala = request.json.get('gejala')
        
        # Call the get_penyakit_by_gejala function
        penyakit = get_penyakit_by_gejala(gejala)
        
        # Return the disease name as JSON
        return jsonify({'penyakit': penyakit}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


