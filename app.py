from flask import Flask
# from flask_cors import CORS
from routes import penyakit,gejala,aturan,konsultasi,user
from db import init_mysql 

app = Flask(__name__)

init_mysql(app)

# CORS(app)


app.register_blueprint(penyakit.penyakit_bp, url_prefix='/penyakit')
app.register_blueprint(gejala.gejala_bp, url_prefix='/gejala')
app.register_blueprint(aturan.aturan_bp, url_prefix='/aturan')
app.register_blueprint(konsultasi.konsultasi_bp, url_prefix='/konsultasi')
app.register_blueprint(user.user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
