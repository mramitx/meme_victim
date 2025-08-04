from flask import Flask, render_template, request
import os
import base64
from datetime import datetime

app = Flask(__name__)
PHOTO_FOLDER = 'static/captured'
os.makedirs(PHOTO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data_url = request.form['image']
    if data_url.startswith('data:image'):
        image_data = base64.b64decode(data_url.split(',')[1])
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{PHOTO_FOLDER}/photo_{timestamp}.jpg"
        with open(filename, 'wb') as f:
            f.write(image_data)
        return 'Success'
    return 'Failed', 400

if __name__ == '__main__':
    app.run(debug=True)
