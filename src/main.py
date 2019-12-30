import os

from mongoengine import connect

from telegram.ext import CommandHandler, CallbackQueryHandler

from bot import Bot

from handlers.start import start_handler
from handlers.submit import submit_handler
from handlers.play_out import play_out_handler


if __name__ == '__main__':
    connect(host=os.environ.get('DATABASE_URI'))
    connect(host=os.environ.get('YANDEX_MUSIC_BOT_DATABASE_URI'), alias='yandex-music-bot')
    bot = Bot(os.environ.get('BOT_TOKEN'))

    handlers = [
        CommandHandler('start', start_handler),

        CommandHandler('play_out', play_out_handler),

        CallbackQueryHandler(start_handler, pattern='^main$'),
        CallbackQueryHandler(submit_handler, pattern='^submit$')
    ]
    bot.register_handler(handlers)

    bot.start()
