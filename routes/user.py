from flask import Blueprint, jsonify, request
from models.user import get_all_user, get_user_by_id, create_user, update_user, delete_user, login, get_jumlah_pasien

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_user():
    user = get_all_user()
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'No user found'}), 404

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    nama = data.get('nama')
    email = data.get('email')
    password = data.get('password')
    alamat = data.get('alamat')
    no_telepon = data.get('no_telepon')
    jenis_kelamin = data.get('jenis_kelamin')

    if create_user(nama,email,password,alamat,no_telepon,jenis_kelamin):
        return jsonify({'message': 'user added successfully!'}), 201
    else:
        return jsonify({'message': 'Error while adding user'}), 400

@user_bp.route('/<int:id>', methods=['GET'])
def get_user_by_id_route(id):
    user = get_user_by_id(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'user not found'}), 404

@user_bp.route('/<int:id_user>', methods=['PUT'])
def update_user_route(id_user):
    data = request.get_json()
    nama = data.get('nama')
    email = data.get('email')
    password = data.get('password')
    alamat = data.get('alamat')
    no_telepon = data.get('no_telepon')
    jenis_kelamin = data.get('jenis_kelamin')

    if update_user(id_user,nama,email,password,alamat,no_telepon,jenis_kelamin):
        return jsonify({'message': 'user updated successfully!'})
    else:
        return jsonify({'message': 'Error while updating user'}), 400

@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    if delete_user(id):
        return jsonify({'message': 'user deleted successfully!'})
    else:
        return jsonify({'message': 'Error while deleting user'}), 400

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if login(email,password):
        return jsonify({'message': 'login success'}), 200
        
    else:
        return jsonify({'message': 'login error'}), 400

@user_bp.route('/dashboard/jumlah-pasien', methods=['GET'])
def jumlah_pasien():
    data = get_jumlah_pasien()
    if data:
        return jsonify({
            'message': 'Jumlah pasien berhasil diambil',
            'data': data
        }), 200
    else:
        return jsonify({'message': 'Gagal mengambil jumlah pasien'}), 500