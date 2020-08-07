''''''#нужно для сравнения и записи времени с предыдущим значением
from common_modules import datetime, log

def last_d():

	with open("last_check.txt") as file:
		last_date = file.readline()
	# print("res=\n",res)
	return last_date

def new_d(res, ld):
	try:
		if res["items"][0]["snippet"]["publishedAt"] > str(ld):
			now = datetime.now().isoformat()
			return (now+"Z", res)
		#в противном случае вернуть 0 и перейти к следующей итерации цикла
		else:
			return 0
	except Exception as e:
		return 0