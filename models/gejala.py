from db import mysql

def get_all_gejala():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM gejala")
        result = cur.fetchall()
        cur.close()
        return [{'id_gejala': x[0], 'nama_gejala': x[1]} for x in result]
    except Exception as e:
        print(f"Error fetching all gejala: {e}")
        return []

def get_gejala_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM gejala WHERE id_gejala = %s", (id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return {'id_gejala': result[0], 'nama_gejala': result[1]}
        return None
    except Exception as e:
        print(f"Error fetching gejala by ID {id}: {e}")
        return None

def create_gejala(nama):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO gejala (nama_gejala) VALUES (%s)", (nama,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error creating gejala: {e}")
        return False

def update_gejala(id, nama):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE gejala SET nama_gejala = %s WHERE id_gejala = %s", (nama, id))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error updating gejala ID {id}: {e}")
        return False

def delete_gejala(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM gejala WHERE id_gejala = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error deleting gejala ID {id}: {e}")
        return False
