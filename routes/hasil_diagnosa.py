from flask import Blueprint, jsonify, request
from models.hasil_diagnosa import create_hasil_diagnosa, get_all_hasil_diagnosa, get_hasil_diagnosa_by_user
from models.aturan import get_penyakit_by_gejala


hasil_diagnosa_bp = Blueprint('hasil_diagnosa', __name__)

@hasil_diagnosa_bp.route('/', methods=['POST'])
def add_hasil_diagnosa():
    data = request.get_json()
    id_user = data.get('id_user')
    gejala_terpilih = data.get('gejala')  # List ID gejala

    if not id_user or not gejala_terpilih:
        return jsonify({'message': 'Data tidak lengkap'}), 400

    # Cari penyakit berdasarkan gejala
    penyakit = get_penyakit_by_gejala(gejala_terpilih)
    if not penyakit:
        return jsonify({'message': 'Tidak ditemukan penyakit yang cocok'}), 404

    # Simpan hasil diagnosis ke database
    if create_hasil_diagnosa(id_user, penyakit['id_penyakit']):
        return jsonify({
            'message': 'Hasil diagnosis berhasil disimpan',
            'diagnosa': {
                'penyakit': penyakit['nama_penyakit'],
                'jumlah_gejala_cocok': penyakit['jumlah_gejala_cocok']
            }
        }), 201
    else:
        return jsonify({'message': 'Gagal menyimpan hasil diagnosis'}), 500


# Ambil semua hasil diagnosa
@hasil_diagnosa_bp.route('/hasil-diagnosa', methods=['GET'])
def get_hasil():
    hasil = get_all_hasil_diagnosa()
    if hasil:
        return jsonify({'data': hasil}), 200
    else:
        return jsonify({'message': 'Tidak ada hasil diagnosa ditemukan'}), 404

# Ambil hasil diagnosa berdasarkan ID User
@hasil_diagnosa_bp.route('/hasil-diagnosa/<int:id_user>', methods=['GET'])
def hasil_by_user(id_user):
    hasil = get_hasil_diagnosa_by_user(id_user)
    if hasil:
        return jsonify({'data': hasil}), 200
    else:
        return jsonify({'message': 'Tidak ada hasil diagnosa untuk user ini'}), 404
