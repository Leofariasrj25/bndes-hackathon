import os
from telegram.ext import *
from telegram import Update
import json
import responses as r

print("Bot started...")

data = dict()

# pega o id do usuário que esta se comunicando com o bot no momento
def get_id(update):
	return update.message.chat.id

# inicializa dicionario com as categorias das respostas
def create_fields(id):
	global data
	data[id] = {'pergunta' : 0, 'nome': '', 'CNPJ': '', 'estado' : '', 'renda' : '', 'credito' : '', 'maturidade' : False}

# quando o comando /start é solicitado
def start_command(update, context):
	global data
	update.message.reply_text("Olá! Fico muito feliz em ver que você quer investir no seu negócio. Se você deseja se cadastrar digite 'cadastro' para iniciar o processo (utilize dados fictícios para testar o bot 😊)")
	create_fields(get_id(update))

# quando o comando /hellp é solicitado
def help_command(update, context):
	update.message.reply_text("Por enquanto eu sou só um protótipo e só cadastro as pessoas. Digite 'cadastro' para iniciar o processo de cadastro")

# Função para lidar com as diferentes mensagens recebidas
def handle_message(update, context):
	text = str(update.message.text).lower()
	response = r.sample_responses(text, data[get_id(update)])
	update.message.reply_text(response)
	print(update.message.chat.id)
	print(data[get_id(update)]['pergunta'])
	if data[get_id(update)]['pergunta'] == -1:
		update.message.reply_text(json.dumps(data[get_id(update)]))

# printa o erro no terminal e seu contexto no terminal
def error(update, context):
	print(f"Update {update} caused error {context.error}")

def main():
	updater = Updater(os.environ['API_KEY'], use_context = True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

main()
