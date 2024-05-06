from flask import Flask, request, jsonify
from deepface import DeepFace
import numpy as np
import cv2
import base64

app = Flask(__name__)

# ... your facial expression detection code here ...


@app.route('/detect_emotions', methods=['POST'])
def detect_emotions():
    # Get base64 string from the request
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({"error": "No image provided"}), 400

    # Decode the image from base64
    img_str = data['image']
    img_data = base64.b64decode(img_str)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Analyze emotions with DeepFace
    try:
        emotions = DeepFace.analyze(img, actions=['emotion'])
        return jsonify({'emotions': emotions['emotion']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)