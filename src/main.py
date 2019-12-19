import os

from mongoengine import connect

from telegram.ext import CommandHandler

from bot import Bot

from handlers.start import start_handler


if __name__ == '__main__':
    connect(host=os.environ.get('DATABASE_URI'))
    bot = Bot(os.environ.get('BOT_TOKEN'))

    handlers = [
        CommandHandler('start', start_handler)
    ]
    bot.register_handler(handlers)

    bot.start()
