mysql = None  # Placeholder to be set later

def init_mysql(app):
    global mysql
    from flask_mysqldb import MySQL
    mysql = MySQL(app)
