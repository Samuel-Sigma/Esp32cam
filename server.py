from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/latest.jpg")
def latest():
    path = os.path.join(UPLOAD_FOLDER, "latest.jpg")
    if os.path.exists(path):
        return send_file(path, mimetype="image/jpeg")
    return "No image uploaded yet"

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No image", 400

    image = request.files["image"]
    image.save(os.path.join(UPLOAD_FOLDER, "latest.jpg"))
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)