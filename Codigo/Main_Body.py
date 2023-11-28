import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True



import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


stopwords = set(stopwords.words('english'))
greetings = [
    'hi', 'hey', 'hello', 'good morning', 'good afternoon', 'good evening', 'greetings',
    'what\'s up', 'howdy', 'hey there', 'yo', 'hi there', 'hiya', 'hey hey', 'sup',
    'how\'s it going', 'hi friend', 'hola', 'bonjour', 'ciao', 'hey dude'
]

responses = {
    'hi': 'Heyyy!',
    'hey': 'Hello there!',
    'hello': 'Hi! How can I assist you?',
    'good morning': 'Good morning! How can I help you today?',
    'good afternoon': 'Good afternoon! What can I do for you?',
    'good evening': 'Good evening! Ready for a chat?',
    'greetings': 'Greetings! What\'s on your mind?',
    'what\'s up': 'Not much, just here and ready to chat. What\'s up with you?',
    'howdy': 'Howdy! Ready for a good conversation?',
    'yo': 'Yo! What\'s going on?',
    'hi there': 'Hello! How can I brighten your day?',
    'hiya': 'Hiya! Ready to talk about anything?',
    'hey hey': 'Hey hey! What\'s the latest?',
    'sup': 'Sup! Anything exciting happening?',
    'how\'s it going': 'It\'s going well, thanks for asking! How about you?',
    'hi friend': 'Hello, friend! What brings you here?',
    'hey dude': 'Hey dude! What\'s on your mind?',
    'how are you': 'I\'m doing well, thanks for asking!',
    'tell me a joke': 'Why don\'t scientists trust atoms? Because they make up everything!',
    'what is your favorite color': 'I like all colors, but if I had to choose, I\'d say dragon green!',


    'how are you': 'Never get bad',
    'I\'m fine': 'Nice nice',
    'Cool': 'Nice nice',

}




class MyClient(discord.Client):
	async def on__ready(self):
		print('Logged on as {0}'.format(self.user))

	async def on_message(self,message):
		print('Message from {0.author}: {0.content}'.format(message))
		box =  word_tokenize(message.content)
		sentence = sent_tokenize(message.content)
		words = StopWords(box, sentence)
		for greeting in greetings:
			if greeting in message.content and 'tohru' in words:
				await message.channel.send('{}'.format(responses[greeting]))
#			await message.channel.send(f'responses{greeting}')
#		for i in range(len(words)):
#			words[i] = words[i].upper()
#			if words[i] in ['HI', 'HEY'] or words[i] == ['GOOD'] and words[i+1] == ["MORNING"]:
#				for j in words:
#					if j.upper() == 'TOHRU':
#						await message.channel.send(f'Heyyy {message.author.name}')



def StopWords(wrds, sentences):
	final_text = []
	for w in wrds:
		if w not in stopwords:

			final_text.append(w.lower())
	print("texto processado {} \n {}".format(final_text, sentences))
	return final_text
##                      await message.channel.send(f'salveee {message.author.name}')



#MAIN CODE
if __name__ == "__main__":
	client = MyClient(intents=intents)
	client.run('MTA3NzYyNDMzMTc0OTgxODM5OA.Gdz2ex.rm-wKxtxrAPNJ-XpdeIXB3YeWl05qDAWA6brLU')
