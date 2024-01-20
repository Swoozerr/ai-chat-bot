from flask import Flask, render_template, jsonify, request
import openai
from config import Config

app = Flask(__name__)
app.config.from_object(Config) 

# root path context
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html') # note, Flask by default looks in templates folder

# for running app.py when exectued, not when imported
if __name__ == "__main__":
    app.run(debug=True)