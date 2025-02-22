from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(f"/uploads/{file.filename}")  # No file type check
    return "File uploaded!"

app.run()
