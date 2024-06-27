from flask import Flask,request, jsonify
from flask_cors import CORS
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

app = Flask(__name__)

CORS(app)



# Rota para o index (menu)
@app.route('/', methods=['GET'])
def index():
    return "It's live"


# Rota para o AI Product Enrichment
@app.route('/verificaImage', methods=['POST'])
def ai_product_enrichment():
    return 'ai_product_enrichment'


if __name__ == '__main__':
    app.run(port=5000, debug=True)