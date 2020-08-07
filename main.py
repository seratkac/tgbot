#импортирование модулей
from log import log
from common_modules import datetime, sleep, log

import TGRMthread as trT
import YTthread
import threading



def InOut():
	while True:
			if input("In:") == ".exit":
				raise SystemExit(0)

def main():
	with open("lastlaunch.txt", "w") as f:
		now = datetime.now().isoformat()
		f.write(str(datetime.now()))
	x1 = threading.Thread(target = trT.threadTelegramm, daemon = True)
	x2 = threading.Thread(target = YTthread.YouTubeThread, daemon = True)
	# x3 = threading.Thread(target = InOut, daemon = True)

	x1.setName("TG")
	x2.setName("YT")
	# x3.setName("IO")

	x1.start()
	x2.start()
	# x3.start()

	x1.join()

	with open("last_check.txt", 'w') as file:
		file.seek(0)
		file.writelines(now + "Z")



def exit():
	log.info('shutdown')
	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()