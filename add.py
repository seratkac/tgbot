'''функция собирает все параметры'''
def add(token, params=[('1',2)]):
	temp = []
	temp.extend(params)
	temp.append(('key',token))
	return temp
