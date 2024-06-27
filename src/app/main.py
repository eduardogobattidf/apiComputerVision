from flask import Flask,request, jsonify
from flask_cors import CORS
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.tools.torch_category import ImageClassifier
classifier = ImageClassifier()

app = Flask("DFvision")
app = Flask(__name__)
app.config['SEND_TIMEOUT'] = 180

# Rota para o index (menu)
@app.route('/', methods=['GET'])
def index():
    return "It's live"


# Rota para o AI Product Enrichment
@app.route('/verificaImage', methods=['POST'])
def verificaImage():
    data = request.json

    image_url = data['image_url']
    predicted_class = classifier.predict(image_url)
    print(predicted_class)
    if not image_url:
            return jsonify({'error': 'No image_url provided'}), 400
    predicted_class = classifier.predict(image_url)
    return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    cors = CORS(app, resources={r"": {"origins": ""}})
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)