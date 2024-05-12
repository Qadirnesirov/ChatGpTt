from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# ChatGPT API anahtarını buraya yerleştirin
openai.api_key = 'YOUR_OPENAI_API_KEY'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot başlatıldı. Hoş geldiniz!')

def echo(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    # ChatGPT ile cevap oluşturma
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
        max_tokens=150
    )
    bot_response = response.choices[0].text.strip()
    update.message.reply_text(bot_response)

def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
