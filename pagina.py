from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenido a mi página</h1>"

@app.route("/hello")
def hello():
    return "<p>Hola</p>"