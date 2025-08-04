from flask import Flask, render_template, request
import os
import base64
from datetime import datetime

app = Flask(__name__)

# Folder to save images
SAVE_DIR = "static/captured"
os.makedirs(SAVE_DIR, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/capture', methods=['POST'])
def capture():
    data = request.json['image']
    image_data = data.split(',')[1]
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    filepath = os.path.join(SAVE_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(base64.b64decode(image_data))

    return {'status': 'success', 'filename': filename}


if __name__ == '__main__':
    app.run(debug=True)