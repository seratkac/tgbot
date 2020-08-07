from log import log
from common_modules import requests

class Telegramm:
	"""docstring for Telegramm"""
	def __init__(self):
		self.YTurl = ""
		self.tgkey = '1350709675:AAEceWlKkdiNwouvx0ZVWHaEKFlSY-kEOHc'
		self.url = f"https://api.telegram.org/bot{self.tgkey}/"



	def getMe(self):
		return req(self.url + 'getMe')

	def sendMsg(self, chatId, msgText):
		return self.reqPost(self.url + "sendMessage", {'chat_id':chatId, 'text':msgText})


	def getUpdt(self, offset = None, timeout = 120):
		return self.req(self.url + 'getUpdates', {'timeout': timeout, 'offset': offset})

	def lastUpdt(self, offset = None):
		data = self.getUpdt(offset)
		# log.info(data)

		res = data['result']
		try:
			log.info('try 2')
			return (res[len(res) - 1], res)
		except:
			return 'nothing happaned'

		

	def req(self, u, params = {}):
		log.info("\033[96mGet:\n{0}\033[36m{1}\033[0m".format(u, params))
		temp = requests.get(u , params)
		return temp.json()
	def reqPost(self, u, params = {}):
		log.info("\033[96mPost:\n{0}\033[33m{1}\033[0m".format(u, params))
		temp = requests.post(u , params)
		# log.info("\033[46mPost Answer: \n{0}\033[0m".format(temp.json()))
		return temp
