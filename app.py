from flask import Flask, request, jsonify
import cv2
import numpy as np
import torch
from PIL import Image
import io

app = Flask(__name__)

# Load YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "custom", path="yolov5s.pt", force_reload=True)

@app.route("/detect_currency", methods=["POST"])
def detect_currency():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Read the image
    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read()))

    # Run YOLO detection
    results = model(image)

    # Extract detected objects
    detected_objects = results.pandas().xyxy[0].to_dict(orient="records")

    return jsonify({"detected_currency": detected_objects})

if __name__ == "__main__":
    app.run(debug=True)
