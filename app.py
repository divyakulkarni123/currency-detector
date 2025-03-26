import time
import requests
import torch

def download_file(url, filename):
    for attempt in range(5):  # Retry up to 5 times
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error if request fails
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)  # Wait 5 seconds before retrying
    print("Failed to download file after 5 attempts.")

# Example: Download model file if it's missing
model_url = "https://your-download-link.com/best.pt"  # Replace with actual URL
model_path = "best.pt"

if not os.path.exists(model_path):
    download_file(model_url, model_path)

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False)

import time

for attempt in range(5):  # Retry up to 5 times
    try:
        response = requests.get("https://your-api-url.com")
        response.raise_for_status()
        data = response.json()
        break  # Exit loop if successful
    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt+1} failed: {e}")
        time.sleep(5)  # Wait 5 seconds before retrying
        
import os
import gdown

file_id = "YOUR_FILE_ID"
output = "best.pt"

if not os.path.exists(output):
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

model = torch.hub.load('ultralytics/yolov5', 'custom', path=output, force_reload=False)

