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


class MyClient(discord.Client):
	async def on__ready(self):
		print('Logged on as {0}'.format(self.user))

	async def on_message(self,message):
		print('Message from {0.author}: {0.content}'.format(message))
		box =  word_tokenize(message.content)
		sentence = sent_tokenize(message.content)
		words = StopWords(box, sentence)
		for i in range(len(words)):
			words[i] = words[i].upper()
			if words[i] in ['HI', 'HEY'] or words[i] == ['GOOD'] and words[i+1] == ["MORNING"]:
				for j in words:
					if j.upper() == 'TOHRU':
						await message.channel.send(f'Heyyy {message.author.name}')



def StopWords(wrds, sentences):
	final_text = []
	for w in wrds:
		if w not in stopwords:

			final_text.append(w)
	print("texto processado {} \n {}".format(final_text, sentences))
	return final_text
##                      await message.channel.send(f'salveee {message.author.name}')



#MAIN CODE
if __name__ == "__main__":
	client = MyClient(intents=intents)
	client.run('Your Token Id')
