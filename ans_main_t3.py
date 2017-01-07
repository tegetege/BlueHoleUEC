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
import ans_main_t3
import add_q_main
import main_t3
from k3.main import K3


#k3システムからもらう"result"の形式
'''
{'all_and': 1,
    'data': {'created_at': None,
             'how_time': '10時間',
             'id': 7,
             'title': '剣道部のフライドチキン',
             'updated_at': None,
             'what': '剣道部のフライドチキン',
             'when_day': '17',
             'when_time': '10',
             'where': '広場',
             'who': '剣道部'},
    'reliability': 4.0},
'''

#回答候補が一つの場合の応答
def one_ans(category_ans,result):

	print('回答候補が一つ見つかりました。')

	#リストの配列から辞書を取り出す
	result = result[0]['data']


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


#回答候補をリスト化して表示
def some_ans(category_ans,results):
	print('いくつかの回答候補が見つかりました。')

	if category_ans == 'what':
		print('category is what')
		for result in results:
			result = result['data']
			ans_what = result['what']
			print(ans_what + 'が候補として挙がっています。')


	elif category_ans == 'when':
		print('category is when')
		for result in results:
			result = result['data']
			ans_when_day  = result['when_day']
			ans_when_time = result['when_time']

			print(str(ans_when_day) + '日の' + str(ans_when_time) + '時が候補として挙がっています。')


	elif category_ans == 'who':
		print('category is who')
		for result in results:
			result = result['data']
			ans_name = result['who']
			print(ans_name + 'さんのイベントが候補として挙がっています。')


	elif category_ans == 'where':
		print('category is where')
		for result in results:
			result = result['data']
			ans_where = result['where']
			print(ans_where + 'で行われるイベントが候補として挙がっています。')


	elif category_ans == 'how_time':
		print('category is how_time')
		for result in results:
			result = result['data']
			ans_what     = result['what']
			ans_how_time = result['how_time']
			print(ans_what + ':' + ans_how_time)


	else:
		print('category is why or how')
		print('スタッフの方に引き継ぎます。')

#情報検索部(k3)にアクセスしてDBを検索する
#該当するタプルはリスト化して返される
def look_k3(data):
	k3 = K3()
	k3.set_params(data)
	return k3.search()


#情報検索部(k3)から返されたタプルの数によってそれぞれの返答をする。
#回答候補が５個以上の場合、追加質問を行う。
def anser(data,category_ans,add_q_count,result):
	#応答数をカウントする
	ans_count = len(result)
	if int(ans_count)  == 0:
		print('結果が見つかりませんでした。')
		print('スタッフに引き継ぐために履歴表示をします。')
		#終了
		sys.exit()

	if int(add_q_count) > 1:
		if int(ans_count)  == 0:
			print('追加質問の内容を加味して再検索しましたが,結果が見つかりませんでした。')
			print('スタッフに引き継ぐために履歴表示をします。')
			#終了
			sys.exit()

	else:
		#条件の全探索で見つかったものかどうかの判定	
		result_A = result[0]['all_and']
		print(result_A)
		#条件の全探索(AND)で見つかった時の返答
		if result_A == 1:
			print('条件の全探索で当てはまるものが見つかりました。')

			ans_main_t3.one_ans(category_ans,result)
		
			print('欲しい情報はありましたか？')
			print('もう一度初めから開始しますか？(yes/no)')
			#　入力
			u_ans = input('Input: ')
			if u_ans == 'yes':
				main_t3.start()
			else:
				sys.exit()


		#条件の部分探索(OR)で見つかった時の返答
		elif result_A == 0:
			print('条件の全探索では当てはまりませんでした。')
			print('代わりに似たものを表示させます。')

			ans_main_t3.some_ans(category_ans,result)

			print('欲しい情報はありましたか？')
			print('もう一度初めから開始しますか？(yes/no)')
			#　入力
			u_ans = input('Input: ')

			if u_ans == 'yes':
				main_t3.start()
			else:
				sys.exit()


		#追加質問を行う。
		else:
			print('大量の回答候補が見つかりました。追加質問を生成します。')
			#追加質問をした回数をカウントする変数へ+1
			add_q_count += 1
			#k3システムから"最重要キーワード"を取得してくる
			key = 'when_time'
			#whereの場合のみ、whatのリストに追加して情報検索部に投げる
			if key == 'where':
				data['what'].extend(add_q_main.make_q(key))
			else:
				data[key].extend(add_q_main.make_q(key))
		
			print('---もう一度検索します。---')
			ans_main_t3.search(data)
			ans_main_t3.anser(data,category_ans,add_q_count,result)
