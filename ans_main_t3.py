 # coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

import sys
import MeCab
import re
import pandas
from PIL import Image
#----外ファイルインポート----
import python_mecab
import get_nlc 
import get_day_time
import record
import ans_main_t3
import add_q_main
import main_t3
from k3.main import K3




#k3システムからもらう"results"の形式
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
def one_ans(category_ans,result,count_row_start):

	reliability = result[0]['reliability']
	if reliability < 1:
		rfs('>条件に合致するデータは見つかりませんでしたが、似たデータが一つ見つかりました。')
	else:
		rfs('>回答候補が一つ見つかりました。')

	#リストの配列から辞書を取り出す
	result = result[0]['data']


	if category_ans == 'what':
		print('----------')
		print('category is what')
		ans_what = result['what']
		ans_title = result['title']
		ans_when_time = result['when_time']
		rfs(">" + ans_what + "'" + ans_title + "'" + 'があります。' + '(' + ans_when_time + ')')
		print('----------')

	elif category_ans == 'when':
		print('----------')
		print('category is when')
		ans_title = result['title']
		ans_when_day =  result['when_day']
		ans_when_time = result['when_time']
		rfs('>title:' + str(ans_title))
		rfs(">" +ans_when_day + '日の' + ans_when_time + '開始です。')
		print('----------')

	elif category_ans == 'who':
		print('----------')
		print('category is who')
		ans_title = result['title']
		ans_who =  result['who']
		rfs('>title:' + str(ans_title))
		rfs(">" +ans_who + 'です。')
		print('----------')

	elif category_ans == 'where':
		print('----------')
		print('category is where')
		ans_title = result['title']
		ans_where =  result['where']
		rfs('>title:' + str(ans_title))
		rfs('>場所は'+ ans_where + 'です。')
		print('----------')

	elif category_ans == 'how_time':
		print('----------')
		print('category is how_time')
		ans_how =  result['how_time']
		ans_title = result['title']
		rfs('>title:' + str(ans_title))
		rfs(">" +ans_how + 'です。')
		print('----------')

	else:
		print('>category is why or how')
		rfs('>スタッフの方に引き継ぎます。')
		#終了
		record.record_A('----- conversation end   -----')
		#履歴の表示
		df = pandas.read_csv('conversation_log.csv')
		print_record = df[count_row_start:]
		print(print_record)
		sys.exit()
    
	if reliability < 1:
		parent = k3.get_parent(result['parent_id'])
		if parent['image']:
			rfs('>参考に親データ画像を表示します')
			#画像の読み込み
			im = Image.open(parent['image'])
			im.show()


#条件部分探索の複数回答候補をリスト化して表示
#自信度でテーブルをフィルタリング
def some_ans(category_ans,results,borderline,count_row_start):
	rfs('>いくつかの回答候補が見つかりました。')
	#解答をカウント数で管理
	count = 0
	for result in results:
		#あらかじめ設定された信頼度以上のカウントのみを表示
		if borderline >= count:
			print('----------')
			if category_ans == 'what':
				#print('category is what')
				result = result['data']
				ans_what = result['what'] 
				ans_title = result['title']
				ans_when_time = result['when_time']
				ans_where = result['where']
				print('[' + str(count) + ']')
				rfs(ans_what + "'" + ans_title + "'" + 'があります。' + '(' + ans_when_time + ')')
				rfs('開催場所：' + ans_where)


			elif category_ans == 'when':
				#print('category is when')
				result = result['data']
				ans_title = result['title']
				ans_when_day  = result['when_day']
				ans_when_time = result['when_time']
				ans_where  = result['where']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(str(ans_when_day) + '日の' + str(ans_when_time) + '開始です。')
				rfs('開催場所：' + ans_where)


			elif category_ans == 'who':
				#print('category is who')
				result = result['data']
				ans_title = result['title']
				ans_name = result['who']
				ans_when_time = result['when_time']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(ans_name + 'さん。')


			elif category_ans == 'where':
				#print('category is where')
				result = result['data']
				ans_title = result['title']
				ans_where = result['where']
				ans_when_time = result['when_time']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(ans_where + 'で行われます。')


			elif category_ans == 'how_time':
				#print('category is how_time')
				result = result['data']
				ans_title     = result['title']
				ans_how_time = result['how_time']
				print('[' + str(count) + ']')
				rfs(ans_title + ':' + ans_how_time + '時間')


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

			#解答番号をカウントアップ
			count += 1
	print('----------')

