from db import mysql

def get_all_penyakit():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM penyakit")
        result = cur.fetchall()
        cur.close()
        return [{'id_penyakit': x[0], 'nama_penyakit': x[1]} for x in result]
    except Exception as e:
        print(f"Error fetching all penyakit: {e}")
        return []

def get_penyakit_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM penyakit WHERE id_penyakit = %s", (id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return {'id_penyakit': result[0], 'nama_penyakit': result[1]}
        return None
    except Exception as e:
        print(f"Error fetching penyakit by ID {id}: {e}")
        return None

def create_penyakit(nama):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO penyakit (nama_penyakit) VALUES (%s)", (nama,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error creating penyakit: {e}")
        return False

def update_penyakit(id, nama):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE penyakit SET nama_penyakit = %s WHERE id_penyakit = %s", (nama, id))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error updating penyakit ID {id}: {e}")
        return False

def delete_penyakit(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM penyakit WHERE id_penyakit = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error deleting penyakit ID {id}: {e}")
        return False
