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
		return "Perfeito! Vamos iniciar o seu cadastro! ^_^ Eu sou a Maria. E você, como se chama?"
	elif data['pergunta'] == 1:
		if has_numbers(user_message):
			data['pergunta'] = 1
			return "Nem eu que sou uma robô tenho números no meu nome. o__O Seu nome completo, como consta na identidade por favor."
		else:
			data.update({'nome':user_message})
			data['pergunta'] += 1
			return "Agora o CNPJ da empresa, mas sem pontos nem traços, por favor. :-)"
	elif data['pergunta'] == 2:
		if user_message.isdigit() is False:
			data['pergunta'] = 2
			return "Somente os dígitos do seu CNPJ, por favor. Sem pontos nem traços."
		else:
			data.update({'CNPJ': user_message})
			data['pergunta'] += 1
			return "Vamos te conectar a uma instituição próxima de onde você está. Qual é a sigla do estado? Por exemplo: RJ, CE, DF…"
	elif data['pergunta'] == 3:
		if user_message in ("rj, sp, es, mg, pr, sc, rs, ms, go, ac, al, ap, am, ba, ce, df, ma, mt, pa, pb, pe, pi, rn, ro, rr, se, to"):
			data.update({'estado': user_message})
			data['pergunta'] += 1
			return "É um lugar lindo! \*___\* Já estamos na metade! Qual é a sua renda mensal em reais? Por exemplo: 1000."
		else:
			data['pergunta'] == 3
			return "Não reconheço esse estado. Não tem no Brasil. x__x Digite a sigla de um dos estados ou do Distrito Federal."
	elif data['pergunta'] == 4:
		if user_message.isdigit() is False:
			data['pergunta'] = 4
			return "Somente os dígitos, por favor. Sem cifras, sem centavos e sem vírgula. ;-)"
		else:
			data.update({'renda': user_message})
			data['pergunta'] += 1
			return "Agora me conta… $___$ Qual valor em reais você procura? Por exemplo: 4000."
	elif data['pergunta'] == 5:
		if user_message.isdigit() is False:
			data['pergunta'] = 5
			return "Somente os dígitos, por favor. Sem cifras, sem centavos e sem vírgula. ;-)"
		else:
			data.update({'credito': user_message})
			data['pergunta'] += 1
			return "Está acabando! Você foi indicado por alguém? Caso sim, digite o código de identificação de quem te indicou. Se não for o caso, por favor, digite \"não\"."
	elif data['pergunta'] == 6:
			data.update({'indicador': user_message})
			data['pergunta'] += 1
			return "Para terminar! Você possui MEI a mais de seis meses? Responda com \"sim\" ou \"não\"."
	elif data['pergunta'] == 7:
		data['pergunta'] = -1
		if user_message in ("sim", "s"):
			data.update({'maturidade': True})
		else:
			data.update({'maturidade': False})
		print(data)
		return "Prontinho! Já terminamos! Obrigada pelas respostas. Agora vamos conectar você à instituição que mais combina com o seu perfil. Aguarde o retorno deles em alguns dias, beleza? Abraços, vou ficando por aqui! :-D"
	if user_message in ("oi", "ola", "olá"):
		return "Olááá! :-D"
