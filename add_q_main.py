# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0


import sys


def make_q(category_ans):
	#K３から受け取った最重要キーワード
	key = "where"


	if key == 'what':
		print('Key is "what"')
		print('イベント名はご存知ですか？')

	elif category_ans == 'when':
		print('Key is "when"')
		print('イベントは何時から始まるかご存知ですか？')


	elif category_ans == 'who':
		print('Key is "who"')
		print('どなたがご出演かご存知ですか？')

	elif category_ans == 'where':
		print('どこで行われるかご存知ですか？')


