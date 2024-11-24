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


