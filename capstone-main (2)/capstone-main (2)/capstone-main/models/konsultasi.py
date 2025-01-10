from db import mysql

def get_all_konsultasi():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM konsultasi")
        result = cur.fetchall()
        cur.close()
        return [{'id_konsultasi': x[0], 
        'id_user': x[1],
        'nama': x[2],
        'email': x[3],
        'usia': x[4],
        'pesan': x[5],
        'tanggal': x[6],
        } for x in result]
    except Exception as e:
        print(f"Error fetching all konsultasi: {e}" )
        return []

def get_konsultasi_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM konsultasi WHERE id_konsultasi = %s", (id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return [{'id_konsultasi': result[0], 
            'id_user': result[1],
            'nama': result[2],
            'email': result[3],
            'usia': result[4],
            'pesan': result[5],
            'tanggal': result[6],
            } for x in result]
        return None
    except Exception as e:
        print(f"Error fetching konsultasi by ID {id}: {e}")
        return None

def create_konsultasi(id_user,nama,email,usia,pesan):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO konsultasi (id_user,nama,email,usia,pesan) VALUES (%s,%s,%s,%s,%s)", (id_user,nama,email,usia,pesan,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error creating konsultasi: {e}")
        return False

def update_konsultasi(id_konsultasi,id_user,nama,email,usia,pesan):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE konsultasi SET id_user = %s,nama = %s ,email = %s,usia = %s,pesan = %s WHERE id_konsultasi = %s", (id_user,nama,email,usia,pesan, id_konsultasi))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error updating konsultasi ID {id}: {e}")
        return False

def delete_konsultasi(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM konsultasi WHERE id_konsultasi = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error deleting konsultasi ID {id}: {e}")
        return False
