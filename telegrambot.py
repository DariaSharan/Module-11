import requests
from telegram.ext import Updater, CommandHandler, MessageHandler

def search_gifs(search_query):
    api_key = 'BYAObLWHDa3LwtWMgg2Jat3uhEu000Yh'
    url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_query}&limit=5'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return [gif['images']['original']['url'] for gif in data['data']]
    else:
        return None

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the GIF search bot!")

def search(update, context):
    search_word = update.message.text
    gifs = search_gifs(search_word)
    
    if gifs:
        for gif_url in gifs:
            context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_url)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error occurred while searching for GIFs.")

def main():
    updater = Updater('6383541965:AAGCKMjyPq9l90lg8kbDEgVoUGSs1625al8')
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(lambda update: update.message.text, search))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()