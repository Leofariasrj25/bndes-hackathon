from telegram.ext import *

# Verificação de digitos
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

# Verificação de letras
def has_alpha(inputString):
    return any(char.alpha() for char in inputString)

# Logica responsável por selecionar as respostas. Ela toma como input
# a resposta do usuário e verifica se não tem nenhum erro grotesco.
# Caso esteja tudo ok, o usuário recebe a próxima pergunta, caso contrário,
# uma mensagem de erro é exibida até que ele coloque uma resposta adequada.
def sample_responses(input_text, data):
	user_message = str(input_text).lower()


	if "cadastr" in user_message:
		data['pergunta'] = 1
		return "Vamos iniciar o seu cadastro. Qual é o seu nome?"
	elif data['pergunta'] == 1:
		if has_numbers(user_message):
			data['pergunta'] = 1
			return "Numeros não sao permitidos! Tente novamente."
		else:
			data.update({'nome':user_message})
			data['pergunta'] += 1
			return "Digite seu CNPJ (Sem pontos ou traços)"
	elif data['pergunta'] == 2:
		if user_message.isdigit() is False:
			data['pergunta'] = 2
			return "Seu CNPJ deve conter apenas digitos! Tente novamente."
		else:
			data.update({'CNPJ': user_message})
			data['pergunta'] += 1
			return "Qual estado(Sigla) você reside: Ex: RJ, CE, SC ..."
	elif data['pergunta'] == 3:
		if user_message in ("rj, sp, es, mg, pr, sc, rs, ms, go, ac, al, ap, am, ba, ce, df, ma, mt, pa, pb, pe, pi, rn, ro, rr ,se, to"):
			data.update({'estado': user_message})
			data['pergunta'] += 1
			return "Qual sua renda bruta mensal em reais? Ex: 1000"
		else:
			data['pergunta'] == 3
			return "Digite uma Sigla Válida"
	elif data['pergunta'] == 4:
		if user_message.isdigit() is False:
			data['pergunta'] = 4
			return "Esse valor deve conter apenas digitos! Tente novamente."
		else:
			data.update({'renda': user_message})
			data['pergunta'] += 1
			return "Quando é o valor do crédito que você procura em reais? ex: 4000"
	elif data['pergunta'] == 5:
		if user_message.isdigit() is False:
			data['pergunta'] = 5
			return "Esse valor deve conter apenas digitos! Tente novamente."
		else:
			data.update({'credito': user_message})
			data['pergunta'] += 1
			return "Houve indicação? Caso sim, Digite o id do(a) indicador(a), caso não, digite 'não'."
	elif data['pergunta'] == 6:
			data.update({'indicador': user_message})
			data['pergunta'] += 1
			return "Possui MEI a mais de 6 meses?"
	elif data['pergunta'] == 7:
		data['pergunta'] = -1
		if user_message in ("sim", "s"):
			data.update({'maturidade': True})
		else:
			data.update({'maturidade': False})
		print(data)
		return "Obrigado Pelas Respostas!"
	if user_message in ("oi", "ola", "olá"):
		return "Olááá!"