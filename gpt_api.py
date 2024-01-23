import dev_config
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

 #set api key

def defineBot(define):
    return None

def getResponse(query):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    
    # get question from func call
    question = {}
    question['role'] = 'user'
    question['content'] = query;
    messages.append(question)

    # send to gpt, get response 
    response = openai.Completion.create( engine="gpt-3.5-turbo", messages=messages)
    answer = response['choices'][0]['message']['content']

    #TODO
    if response['choices'][0]['finish_reason'] != 'stop':
        return "failed to acquire answer due to..."

    return answer



# documentation ...
"""
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
"""

#response
"""
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
      "logprobs": null
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
"""