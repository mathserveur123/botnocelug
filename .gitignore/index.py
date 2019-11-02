import discord
from discord.ext import commands

TOKEN = '62BrPAOH_be1lIy_DnGV29sQIN5e9H88'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print('Bot is ready')


	
@client.event
async def on_message(message):
	author = message.author
	content = message.content
	print('{}: {}'.format(author, content))

channel = message.channel
lipide = 630
glucide = 630
proteine = 630
user = Client.get_user()


from threading import Thread, RLock
import time  as time

verrou = RLock()

class Afficheur(Thread):

 Thread.__init__(self)

def run(self):
	if message.content.startswith('Faim'+ user):
		with verrou:
			for i in range(25):
				t=0 
				tl=time.time()
				while t != 604800:
						t3=time.time()
						T=0
				while seconde != 604800/630:
						t4=time.time()
						seconde=t4-t3
						lipide =lipide - 1
						glucide = glucide - 1
						proteine = proteine - 1
				if lipide==0 or glucide==0 or proteine==0:
					tl=time.time()
					client.send_message("Mange vite quelque chose !")
					t2=time.time()
					t=t2-t1
				elif message.content.startswith('Faim'):
					client.send_message('Veuillez indiquer le nom du joueur.')
				else:
					pass
		
thread_1 = Afficheur(lipide, proteine, glucide)
thread_2 = Afficheur(lipide, proteine, glucide)
thread_3 = Afficheur(lipide, proteine, glucide)
thread_4 = Afficheur(lipide, proteine, glucide)
thread_5 = Afficheur(lipide, proteine, glucide)
thread_6 = Afficheur(lipide, proteine, glucide)
thread_7 = Afficheur(lipide, proteine, glucide)
thread_8 = Afficheur(lipide, proteine, glucide)
thread_9 = Afficheur(lipide, proteine, glucide)
thread_10 = Afficheur(lipide, proteine, glucide)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_9.start()
thread_10.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()
thread_9.join()
thread_10.join()

client.run(TOKEN)
