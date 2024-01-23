from flask import Flask, render_template, jsonify, request
import gpt_api
from config import Config


app = Flask(__name__)
app.config.from_object(Config) 

#default get, return template
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html') # note, Flask by default looks in templates folder

# handle ajax question call to ask a question
@app.route('/', methods=['POST'])
def post_index():
    data = request.form.get('query')  # get data from ajax
    answer = gpt_api.getResponse(data) # use getResponse method to get response from openAI given query

    # create json obj with 'answer:generated answer' pair and return to ajax call
    response = {}
    response['answer'] = answer
    return jsonify(response)    

# for running app.py when exectued, not when imported
if __name__ == "__main__":
    app.run(debug=True)