#条件全探索の回答が複数ある時、
#信頼度のフィルタリングをしない
def some_ans_all(category_ans,results,count_row_start):
	rfs('>いくつかの回答候補が見つかりました。')
	#解答をカウント数で管理
	count = 0
	for result in results:
		if result['all_and'] == 1:
			print('----------')
			if category_ans == 'what':
				#print('category is what')
				result = result['data']
				ans_what = result['what'] 
				ans_title = result['title']
				ans_when_time = result['when_time']
				ans_where = result['where']
				print('[' + str(count) + ']')
				rfs(ans_what + "'" + ans_title + "'" + 'があります。' + '(' + ans_when_time + ')')
				rfs('開催場所：' + ans_where)
		
		
			elif category_ans == 'when':
				#print('category is when')
				result = result['data']
				ans_title = result['title']
				ans_when_day  = result['when_day']
				ans_when_time = result['when_time']
				ans_where  = result['where']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(str(ans_when_day) + '日の' + str(ans_when_time) + '開始です。')
				rfs('開催場所：' + ans_where)
	
		
			elif category_ans == 'who':
				#print('category is who')
				result = result['data']
				ans_title = result['title']
				ans_name = result['who']
				ans_when_time = result['when_time']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(ans_name + 'さん。')
		
		
			elif category_ans == 'where':
				#print('category is where')
				result = result['data']
				ans_title = result['title']
				ans_where = result['where']
				ans_when_time = result['when_time']
				print('[' + str(count) + ']')
				rfs('title:' + str(ans_title))
				rfs(ans_where + 'で行われます。')
	
	
			elif category_ans == 'how_time':
				#print('category is how_time')
				result = result['data']
				ans_title     = result['title']
				ans_how_time = result['how_time']
				print('[' + str(count) + ']')
				rfs(ans_title + ':' + ans_how_time + '時間')
		
		
			else:
				print('category is why or how')
				rfs('スタッフへ引き継ぎます。')
				#終了
				record.record_A('----- conversation end   -----')
				#履歴の表示
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()
			#解答番号をカウントアップ
			count += 1
	print('----------')

#情報検索部(k3)にアクセスしてDBを検索する
#該当するタプルはリスト化して返される
def look_k3(data):
	k3.set_params(data)
	return k3.search()

#ユーザーに欲しい情報があるか否かを質問して、
#ない場合は、もう一度初めからやり直す
#yes_or_no_one:一意の返答の場合
def yes_or_no_one(result,count_row_start):

	if result['image'] != None:	
		rfs('>詳細を表示します')
		im = Image.open(result['image'])
		im.show()
	rfs('>欲しい情報でしたか？(yes/no)')
	u_ans = input('Input: ')
	rfu(u_ans)
	if u_ans == 'yes':
		result_more = result
		ans_main_t3.more_question(result_more)
		
	elif u_ans == 'no':
		rfs('>スタッフへ引き継ぐために履歴を表示します。')
		record.record_A('----- conversation end   -----')
		#履歴の表示
		df = pandas.read_csv('conversation_log.csv')
		print_record = df[count_row_start:]
		print(print_record)
		sys.exit()


