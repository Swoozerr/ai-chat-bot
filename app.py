from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# root path context
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')