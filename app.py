from flask import Flask, render_template, request, jsonify
from seguir import app as seguir_app
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(seguir_app)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
