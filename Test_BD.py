from multiprocessing import connection
import pymysql
import pymysql.cursors

try:
	connect = pymysql.Connect( #запрос к какому серверу
		host="127.0.0.1",
		port=3306,
		user="Oleg",
		password="",
		database="russian_vocabulary",
		charset="utf8",
		cursorclass=pymysql.cursors.DictCursor
	)

	kw = 'пончик' #запрос со стороны пользователя
	type = 'nouns'
	condition = kw.isalpha()
	try:
		if condition == True: #вывод информации с БД
			lkw = kw[-1]
			cursor = connect.cursor()
			if type == 'nouns':
				cursor.execute("SELECT word FROM nouns WHERE word LIKE %s", ('%' + lkw))
			elif type == 'adjectives':
				cursor.execute("SELECT word FROM adjectives WHERE word LIKE %s", ('%' + lkw))
			elif type == 'adverbs':
				cursor.execute("SELECT word FROM adverbs WHERE word LIKE %s", ('%' + lkw))
			elif type == 'introductors':
				cursor.execute("SELECT word FROM introductors WHERE word LIKE %s", ('%' + lkw))
			elif type == 'nouns':
				cursor.execute("SELECT word FROM nouns WHERE word LIKE %s", ('%' + lkw))
			elif type == 'adverbs':
				cursor.execute("SELECT word FROM adverbs WHERE word LIKE %s", ('%' + lkw))
			elif type == 'patriciples':
				cursor.execute("SELECT word FROM participles WHERE word LIKE %s", ('%' + lkw))
			elif type == 'words':
				cursor.execute("SELECT word FROM words WHERE word LIKE %s", ('%' + lkw))
			data = cursor.fetchall()
			cursor.close()
			connect.close()

			for i in data:
				print(str(i))
			
		else: # вывод если нашлось что-то кроме букв
			print("В введённом тексте есть число. Повторите попытку.")
	finally:
		connection.close()
	



except Exception as ex:
	print("Нет ответа от сервера. Скорее всего сервер отключён")
	print(ex)
