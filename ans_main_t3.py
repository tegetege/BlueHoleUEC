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

#回答候補が一つの場合の応答
def one_ans(category_ans,result):

	print('回答候補が一つ見つかりました。')
	#動作確認のため、便宜上取り入れた辞書タプル。
	#本来は情報検索部から解答タプルを得る。
	ans  ={'category' :'where',
		   'what'     :'講演会',
		   'where'    :'東3-501',
		   'who'      :'西野教授',
		   'when_time':'13',
		   'when_day' :'17',
		   'how_time' :'3時間'}

	if category_ans == 'what':
		print('category is what')
		ans_what =  result['what']
		print(ans_what + 'です。')

	elif category_ans == 'when':
		print('category is when')
		ans_when_day =  result['when_day']
		ans_when_time = result['when_time']
		print(ans_when_day + '日の' + ans_when_time + '時です。')

	elif category_ans == 'who':
		print('category is who')
		ans_who =  result['who']
		print(ans_who + 'です。')

	elif category_ans == 'where':
		print('category is where')
		ans_where =  result['where']
		print('場所は'+ ans_where + 'です。')

	elif category_ans == 'how_time':
		print('category is how_time')
		ans_how =  result['how_time']

	else:
		print('category is why or how')
		print('スタッフの方に引き継ぎます。')


#回答候補が複数の時の応答
def some_ans(category_ans,result):
	print('いくつかの回答候補が見つかりました。')
	'''
	#動作確認のため、便宜上取り入れた辞書タプル。
	#本来は情報検索部から解答タプルを得る。
	ans0  ={'category' :'where',
		   'what'      :'これからの電通生に必要な知識とマナーとは',
		   'where'     :'東3-501',
		   'who'       :'西野教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how_time'       :'3時間'}

	ans1  ={'category' :'where',
		   'what'      :'電通大と電通通りの関係について',
		   'where'     :'講堂',
		   'who'       :'高木教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how_time'       :'1時間30分'}

	ans2  ={'category' :'where',
		   'what'      :'西友とパルコでの上手な買い物の仕方',
		   'where'     :'東5-202',
		   'who'       :'野田教授',
		   'when_time' :'13',
		   'when_day'  :'17',
		   'how_time'       :'2時間'}

	anser = [ans0,ans1,ans2]
	'''

	if category_ans == 'what':
		print('category is what')
		for result in resul:
			ans_what = result['what']
			print(ans_what + 'が候補として挙がっています。')

	elif category_ans == 'when':
		print('category is when')
		for result in result:
			ans_when_day  = result['when_day']
			ans_when_time = result['when_time']
			print(ans_when_day + '日の' + ans_when_time + '時が候補として挙がっています。')

	elif category_ans == 'who':
		print('category is who')
		for result in result:
			ans_name = result['who']
			print(ans_name + 'さんのイベントが候補として挙がっています。')

	elif category_ans == 'where':
		print('category is where')
		for result in result:
			ans_where = result['where']
			print(ans_where + 'で行われるイベントが候補として挙がっています。')

	elif category_ans == 'how_time':
		print('category is how_time')
		for result in result:
			print(result['how_time'])

	else:
		print('category is why or how')
		print('スタッフの方に引き継ぎます。')

