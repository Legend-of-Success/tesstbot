from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
# print(bot.get_me())

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm Ali's bot, please talk to me and I will tell him!")

def echo(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
	# bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
	# s = "Message From:"+ str(update.message.chat_id)+"\n 	"+ str(update.message.text)
	# print(s)
	# answer = str(raw_input("Send answer: "))
	

def resp(bot, update):
	myID = 74174159
	if update.message.chat_id != myID:
		bot.send_message(myID, text=update.message.text)
		bot.send_message(myID, text=str(update.message.chat_id))
	else:
		l = update.message.text.split()
		recieverID = int(l[0])
		del l[0]
		answer = ''.join(l)
		bot.send_message(int(recieverID), answer)
		

updater = Updater(token='291616496:AAHyk2ZmC6o1g2P6FuJRnW6v8m5J7C42-dI')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()