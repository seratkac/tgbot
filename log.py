import logging as log

log.basicConfig(
	format='{%(threadName)s}:[%(filename)s->%(funcName)s(**)->%(lineno)d]: %(message)s',
	level=log.INFO)