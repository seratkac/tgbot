from log import log
from common_modules import sleep, add, requests, last_d, new_d



#создание ссылки на токен и chId канала
token = "AIzaSyDEqPYOYxXUPtn_rXCqe4ChecmfU5SEZEk"
chId = "UCzvgNsa441iaCgMai585_GA"
#url с переменной метода
url = 'https://www.googleapis.com/youtube/v3/activities'


#функция которая производит запрос по url ютуба
def res(last_chck):

	#инициализация параметров запроса

	param = {
		'part':'snippet,contentDetails',
		'channelId':chId,
		'publishedAfter':last_chck,
		'key':token
	}
	# param = add(token,param)

	#сам запрос
	respons = requests.get(
	 	url,
		param
	)
	#хз что делает
	respons.encoding = 'utf-8'
	#конец функции
	return respons.json(), last_chck


def YouTubeThread():

	last_check = last_d()

	from common_modules import tgbot

	while True:
		#запрос на ютуб
		res1 = res(last_check)
		ld = res1[1]
		r = res1[0]
		#если новых видео не выходило - ждать n времени, пропустить итерацию цикла

		res1 = new_d(r, ld)
		if res1 == 0:  
			log.info("\033[43mVideo has not apeared for some period\033[0m")	
			sleep(3600)		
			continue

		last_check = res1[0]
		r = res1[1]
		YTurl = r["items"][0]["contentDetails"]["upload"]["videoId"]
		tgbot.sendMsg(chatId = "-1001384552463", msgText="https://youtu.be/"+YTurl)
		sleep(43200)