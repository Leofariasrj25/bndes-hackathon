import keys
from telegram.ext import *
from telegram import Update
import responses as r

print("Bot started...")

data = dict()
def get_id(update):
	return update.message.chat.id

def create_fields(id):
	global data
	data[id] = {'nome': '', 'cpf': '', 'estado' : '', 'renda' : '', 'maturidade' : False}

def start_command(update, context):
	update.message.reply_text("Olá! Fico muito feliz em ver que você quer investir no seu negócio. Se você deseja se cadastrar digite 'cadastrar' para iniciar o processo (utilize dados fictícios para testar o bot 😊)")
	create_fields(get_id(update))
	print(data)

def help_command(update, context):
	update.message.reply_text("Por enquanto eu sou só um protótipo e só cadastro as pessoas. Digite 'cadastrar' para iniciar o processo de cadastro")

def handle_message(update, context):
	text = str(update.message.text).lower()
	response = r.sample_responses(text)
	update.message.reply_text(response)
	print(update.message.chat.id)

def error(update, context):
	print(f"Update {update} caused error {context.error}")

def main():
	updater = Updater(keys.API_KEY, use_context = True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

main()
