# GPT-4 Telegram Bot 🤖💬

A simple Telegram bot that leverages GPT-4 to provide conversational AI capabilities. This bot allows users to interact with the GPT-4 model directly through a Telegram chat interface.

## Features ✨

- **Conversational AI**: Chat with the GPT-4 model using natural language.
- **Telegram Integration**: Seamlessly interact with the bot via Telegram.

## Prerequisites 📋

Before you begin, make sure you have the following:

- **Python 3.6+** installed
- A **Telegram Bot Token**. You can obtain this by creating a new bot on [BotFather](https://core.telegram.org/bots#botfather).

## Getting Started 🚀

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hosseingz/IntelliBot.git
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   - Create a `.env` file in the project root directory:
     ```bash
     touch .env
     ```
   - Add your API key to the `.env` file:
     ```
     api_key="set_your_apikey_here"
     ```

5. **Run the bot**:
   ```bash
   python main.py
   ```


### Running on Google Colab 🚀

You can also run this project on Google Colab by following these steps:

1. **Clone the repository**:
   ```python
   !git clone https://github.com/hosseingz/IntelliBot.git
   ```

2. **Install dependencies**:
   ```python
   !pip install -r /content/IntelliBot/requirements.txt
   ```

3. **Set up environment variables**:
   ```python
   import os
   os.environ['api_key'] = 'your_openai_api_key_here'  # Replace with your actual API key
   ```

4. **Run the bot**:
   ```python
   !python /content/IntelliBot/main.py
   ```

Now, your bot should be up and running on Colab! You can start chatting with it on Telegram using the bot's username.


## Usage 📝

1. **Start a chat with your bot** on Telegram by searching for its username.
2. **Send a message** to the bot, and it will respond using GPT-4.
3. If there are any server issues, the bot will notify you to try again.

## Project Structure 🗂️

- `main.py`: The main script that runs the Telegram bot.
- `.env`: Environment file for storing the API key (not included in version control for security).
- `.gitignore`: Specifies files and directories to be ignored by Git.


## Security Considerations 🔒

- **Do not share your API key** or `.env` file.
- Make sure to **add `.env` to your `.gitignore`** to prevent it from being tracked by Git.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project.
2. Create a new branch for your feature or bugfix.
3. Submit a Pull Request for review.

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.
