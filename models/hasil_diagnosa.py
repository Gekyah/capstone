from db import mysql

def create_hasil_diagnosa(id_user, id_penyakit):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hasil_diagnosa (id_user, id_penyakit) VALUES (%s, %s)", (id_user, id_penyakit))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error menambahkan hasil diagnosa: {e}")
        return False

def get_all_hasil_diagnosa():
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT hd.id_hasil, u.nama AS nama_user, p.nama_penyakit, hd.tanggal
            FROM hasil_diagnosa hd
            JOIN user u ON hd.id_user = u.id_user
            JOIN penyakit p ON hd.id_penyakit = p.id_penyakit;
        """)
        hasil = cur.fetchall()
        cur.close()
        return hasil
    except Exception as e:
        print(f"Error mengambil semua hasil diagnosa: {e}")
        return None

def get_hasil_diagnosa_by_user(id_user):
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT hd.id_hasil, p.nama_penyakit, hd.tanggal
            FROM hasil_diagnosa hd
            JOIN penyakit p ON hd.id_penyakit = p.id_penyakit
            WHERE hd.id_user = %s;
        """, (id_user,))
        hasil = cur.fetchall()
        cur.close()
        return hasil
    except Exception as e:
        print(f"Error mengambil hasil diagnosa untuk user: {e}")
        return None
