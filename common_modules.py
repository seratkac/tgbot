import requests
from log import log
from time import sleep
from datetime import datetime
import tgrm


with open("txt/token.txt") as f:
	token = f.readline()

tgbot = tgrm.Telegramm(token)

