from telegram import Update
from telegram.ext import CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Soy el BotTele nombre provisional :D')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Contesto a los comandos: \n /start -> Empiezo a funcionar \n /hello -> Te saludo\n /memaso -> Te envio un meme\n /help -> Lo que estas viendo')