from telegram import Update
from telegram.ext import CallbackContext

def memaso(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Te enviaria el buen memaso pero aun no me conecto con Reddit :(')