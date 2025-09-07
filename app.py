from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@Unknown_person0256'


if __name__ == "__main__":
    app.run()
