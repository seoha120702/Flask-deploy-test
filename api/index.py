from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '배포 성공'