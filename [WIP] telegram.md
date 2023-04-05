# Telegram Bot

## Brief

The objective of this project is to get some hands on experience in applying the knowledge we have learnt about Python.

## Part 1: Setting up your project

### Objectives

1. Set up your Telegram bot's administrative details
2. Set up your codebase

### Obtain your Token

Follow the instructions on [Telegram's documentation](https://core.telegram.org/bots/features#botfather) on obtaining a token for your bot.

### Initialise workspace

Set up the Python virtual environment

```bash
python3 -m venv venv
```

This will set up a virtual environment called `venv` in the current directory.

Once that has been set up, we need to activate it

```bash
source venv/bin/activate
```

This loads the virtual environment by loading a script from `venv/bin/activate` created in the previous step.

### Install necessary packages

We will primarily be working with

- python-telegram-bot
- requests

We will need the following for importing environment variables to store our token

- python-dotenv

In addition to those, we will also need the following for formatting and linting

- autopep8
- pylint

```bash
pip install python-telegram-bot requests python-dotenv autopep8 pylint
```

### Create `main.py`

Create a folder called `src` and create a file `main.py` within it

```bash
mkdir src

cd src

touch main.py
```

### Create `.gitignore`

Create a `.gitignore` file in the root directory with the following content

```
__pycache__/
venv/
.vscode/

.DS_Store
.env
```

This ensures that there will be no sensitive or temporary files uploaded to our code repo in the next step.

### Initialise code repository

Create a new repository on Github and follow the instructions to push your code there.

## Part 2: Testing your bot

### Objectives

Set up a simple echo bot and test it

### Create a `.env` and `.env.example` file

#### `.env.example`

In the root directory, create a file `.env.example` with the following

```
TOKEN=YOUR_TOKEN
```

This is the template file to let users know what other information needs to be supplied for your code to work.

Since it will be uploaded to the repo, we do not want to populate this with any sensitive information.

#### `.env`

In the root directory, create a file `.env` and replace `YOUR_TOKEN` with your own.

```
TOKEN=YOUR_TOKEN
```

This file is where sensitive information is stored, separate from the actual code itself.

As we have already specified for this file in `.gitignore`, any changes to it will be ignored by `git` and we do not need to worry about any information leakage.

### Populate `main.py`

Copy the example code [from the python-telegram-bot repo](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot.py)

### Load your token

At the bottom of our imports, add the following

```python
from dotenv import load_dotenv

load_dotenv()
```

And in the `main` function, replace the placeholder string `"TOKEN"` with `os.getenv('BOT_TOKEN')`

```python
# Create the Application and pass it your bot's token.
bot_token = os.getenv('BOT_TOKEN')
application = Application.builder().token(bot_token).build()
```

`load_dotenv()` loads your token as an environment variable, and the value is loaded to your app using `os.getenv`.

Any subsequent changes to the token will not require us to make any changes to the code at all.

### Run the code to test the bot

As explained in the code's usage instructions, the bot should echo whatever message it receives.

Run the bot, and send it a message using the Telegram app.

Your bot should reply with the exact message you send it.

## Part 3: Working with APIs

- Check out the documentation

## Part 4: Adding placeholder commands

- Add basic `/commands`
- Might want to swap parts 3 and 4

## Part 5: Giving functionality to your bot

- Integrate with APIs

## Part 6: Running your bot from the command line

## Part 7: Running your bot on another system
