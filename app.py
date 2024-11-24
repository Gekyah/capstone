from flask import Flask
# from flask_cors import CORS
from routes import penyakit,gejala,aturan
from db import init_mysql 

app = Flask(__name__)

init_mysql(app)

# CORS(app)


app.register_blueprint(penyakit.penyakit_bp, url_prefix='/penyakit')
app.register_blueprint(gejala.gejala_bp, url_prefix='/gejala')
app.register_blueprint(aturan.aturan_bp, url_prefix='/aturan')

if __name__ == '__main__':
    app.run(debug=True)
