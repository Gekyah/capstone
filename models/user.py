from db import mysql

def get_all_user():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user")
        result = cur.fetchall()
        cur.close()
        return [{'id_user': x[0], 
        'nama': x[1],
        'email': x[2],
        'password': x[3],
        'alamat': x[4],
        'no_telepon': x[5],
        'jenis_kelamin': x[6]
        } for x in result]
    except Exception as e:
        print(f"Error fetching all user: {e}" )
        return []

def get_user_by_id(id_user):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE id_user = %s", (id_user,))
        result = cur.fetchone()
        cur.close()
        if result:
            return {'id_user': result[0], 
            'nama': result[1],
            'email': result[2],
            'password': result[3],
            'alamat': result[4],
            'no_telepon': result[5],
            'jenis_kelamin': result[6]
            }
        return None
    except Exception as e:
        print(f"Error fetching user by ID {id}: {e}")
        return None

def create_user(nama,email,password,alamat,no_telepon,jenis_kelamin):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (nama,email,password,alamat,no_telepon,jenis_kelamin) VALUES (%s,%s,%s,%s,%s,%s)", (nama,email,password,alamat,no_telepon,jenis_kelamin,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False

def update_user(id_user,nama,email,password,alamat,no_telepon,jenis_kelamin):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user SET nama = %s ,email = %s,password = %s,alamat = %s,no_telepon = %s,jenis_kelamin = %s WHERE id_user = %s", (nama,email,password,alamat,no_telepon,jenis_kelamin,id_user))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error updating user ID {id_user}: {e}")
        return False

def delete_user(id_user):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM user WHERE id_user = %s", (id_user,))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error deleting user ID {id_user}: {e}")
        return False

def login(email, password):
    try:
        query = "SELECT * FROM user WHERE email = %s AND password = %s"
        print(f"Executing query: {query} with email={email}, password={password}")
        
        cur = mysql.connection.cursor()
        cur.execute(query, (email, password))
        user = cur.fetchone()
        cur.close()
        if user:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error during login query execution: {e}")
        return False