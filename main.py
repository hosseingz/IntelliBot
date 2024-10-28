import telebot
import dotenv
import g4f
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the API key for the Telegram bot from the environment variable
api_key = os.environ.get('api_key')
bot = telebot.TeleBot(api_key)

def ask_gpt(prompt):
    """Communicates with the GPT-4 AI model to get a response based on the user prompt.
    
    Args:
        prompt (str): The message or question to send to the AI model.
    
    Returns:
        str: The AI's response to the prompt or an error message if the request fails.
    
    Raises:
        Exception: If there is an issue with querying the AI model, an appropriate error message is returned.
    """
    try:
        # Request completion from the ChatCompletion API
        response = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response
    
    except Exception as e:
        # Handle exceptions and return an error message
        return "There is a problem with the server, please try again later."


@bot.message_handler(commands=['start'])
def handle_start(message):
    """Handles the /start command, providing a welcome message to the user.
    
    Args:
        message (telebot.types.Message): The incoming message object that triggered this command.
    
    Returns:
        None: Sends a welcome message to the user.
    """
    greeting_message = (
        "Hello! 👋\n"
        "Welcome to the Bot project. This bot allows you to chat with an AI and receive responses based on your messages.\n"
        "You can ask me anything!\n"
        "For more details and the source code, please check my GitHub project: https://github.com/hosseingz/IntelliBot.git"
    )
    
    # Reply to the user with the greeting message
    bot.reply_to(message, greeting_message)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Processes incoming messages from users and interacts with the AI model.
    
    Args:
        message (telebot.types.Message): The incoming message object from the user.
    
    Returns:
        None: Sends processing status or AI response back to the user.
    
    If the AI model fails to respond or if there is an internal problem, an error message is sent to the user.
    """
    user_message = message.text
    
    # Notify the user that their message is being processed
    bot.reply_to(message, "Processing ...")
    
    try:
        # Ask the GPT model for a response to the user's message
        response = ask_gpt(user_message)
        bot.reply_to(message, response)
    except:
        # Handle any exceptions that occur during the message processing
        bot.reply_to(message, "There is a problem, Try again !")
    
if __name__ == '__main__':
    # Begin polling for new messages for the bot
    bot.polling()