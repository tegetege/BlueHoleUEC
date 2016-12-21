# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

import sys
import MeCab
import re

#----外ファイルインポート----
import python_mecab
import get_nlc 
import get_day 
import record
from k3.main import K3

def one_ans(category_ans):

	print('回答候補が一つ見つかりました。')
	#動作確認のため、便宜上取り入れた辞書タプル。
	#本来は情報検索部から解答タプルを得る。
	ans  ={'category' :'where',
		   'what'     :'講演会',
		   'where'    :'東3-501',
		   'who'      :'西野教授',
		   'when_time':'13',
		   'when_day' :'17',
		   'how'      :'3時間'}

	if category_ans == 'what':
		print('category is what')
		ans_what =  ans['what']
		print(ans_what + 'です。')

	elif category_ans == 'when':
		print('category is when')
		ans_when_day =  ans['when_day']
		ans_when_time = ans['when_time']
		print(ans_when_day + '日の' + ans_when_time + '時です。')

	elif category_ans == 'who':
		print('category is who')
		ans_who =  ans['who']
		print(ans_who + 'です。')

	elif category_ans == 'where':
		print('category is where')
		ans_where =  ans['where']
		print('場所は'+ ans_where + 'です。')

	elif category_ans == 'how':
		print('category is how')
		ans_how =  ans['how']

	else:
		print('category is why')
		print('スタッフの方に引き継ぎます。')



def some_ans(category_ans):
	print('いくつかの回答候補が見つかりました。')
	#動作確認のため、便宜上取り入れた辞書タプル。
	#本来は情報検索部から解答タプルを得る。
	ans0  ={'category' :'where',
		   'what'      :'講演会',
		   'where'     :'東3-501',
		   'who'       :'西野教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how'       :'3時間'}

	ans1  ={'category' :'where',
		   'what'      :'講演会',
		   'where'     :'講堂',
		   'who'       :'高木教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how'       :'1時間30分'}

	ans2  ={'category' :'where',
		   'what'      :'講演会',
		   'where'     :'東5-202',
		   'who'       :'野田教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how'       :'2時間'}

	anser = [ans0,ans1,ans2]

	if category_ans == 'what':
		print('category is what')
		for anser in anser:
			ans_what = anser['what']
			print(ans_what + 'が候補として挙がっています。')

	elif category_ans == 'when':
		print('category is when')
		for anser in anser:
			ans_when_day  = anser['when_day']
			ans_when_time = anser['when_time']
			print(ans_when_day + '日の' + ans_when_time + '時が候補として挙がっています。')

	elif category_ans == 'who':
		print('category is who')
		for anser in anser:
			ans_name = anser['who']
			print(ans_name + 'さんのイベントが候補として挙がっています。')

	elif category_ans == 'where':
		print('category is where')
		for anser in anser:
			ans_where = anser['where']
			print(ans_where + 'で行われるイベントが候補として挙がっています。')

	elif category_ans == 'how':
		print('category is how')
		for anser in anser:
			print(anser['how'])

	else:
		print('category is why')
		print('スタッフの方に引き継ぎます。')

