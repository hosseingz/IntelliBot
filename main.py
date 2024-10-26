import dotenv
import g4f
import os

dotenv.load_dotenv()

api_key = os.environ.get('api_key')
bot = telebot.Telebot(api_key)

def ask_gpt(prompt):
    try:
        response = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content':prompt}]
        )
        return response
    
    except Exception as e:
        return "There is a problem with the server, please try again later."

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
    