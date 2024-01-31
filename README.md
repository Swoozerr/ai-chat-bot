# AI Chat Bot
This chat bot is an AI-driven chat bot powered by OpenAI's language models, specifically utilizing their chat completions API (found [here](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)). Ask the bot anything you like and an answer will be sent back in seconds.

## How to start:
### Update pip
```python
pip install --upgrade pip
```

### Create a virtual environment 
```python
python -m venv venv
```

### Activate the virtual environment (make sure you have admin privileges on your system)
- *On Windows*:
```python
venv\Scripts\activate
```
- *On macOS/Linux*:
```python
source venv/bin/activate
```

###  Install flask
```python
pip install flask
```

###  Install OpenAi Api
```python
pip install openai
```

##  Running the App
1. Set up config by grabbing your OpenAI API key after creating an OpenAI account
2. Run python app.py in terminal to initialize flask app on a dev server

# Migrating to new OpenAI Version **if Needed**
If OpenAI cannot be installed or is out of date, please read the OpenAI v1.0.0 migration guide post found [here](https://github.com/openai/openai-python/discussions/742)


