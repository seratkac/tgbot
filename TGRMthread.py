from common_modules import sleep, log

def tg(new_offset):
	rules = [
		(("hi","hello","привет","ку","прив","ы"),"привет"),
		(("bye","пока"),"пока")
	]


	from common_modules import tgbot

	while True:
		tt = tgbot.lastUpdt(offset = new_offset)
		if tt == 'nothing happaned':
			log.info('nothing happend')
			sleep(90)
			continue
		try:
			lastUpdtId = tt[0]['update_id']
		except:
			log.info("lastUpdtId not working")
			continue

		new_offset = lastUpdtId + 1

		f = fun(tt[1], tgbot, rules, new_offset)

		if f == "stoped":
			with open("offset.txt", "w") as file:
				file.seek(0)
				file.writelines(str(new_offset))
			log.info("\033[96moffset has been wrote into the file\033[0m")
			break


def fun(tt, tgbot, rules, new_offset):
	for elem in tt:
		try:
			chatId = elem['message']['chat']['id']
			first_name = elem['message']['from']['first_name']
			username = elem['message']['from']['username']
			msg = elem["message"]["text"].lower()

			try:
				log.info("\033[33m{0}@{1}:{2}\033[0m".format(first_name, username, msg))
			except:
				log.info("\033[33mprinting get's answ has not successfull\033[0m")

			if msg == "/stopbot":
				tgbot.sendMsg("725166072","system: offset has been wrote into the file")
				return "stoped"

			if '/getofsset' in msg and '1111' in msg:
				tgbot.sendMsg("725166072", new_offset)
				continue

			def delsnd():
				# /snd:if[td
				cmd = msg[msg.find(":") + 1 : msg.find("[") ]  
				td = msg[msg.find("[") + 1 : ]
				s = ((cmd,cmd), td)
				return s


			def delrule(s):
				rules.pop(rules.index(s))
				tgbot.sendMsg("725166072", "__system:__ deleted a rule:{0}".format(s))
			def addrule(s):
				rules.append(s)
				log.info(rules)
				tgbot.sendMsg("725166072", "__system:__ added new rule:{0}".format(s))


			if '/del' in msg:
				s = delsnd()
				if s in rules:
					delrule(s)
					msg = f"Deleted the rule. If msg = \"{s[0][0]}\" then answ = \"{s[1]}\""
			if '/snd' in msg:
				s = delsnd()
				if s in rules:
					log.info("FINDED_____________________")
					delrule(s)
					# rules.pop(rules.index(s))
					tgbot.sendMsg("725166072", f"Deleted the rule. If msg = \"{s[0][0]}\" then answ = \"{s[1]}\"")
					continue
				addrule(s)
				msg = f"New rule. If msg = \"{s[0][0]}\" then answ = \"{s[1]}\""


			if chatId != "-1001384552463":

				for elem in rules:
					if msg in elem[0]:
						msg = elem[1]
				tgbot.sendMsg(chatId,msg)
		except:
			pass

def threadTelegramm():
	with open("txt/offset.txt", "r") as f:
		new_offset = f.readline()
	tg(new_offset)
