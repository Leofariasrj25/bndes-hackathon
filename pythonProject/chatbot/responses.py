

def sample_responses(input_text):
	user_message = str(input_text).lower()

	if user_message in ("oi", "ola", "olá"):
		return "Olááá!"
	elif user_message in ("cadastro"):
		return "Qual é o seu nome?"
	
