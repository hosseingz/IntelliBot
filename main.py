import telebot
import dotenv
import g4f
import os

dotenv.load_dotenv()

api_key = os.environ.get('api_key')
bot = telebot.TeleBot(api_key)

def ask_gpt(prompt):
    try:
        response = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content':prompt}]
        )
        return response
    
    except Exception as e:
        return "There is a problem with the server, please try again later."


@bot.message_handler(commands=['start'])
def handle_start(message):
    greeting_message = (
        "Hello! 👋\n"
        "Welcome to the Bot project. This bot allows you to chat with an AI and receive responses based on your messages.\n"
        "You can ask me anything!\n"
        "For more details and the source code, please check my GitHub project: [GitHub Link](https://github.com/hosseingz/IntelliBot.git)"
    )
    
    bot.reply_to(message, greeting_message)


@bot.message_handler(func=lambda message:True)
def handle_message(message):
    user_message = message.text
    
    bot.reply_to(message, "Processing ...")
    
    try:
        response = ask_gpt(user_message)
        bot.reply_to(message, response)
    except:
        bot.reply_to(message, "There is a problem, Try again !")
    
if __name__ == '__main__':
    bot.polling()