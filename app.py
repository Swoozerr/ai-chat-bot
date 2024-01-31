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
    data = request.get_json() # get json data from ajax
    
    if data and 'query' in data:
        message = data['query']
        answer = gpt_api.getResponse(message) # get gpt response using method from gpt_api
        
        # create json object with 'answer: generated answer' pair and return to ajax call
        response = {'answer': answer}
        return jsonify(response)
    
# for running app.py when exectued, not when imported
if __name__ == "__main__":
    app.run(debug=True)