#ユーザーに欲しい情報があるか否かを質問して、
#ない場合は、もう一度初めからやり直す
#yes_or_no_one:複数の返答の場合
def yes_or_no_some(results,list_num,count_row_start):
	rfs('>欲しい情報はありましたか？(yes/no)')
	u_ans = input('Input: ')
	rfu(u_ans)

	if u_ans == 'yes':
		#ユーザーが欲しかった情報の回答番号を確保
		rfs('>良かったです！何番の回答でしたか？')
		ans_num = input('Input: ')
		#間違った数字が入力されたときのエラー対処
		if list_num < int(ans_num):
			ans_num = ans_main_t3.what_num(list_num)
		#任意の番号の回答を確保する
		result_more = results[int(ans_num)]['data']
		ans_main_t3.more_question(result_more)

	elif u_ans == 'no':
		rfs('>スタッフへ引き継ぐために履歴を表示します。')
		record.record_A('----- conversation end   -----')
		#履歴の表示
		df = pandas.read_csv('conversation_log.csv')
		print_record = df[count_row_start:]
		print(print_record)
		sys.exit()

	else:
		ans_main_t3.yes_or_no_some(results,list_num,count_row_start)
		'''
		rfs('>もう一度初めから開始しますか？(yes/no)')
		#　入力
		u_ans = input('Input: ')
		rfu(u_ans)
		if u_ans == 'yes':
			main_t3.start()
		else:
			record.record_A('----- conversation end   -----')
			sys.exit()
		'''


#正しい番号が入力されるまで無限ループ
def what_num(ans_num):
	rfs('>正しい番号を入力してください。(0 ~ ' + str(ans_num) + ')')
	num = input('Input: ')
	if ans_num >= int(num) :
		return num 
	else:
		ans_main_t3.what_num(ans_num)

#yes or noが入力されるまで無限ループ
def more_(text):
	rfs(">" + text +'(yes/no)')
	ans = input('Input: ')

	if ans == 'yes|no':
		return ans
	else:
		ans_main_t3.y_or_n(text)


#ユーザーの深追い質問に対応する
def more_question(result_more):
	#応答について深追いの質問があるか否か(さらに、場所や時間を訪ねる時)
	#画像が用意されている場合は表示する
	if result_more['image'] != None:	
		rfs('詳細を表示します')
		im = Image.open(result_more['image'])
		im.show()

	rfs('>これについて、何か質問はありますか？(yes/no)')
	u_ans2 = input('Input: ')
	rfu(u_ans2)
	if u_ans2 =='no':
		rfs('>また、質問してくださいね！Have a nice day!')
		record.record_A('----- conversation end   -----')
		sys.exit()
	elif u_ans2 == 'yes':
		rfs('>質問は何でしょうか？')
		#　入力
		st = input('Input: ')
		rfu(st)
		category_ans = get_nlc.nlc_0(st)
		more_category ='カテゴリー: '
		print( more_category + category_ans)

		if category_ans == 'what':
			rfs('>title:' + result_more['title'])		 
		elif category_ans == 'who':
			rfs(">" + result_more['who'] + 'さんです。')
		elif category_ans == 'where':
			rfs(">" + result_more['where'] + 'です。')
		elif category_ans == 'how_time' :
			rfs(">" + result_more['how_time'] + 'です。')
		elif category_ans == 'when':
			rfs(">" + result_more['when_day']+'日の'+result_more['when_time']+'です。')
		
		rfs('>もう一度初めから開始しますか？(yes/no)')
			#　入力
		u_ans = input('Input: ')
		rfu(u_ans)
		if u_ans == 'yes':
			main_t3.start()
		else:
			rfs('>また、質問してくださいね！Have a nice day!')
			record.record_A('----- conversation end   -----')
			sys.exit()
	#yesとno以外が入力されたときのエラー処理
	else:
		rfs('>yesかnoを入力してください')
		ans_main_t3.more_question(result_more)

#自信値が1以上のテーブルの数をカウントする
def count_list(results):
	count = 0
	for result in results:
		if result['reliability'] < 1:
			return count
		count +=  1 
	return count

