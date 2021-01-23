import bot_functions.basics
import bot_functions.reddit

from telegram.ext import Updater, CommandHandler

updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('hello', bot_functions.basics.hello))
updater.dispatcher.add_handler(CommandHandler('start', bot_functions.basics.start))
updater.dispatcher.add_handler(CommandHandler('memaso', bot_functions.reddit.memaso))
updater.dispatcher.add_handler(CommandHandler('help', bot_functions.basics.help))

updater.start_polling()
updater.idle()