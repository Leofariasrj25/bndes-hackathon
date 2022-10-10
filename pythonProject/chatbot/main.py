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
	data[id] = {'pergunta' : 0, 'nome': '', 'CNPJ': '', 'estado' : '', 'renda' : '', 'credito' : '', 'indicador' : '', 'maturidade' : False}

# quando o comando /start é solicitado
def start_command(update, context):
	global data
	update.message.reply_text("Oi! Eu sou a Maria. Fico muito feliz em ver que você quer investir no seu negócio. :-D Estou aqui para te ajudar. Se você desejar, digite \"cadastro\" para iniciar o processo. Lembrando que o pré-cadastro não é garantia de acesso nem liberação de crédito, tá? ;-)")
	create_fields(get_id(update))

# quando o comando /help é solicitado
def help_command(update, context):
	update.message.reply_text("Então, por enquanto sou só um protótipo, realizo apenas o pré-cadastro das pessoas. Digite 'cadastro' se deseja iniciar o processo.")

# salva as respostas num arquivo
def save_file(data, user_id):
	user_file = open(str(user_id), 'w')
	user_file.write(json.dumps(data[user_id]))
	user_file.flush()
	user_file.close()

# Função para lidar com as diferentes mensagens recebidas
def handle_message(update, context):
	text = str(update.message.text).lower()
	response = r.sample_responses(text, data[get_id(update)])
	update.message.reply_text(response)
	print(update.message.chat.id)
	print(data[get_id(update)]['pergunta'])
	if data[get_id(update)]['pergunta'] == -1:
		update.message.reply_text(json.dumps(data[get_id(update)]))
		save_file(data, get_id(update))

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
