from db import mysql

def get_all_aturan():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT penyakit.id_penyakit,penyakit.nama_penyakit,gejala.id_gejala,gejala.nama_gejala FROM aturan JOIN penyakit ON aturan.id_penyakit = penyakit.id_penyakit JOIN gejala ON aturan.id_gejala = gejala.id_gejala")
        result = cur.fetchall()
        cur.close()
        return [{'id_penyakit': x[0], 'nama_penyakit': x[1], 'id_gejala': x[2], 'nama_gejala': x[3]} for x in result]
    except Exception as e:
        print(f"Error fetching all aturan: {e}")
        return []

def get_aturan_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT penyakit.id_penyakit,penyakit.nama_penyakit,gejala.id_gejala,gejala.nama_gejala FROM aturan JOIN penyakit ON aturan.id_penyakit = penyakit.id_penyakit JOIN gejala ON aturan.id_gejala = gejala.id_gejala WHERE penyakit.id_penyakit = %s", (id,))
        result = cur.fetchall()
        cur.close()
        if result:
            return [{'id_penyakit': x[0], 'nama_penyakit': x[1], 'id_gejala': x[2], 'nama_gejala': x[3]} for x in result]
        return None
    except Exception as e:
        print(f"Error fetching aturan by ID {id}: {e}")
        return None

def get_penyakit_by_gejala(gejala):
    print(f"Gejala yang diterima: {gejala}")
    """Cari penyakit berdasarkan gejala yang dipilih"""
    try:
        cur = mysql.connection.cursor()
        query = """
            SELECT p.id_penyakit, p.nama_penyakit, COUNT(a.id_gejala) AS jumlah_gejala_cocok
            FROM aturan a
            JOIN penyakit p ON a.id_penyakit = p.id_penyakit
            WHERE a.id_gejala IN %s
            GROUP BY p.id_penyakit
            ORDER BY jumlah_gejala_cocok DESC
            LIMIT 1
        """
        cur.execute(query, (tuple(gejala),))
        hasil = cur.fetchone()
        cur.close()
        if hasil:
            return {
                'id_penyakit': hasil[0],
                'nama_penyakit': hasil[1],
                'jumlah_gejala_cocok': hasil[2]
            }
        return None
    except Exception as e:
        print(f"Error get_penyakit_by_gejala: {e}")
        return None


def create_aturan(id_gejala, id_penyakit):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO aturan (id_gejala, id_penyakit) VALUES (%s, %s)", (id_gejala, id_penyakit))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error creating gejala: {e}")
        return False

def update_aturan(id_aturan, id_gejala, id_penyakit):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE aturan SET id_gejala = %s, id_penyakit = %s WHERE id_aturan = %s",
                    (id_gejala, id_penyakit, id_aturan))
        mysql.connection.commit()
        cur.close()
        return {"message": "Aturan berhasil diperbarui"}
    except Exception as e:
        print(f"Error updating aturan: {e}")
        return {"error": "Gagal memperbarui aturan"}

def delete_aturan(id_aturan):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM aturan WHERE id_aturan = %s", (id_aturan,))
        mysql.connection.commit()
        cur.close()
        return {"message": "Aturan berhasil dihapus"}
    except Exception as e:
        print(f"Error deleting aturan: {e}")
        return {"error": "Gagal menghapus aturan"}

   