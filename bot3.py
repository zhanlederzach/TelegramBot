# -*- coding: utf-8 -*-
import config
import sys
import telebot
import os, sys
# from telebot import types

# bot = telebot.TeleBot('741952009:AAEbm-WFXPwT2jFbDzeNFHfjrpYnoAj9JMo')
#bot = telebot.TeleBot('598371065:AAEXidznMgzbIyGB6Fz2uA9Ov_miPnxNWxQ')
bot = telebot.TeleBot('732194281:AAE2fUYjTu9Q356M74q4v2Azut_GqWlskqY')
#products=[]
class User:
	def __init__(self, username, location, category, report):
		self.username = username
		self.location=location
		self.category = category
		self.report = report

class Location:
	def __init__(self, name, numberIndex,letterIndex):
		self.name=name
		self.numberIndex=numberIndex
		self.letterIndex=letterIndex

class Category:
	def __init__(self, name, index):
		self.name=name
		self.index=index

path = ''
locations=[]
users = []
categories=[]

categories.append(Category('Все проблемы', 1))
categories.append(Category('Безопасность', 2))
categories.append(Category('Бизнес', 3))
categories.append(Category('Государственное управление', 4))
categories.append(Category('Здравоохранение', 5))
categories.append(Category('Земельные отношения', 6))
categories.append(Category('Инфраструктура', 7))
categories.append(Category('Коррупция', 8))
categories.append(Category('Трудовые отношения', 9))
categories.append(Category('Судебно-правовая система', 10))
categories.append(Category('Образование', 11))
categories.append(Category('Общественный транспорт', 12))
categories.append(Category('Транспорт и автомобильные дороги', 13))
categories.append(Category('Экология', 14))
categories.append(Category('Другое', 15))


locations.append(Location('Республика Казахстан', 0, 'R'))
locations.append(Location('г. Астана', 1, 'Z')) 
locations.append(Location('г. Алматы', 2, 'A')) 
locations.append(Location('Акмолинская область', 3, 'C')) 
locations.append(Location('Актюбинская область', 4, 'D'))
locations.append(Location('Алматинская область', 5, 'B'))
locations.append(Location('Атырауская область', 6, 'E'))
locations.append(Location('Западно-Казахстанская область', 7, 'L'))
locations.append(Location('Жамбылская область', 8, 'H'))
locations.append(Location('Карагандинская область', 9, 'M'))
locations.append(Location('Костанайская область', 10, 'P'))
locations.append(Location('Кызылординская область', 11, 'N'))
locations.append(Location('Мангистауская область', 12, 'R'))
locations.append(Location('Южно-Казахстанская область', 13, 'X'))
locations.append(Location('Павлодарская область', 14, 'S'))
locations.append(Location('Северо-Казахстанская область', 15, 'T'))
locations.append(Location('Восточно-Казахстанская область', 16, 'F'))
locations.append(Location('г. Шымкент', 17, 'X'))


# Handle '/start' 
catMy = ''
locMy = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):

	msg = bot.send_message(message.chat.id, """\
Hello, choose one of these locations (write number)
""") 
	allLocations=""
	for loc in locations:
		allLocations+=loc.name
		allLocations+=" "
		allLocations+=str(loc.numberIndex)
		allLocations+=" "
		allLocations+=loc.letterIndex
		allLocations+="\n"
	print(allLocations)
	msg = bot.send_message(message.chat.id, allLocations) 
	bot.register_next_step_handler(msg, process_loc)

#name calories id
def process_category(message):
	global catMy
	try:
		index = int(message.text)
		cnt=0
		for loc in categories:
			if(loc.index==index):
				catMy = loc.name
				text="Thanks, "+message.from_user.first_name+"! You chose category " + loc.name+". Now write your report"
				msg = bot.send_message(message.chat.id, text)
				cnt=cnt+1
		if(cnt>0):
			bot.register_next_step_handler(msg, process_result)
			return
		else:
			msg = bot.send_message(message.chat.id, "There is no such category")
			return
		bot.register_next_step_handler(msg, process_result)
	except Exception as e:
		bot.reply_to(message, 'oooops')

	# try:
	# 	name = message.text.lower()
	# 	#print(name)
	# 	text= "Okay, "
	# 	text+= message.from_user.first_name
	# 	text+= "! Write your messages: "
	# 	msg = bot.send_message(message.chat.id, text)
	# 	bot.register_next_step_handler(msg, process_result)
	# except Exception as e:
	# 	bot.reply_to(message, 'oooops')

def process_loc(message):
	global locMy
	try:
		index = int(message.text)
		cnt=0
		
		for loc in locations:
			if(loc.numberIndex==index):
				locMy = loc.name
				print(locMy)
				text="You chose category " +loc.name+". Now choose another category \n\n"
				allLocations=""
				for loc in categories:
					allLocations+=loc.name
					allLocations+=" "
					allLocations+=str(loc.index)
					allLocations+="\n"
				msg = bot.send_message(message.chat.id, text+allLocations)
				cnt=cnt+1
		if(cnt>0):
			bot.register_next_step_handler(msg, process_category)
			return
		else:
			msg = bot.send_message(message.chat.id, "There is no such category")
			return
		bot.register_next_step_handler(msg, process_category)
	except Exception as e:
		bot.reply_to(message, 'oooops')

	#print(message)
	
def process_result(message):
	global locMy
	global catMy
	print(message.text)
	print(message.from_user.first_name)
	print(locMy)

	try:
		text = message.text.lower()
		users.append(User(message.from_user.first_name, locMy, catMy, message.text))
		text="Thanks for report! "+message.from_user.first_name+" "+locMy+", "+catMy+" "+"Rahmet!!! Kop Kop!!"
		msg = bot.send_message(message.chat.id, text)

		bot.register_next_step_handler(msg, process_result)

		# os.mkdir(path + '/' + users[0].location.name)
		# os.mkdir(path + '/' + users[0].location.name + '/' + users[0].category.name)
		# f = open(path + '/' + users[0].location.name + '/' + users[0].category.name=
		#directory = .format(myname, locMy, catMy)
		myname = message.from_user.first_name

		filepath = os.path.join(myname, 'newbot.txt')
		if not os.path.exists(myname):
    			# os.makedirs(myname)
    			# os.makedirs(myname + '/' + locMy)
    			# os.makedirs(myname + '/' + locMy + '/' + catMy)
    			os.makedirs(myname)
    			# os.makedirs("data/{}/{}/{}".format(myname, locMy, catMy))
		# f = open(myname + '/' + locMy + '/' + catMy + '/report.txt', "w")
		# f = open("data/{}/{}/{}/report.txt".format(myname, locMy, catMy), "w")
		f = open(filepath, "w")
		f.write(message.text)
		# f.close()
		# try:
		# 	#os.makedirs(myname)
  #   		# os.makedirs("data/{}/{}/{}".format(myname, locMy, catMy))

		# 	os.mkdir(myname)
		#    	os.mkdir(myname + '/' + locMy)
		#    	os.mkdir(myname + '/' + locMy + '/' + catMy)
		# except: 
		# 	print()

		# f = open(myname + '/' + locMy + '/' + catMy + '/report.txt', "w")
		# f.write(message.text)
		# f.close()


#		os.mkdir('./' + users[0].location.name)
#		os.mkdir('./' + users[0].location.name + '/' + users[0].category.name)
#		f = open(users[0].location.name + '/' + users[0].category.name + '' + 'file')
#		f.write(message.text)
	except Exception as e:
		bot.reply_to(message, str(e))
	

bot.polling()