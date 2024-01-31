# AI Chat Bot
This chat bot is an AI-driven chat bot powered by OpenAI's language models, specifically utilizing their chat completions API (found [here] (https://platform.openai.com/docs/guides/text-generation/chat-completions-api)). Ask the bot anything you like and an answer will be sent back in seconds.

## How to start:
### Update pip
pip install --upgrade pip

### Create a virtual environment 
python -m venv venv

### Activate the virtual environment (make sure you have admin privileges on your system)
- On Windows
venv\Scripts\activate
- On macOS/Linux
source venv/bin/activate

###  Install flask
pip install flask

###  Install OpenAi Api
pip install openai

###  Running the App
1. set up config by grabbing your OpenAI API key after creating an OpenAi Account
2. run python app.py in terminal to initialize flask app on a dev server

## Migrating to new OpenAI Version
abridged from https://github.com/openai/openai-python/discussions/742

### Upgrade to newest version
pip install --upgrade openai

### Migrate using grit
- On macOS/Linux
openai migrate

- On Windows
(taken from docs directly)
Automatic migration with grit on Windows
To use grit to migrate your code on Windows, you will need to use Windows Subsystem for Linux (WSL). Installing WSL is quick and easy, and you do not need to keep using Linux once the command is done.

Here's a step-by-step guide for setting up and using WSL for this purpose:

Open a PowerShell or Command Prompt as an administrator and run wsl --install.
Restart your computer.
Open the WSL application.
In the WSL terminal, cd into the appropriate directory (e.g., cd /mnt/c/Users/Myself/my/code/) and then run the following commands:
curl -fsSL https://docs.grit.io/install | bash
grit install
grit apply openai
Then, you can close WSL and go back to using Windows.

### openai should be installed in your venv now