#回答候補の中の条件全探索のテーブル数をカウントする
def count_list_condition(results):
	count = 0
	for result in results:
		if result['all_and'] == 0: 
			return count 
		count += 1
	return count


#情報検索部(k3)から返されたタプルの数によってそれぞれの返答をする。
#回答候補が５個以上の場合、追加質問を行う。
def anser(data,category_ans,add_q_count,results,count_row_start):
	#信頼度１以上の回答候補をカウントする
	ans_count = ans_main_t3.count_list(results)
	#k3システムから返されたリストの数を数える
	res_count = len(results)
	#追加質問を2度行った時
	if int(add_q_count) >= 2:

		#条件の全探索で見つかった場合
		if  res_count > 0 and results[0]['all_and'] == 1:
			ans_count_condition = ans_main_t3.count_list_condition(results)
			#条件全探索リストが１つの時
			if ans_count_condition == 1:
				rfs('>条件の全探索で当てはまるものが一件見つかりました。')
				ans_main_t3.one_ans(category_ans,results)
				ans_main_t3.yes_or_no_one(results[0]['data'],count_row_start)
			#条件全探索リストが2つ~8つの時
			elif ans_count_condition <= 8:
				rfs('>条件の全探索で当てはまるものが複数見つかりました。')
				ans_main_t3.some_ans_all(category_ans,results,count_row_start)
				ans_main_t3.yes_or_no_some(results,ans_conut_condition,count_row_start)

			#条件全探索リストが5つ以上の時
			elif ans_count_condition > 8:
				rfs('>追加質問の内容を加味して再検索しましたが、候補となる結果が絞りきれませんでした。')
				rfs('>スタッフにひきつぐために履歴表示をします。')
				#終了
				record.record_A('----- conversation end   -----')
				#履歴の表示
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()

	
		#条件の部分探索で見つかった場合
		elif res_count == 0 or results[0]['all_and'] == 0:

			if int(ans_count)  == 0:
				rfs('>追加質問の内容を加味して再検索しましたが、結果が見つかりませんでした。')
				rfs('>スタッフに引き継ぐために履歴表示をします。')
				#終了
				record.record_A('----- conversation end   -----')
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()

			elif int(ans_count) == 1:
				rfs('>条件の部分探索で当てはまりました。')
				rfs('>代わりに似たものを表示させます。')

				ans_main_t3.one_ans(category_ans,results,count_row_start)
				ans_main_t3.yes_or_no_one(results[0]['data'],count_row_start)


			#候補の数が8個以内の時
			elif int(ans_count) <= 8:
				rfs('>条件の部分探索では当てはまりました。')
				rfs('>代わりに似たものを表示させます。')

				ans_main_t3.some_ans(category_ans,results,ans_count,count_row_start)
				ans_main_t3.yes_or_no_some(results,ans_count,count_row_start)

			#候補の数が8個以上の時
			elif int(ans_count) > 8:
				rfs('>追加質問の内容を加味して再検索しましたが、候補となる結果が絞りきれませんでした。')
				rfs('>スタッフにひきつぐために履歴表示をします。')
				#終了
				record.record_A('----- conversation end   -----')
				#履歴の表示
				df = pandas.read_csv('conversation_log.csv')
				print_record = df[count_row_start:]
				print(print_record)
				sys.exit()

	#追加質問をまだ行っていない時
	else:

		#条件の全探索(AND)で見つかった時の返答
		if res_count > 0 and results[0]['all_and'] == 1:
			ans_count_condition = ans_main_t3.count_list_condition(results)
			#条件全探索リストが１つの時
			if ans_count_condition == 1:
				rfs('>条件の全探索で当てはまるものが一件見つかりました。')
				ans_main_t3.one_ans(category_ans,results,count_row_start)
				ans_main_t3.yes_or_no_one(results[0]['data'],count_row_start)
			#条件全探索リストが2つ~8つの時
			elif ans_count_condition <= 8:
				rfs('>条件の全探索で当てはまるものが複数見つかりました。')
				ans_main_t3.some_ans_all(category_ans,results,count_row_start)
				ans_main_t3.yes_or_no_some(results,ans_count_condition,count_row_start)
			#条件全探索リストが8つ以上の時
			elif ans_count_condition > 8:
				#追加質問を行う。
				rfs('>大量の回答候補が見つかりました。')
				#追加質問をした回数をカウントする変数へ+1
				add_q_count += 1

				#k3システムから"最重要キーワード"を取得してくる
				key = k3.get_wanting_category()
				
				#whereの場合のみ、whatのリストに追加して情報検索部に投げる
				if key == 'where':
					data['what'].extend(add_q_main.make_q(key))
				else:
					data[key].extend(add_q_main.make_q(key))
			
				rfs('----- もう一度検索します。 -----')
				results = ans_main_t3.look_k3(data)
			
				ans_main_t3.anser(data,category_ans,add_q_count,results,count_row_start)




		#条件の部分探索(OR)で見つかった時の返答
		elif res_count == 0 or results[0]['all_and'] == 0 :
			#信頼度の閾値を超えたリスト数が0個の場合
			if ans_count ==0:
				#データベースから返答されたリストが一つだった場合、信頼度に関わらず返答する
				if len(results) == 1:
					ans_main_t3.one_ans(category_ans,results,count_row_start)
					ans_main_t3.yes_or_no_one(results[0]['data'],count_row_start)

				else:
					rfs('>結果が見つかりませんでした。')
					rfs('>追加質問を生成します。')
					#追加質問をした回数をカウントする変数へ+1
					add_q_count += 1
					#k3システムから"最重要キーワード"を取得してくる
					key = k3.get_wanting_category()
					
					#whereの場合のみ、whatのリストに追加して情報検索部に投げる
					if key == 'where':
						data['what'].extend(add_q_main.make_q(key))
					if key == None:
						rfs('>検索結果が絞り込めませんでした。スタッフへ引き継ぎます')
						rfs('>履歴を表示して、システムを終了します')
						record.record_A('----- conversation end   -----')
						#履歴の表示
						df = pandas.read_csv('conversation_log.csv')
						print_record = df[count_row_start:]
						print(print_record)
						sys.exit()


					else:
						data[key].extend(add_q_main.make_q(key))
				
					rfs('----- もう一度検索します。 -----')
					results = ans_main_t3.look_k3(data)
				
					ans_main_t3.anser(data,category_ans,add_q_count,results,count_row_start)

			elif ans_count == 1:
				rfs('>条件の全探索では当てはまりませんでした。')
				rfs('>代わりに似たものを表示させます。')

				ans_main_t3.one_ans(category_ans,results,count_row_start)
				ans_main_t3.yes_or_no_one(results[0]['data'],count_row_start)

			#回答候補が8個以下の時
			elif ans_count <= 8:
				rfs('>条件の全探索では当てはまりませんでした。')
				rfs('>代わりに似たものを表示させます。')

				ans_main_t3.some_ans(category_ans,results,ans_count,count_row_start)
				ans_main_t3.yes_or_no_some(results,ans_count,count_row_start)

			#回答候補が8個以上の時
			elif ans_count  >8:
				#追加質問を行う。
				rfs('>大量の回答候補が見つかりました。')
				#追加質問をした回数をカウントする変数へ+1
				add_q_count += 1

				#k3システムから"最重要キーワード"を取得してくる
				key = k3.get_wanting_category()
				
				#whereの場合のみ、whatのリストに追加して情報検索部に投げる
				if key == 'where':
					data['what'].extend(add_q_main.make_q(key))
				else:
					data[key].extend(add_q_main.make_q(key))
			
				rfs('----- もう一度検索します。 -----')
				results = ans_main_t3.look_k3(data)
			
				ans_main_t3.anser(data,category_ans,add_q_count,results,count_row_start)
