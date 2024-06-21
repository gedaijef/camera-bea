from flask import Flask, render_template, render_template_string, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)