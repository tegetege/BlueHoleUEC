# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

import sys
import MeCab
import re
import pandas
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
#K３システムのインスタンス作成
k3 =K3()

#入出力を記録
rfs = record.record_for_s
rfu = record.record_for_u

#回答候補が一つの場合の応答
def one_ans(category_ans,result):

	rfs('回答候補が一つ見つかりました。')

	#リストの配列から辞書を取り出す
	result = result[0]['data']


	if category_ans == 'what':
		print('category is what')
		ans_what =  result['what']
		rfs(ans_what + 'です。')

	elif category_ans == 'when':
		print('category is when')
		ans_when_day =  result['when_day']
		ans_when_time = result['when_time']
		rfs(ans_when_day + '日の' + ans_when_time + '時です。')

	elif category_ans == 'who':
		print('category is who')
		ans_who =  result['who']
		rfs(ans_who + 'です。')

	elif category_ans == 'where':
		print('category is where')
		ans_where =  result['where']
		rfs('場所は'+ ans_where + 'です。')

	elif category_ans == 'how_time':
		print('category is how_time')
		ans_how =  result['how_time']
		rfs(ans_how + 'です。')

	else:
		print('category is why or how')
		rfs('スタッフの方に引き継ぎます。')
		#終了
		record.record_A('----- conversation end   -----')
		#履歴の表示
		df = pandas.read_csv('conversation_log.csv')
		print_record = df[count_row_start:]
		print(print_record)
		sys.exit()


#複数回答候補をリスト化して表示
def some_ans(category_ans,results):
	rfs('いくつかの回答候補が見つかりました。')
	for result in results:
		#信頼度が１以上の回答のみを表示
		if result['reliability'] >1:

			if category_ans == 'what':
				print('category is what')
				result = result['data']
				ans_what = result['what']
				rfs(ans_what + 'が候補として挙がっています。')


			elif category_ans == 'when':
				print('category is when')
				result = result['data']
				ans_title = result['title']
				ans_when_day  = result['when_day']
				ans_when_time = result['when_time']
				rfs('title:' + str(ans_title))
				rfs(str(ans_when_day) + '日の' + str(ans_when_time) + '時が候補として挙がっています。')


			elif category_ans == 'who':
				print('category is who')
				result = result['data']
				ans_name = result['who']
				rfs(ans_name + 'さんのイベントが候補として挙がっています。')


			elif category_ans == 'where':
				print('category is where')
				result = result['data']
				ans_where = result['where']
				rfs(ans_where + 'で行われるイベントが候補として挙がっています。')


			elif category_ans == 'how_time':
				print('category is how_time')
				result = result['data']
				ans_what     = result['what']
				ans_how_time = result['how_time']
				rfs(ans_what + ':' + ans_how_time)


			else:
				print('category is why')
				rfs('スタッフの方に引き継ぎます。')
				#終了
				record.record_A('----- conversation end   -----')
				#履歴の表示
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()

'''
#履歴を表示してシステム終了する場合
def end_with_record(count_row_start):
	r_read = record.record_read()
	count_row_end = 0
	for row in r_read:
		count_row_end +=  1 
'''


#情報検索部(k3)にアクセスしてDBを検索する
#該当するタプルはリスト化して返される
def look_k3(data):
	k3.set_params(data)
	return k3.search()


def yes_or_no():
	rfs('欲しい情報はありましたか？(yes/no)')
	u_ans = input('Input: ')
	rfu(u_ans)
	if u_ans == 'yes':
		rfs('良かったです！また、質問してくださいね。')
		record.record_A('----- conversation end   -----')
		sys.exit()
	elif u_ans == 'no':
		rfs('もう一度初めから開始しますか？(yes/no)')
		#　入力
		u_ans = input('Input: ')
		rfu(u_ans)
		if u_ans == 'yes':
			main_t3.start()
		else:
			record.record_A('----- conversation end   -----')
			sys.exit()

def count_list(results):
	count = 0
	for result in results:
		if result['reliability'] >1:
			count +=  1 
	return count 

#情報検索部(k3)から返されたタプルの数によってそれぞれの返答をする。
#回答候補が５個以上の場合、追加質問を行う。
def anser(data,category_ans,add_q_count,results,count_row_start):
	#信頼度１以上の回答候補をカウントする
	ans_count = ans_main_t3.count_list(results)

	#追加質問を1度行った時
	if int(add_q_count) >= 1:

		#条件の全探索で見つかったものかどうかの判定	
		result_A = results[0]['all_and']

		#条件の全探索で見つかった場合
		if result_A == 1:
			rfs('条件の全探索で当てはまるものが見つかりました。')

			ans_main_t3.one_ans(category_ans,result)
			ans_main_t3.yes_or_no()

			
		#条件の部分探索で見つかった場合
		elif result_A == 0:
			#候補の数が５個以内の時
			if int(ans_count) <= 5:
				rfs('条件の全探索では当てはまりませんでした。')
				rfs('代わりに似たものを表示させます。')

				ans_main_t3.some_ans(category_ans,result)
				ans_main_t3.yes_or_no()

			#候補の数が５個以上の時
			if int(ans_count) > 5:
				rfs('追加質問の内容を加味して再検索しましたが、候補となる結果が絞りきれませんでした。')
				rfs('スタッフにひきつぐために履歴表示をします。')
				#終了
				record.record_A('----- conversation end   -----')
				#履歴の表示
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()

		elif int(ans_count)  == 0:
			rfs('追加質問の内容を加味して再検索しましたが、結果が見つかりませんでした。')
			rfs('スタッフに引き継ぐために履歴表示をします。')
			#終了
			record.record_A('----- conversation end   -----')
			df = pandas.read_csv('conversation_log.csv')
			print_record = df[count_row_start:]
			print(print_record)
			sys.exit()




	#追加質問をまだ行っていない時
	else:
		#条件の全探索で見つかったものかどうかの判定	
		result_A = results[0]['all_and']

		#条件の全探索(AND)で見つかった時の返答
		if result_A == 1:
			rfs('条件の全探索で当てはまるものが見つかりました。')
			ans_main_t3.one_ans(category_ans,result)
			ans_main_t3.yes_or_no()


		#条件の部分探索(OR)で見つかった時の返答
		elif result_A == 0 :
			#回答候補が５個以下の時
			if ans_count <= 5:
				rfs('条件の全探索では当てはまりませんでした。')
				rfs('代わりに似たものを表示させます。')

				ans_main_t3.some_ans(category_ans,results)
				ans_main_t3.yes_or_no()

			#回答候補が５個以上の時
			elif ans_count  >5:
				#追加質問を行う。
				rfs('大量の回答候補が見つかりました。追加質問を生成します。')
				#追加質問をした回数をカウントする変数へ+1
				add_q_count += 1

				#k3システムから"最重要キーワード"を取得してくる
				key = k3.get_wanting_category()
				print(key)
				
				#whereの場合のみ、whatのリストに追加して情報検索部に投げる
				if key == 'where':
					data['what'].extend(add_q_main.make_q(key))
				else:
					data[key].extend(add_q_main.make_q(key))
			
				rfs('----- もう一度検索します。 -----')
				result = ans_main_t3.look_k3(data)
			
				ans_main_t3.anser(data,category_ans,add_q_count,result,count_row_start)


		#回答候補が0個のとき
		elif int(ans_count)  == 0:
			rfs('結果が見つかりませんでした。')
			rfs('スタッフに引き継ぐために履歴表示をします。')
			#終了
			record.record_A('----- conversation end   -----')
			df = pandas.read_csv('conversation_log.csv')
			print_record = df[count_row_start:]
			print(print_record)
			sys.exit()

