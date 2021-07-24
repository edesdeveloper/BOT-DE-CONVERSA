from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot=ChatBot('ENIAC')

conversa=['oi', 'Olá', 'tudo bem?', 'Eu estou bem e você?', 'qual é o seu filme favorito?', 'Vingadores', 'como é seu nome?', 'Meu nome é Eniac']
conversa2=['como foi seu dia?', 'Foi bem', 'quem é você?', 'Sou um robô criado por Edes Lázaro para conversar com as pessoas, fui desenvolvido em Python usando Machine Learning']

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)

while True:
	try:
		quest=input("Você: ")
		resposta=bot.get_response(quest)
		if float(resposta.confidence)>0.5:
			print ("Eniac: ", resposta)
		else:
			print ("Eniac: Desculpe, não conseguir entender.")
	except(KeyboardInterrupt, EOFError, SystemExit):
		break
