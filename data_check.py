# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#ユーザーの間違え(勘違い)を指摘するプログラム
#卒研優先で、開発中断(1/27)

import sys
from k3.main import K3


def check(data,results):

	for result in results:
		check_data ={,
		   'where'    :[],
		   'who'      :[],
		   'when_time':[],
		   'when_day' :[]}

		count = 0
		#回答候補とユーザー入力の相違を検知する
		if result['data']['where'] != data['where']:
			if data['where']!= []:
				check_data['where'] == '1'
				count +=  1 
		if result['data']['when_day'] != data['when_day']:
			if data['when_day']!= []:
				check_data['when_day'] == '1'
				count +=  1 
		if result['data']['when_time'] != data['when_time']:
			if data['when_time']!= []:
				check_data['when_time'] == '1'
				count +=  1 
		if result['data']['who'] != data['who']:
			if data['who']!= []:
				check_data['who'] == '1'
				count +=  1 

		#回答候補とユーザ入力との相違が一つの時、確認機能を発動する。
		if count == 1:
			if 	check_data['where'] != []:
				print('場所をお間違いではないでしょうか？')
				print('タイトル'  +result['data']['title'])
				print('日にち：'  + result['data']['when_day'])
				print('開催時間：'+ result['data']['when_time'])
				print('主催者：'  + result['data']['who'])
				print('これではないでしょうか？(yes/no)')
			if check_data['when_day'] !=[]:
				print('日付をお間違いではないでしょうか？')
				print('タイトル'  +result['data']['title'])
				print('日にち：'  + result['data']['when_day'])
				print('開催時間：'+ result['data']['when_time'])
				print('主催者：'  + result['data']['who'])
				print('これではないでしょうか？(yes/no)')
			if check_data['when_time'] !=[]:
				print('時間をお間違いではないでしょうか？')
				print('タイトル'  +result['data']['title'])
				print('日にち：'  + result['data']['when_day'])
				print('開催時間：'+ result['data']['when_time'])
				print('主催者：'  + result['data']['who'])
				print('これではないでしょうか？(yes/no)')
			if check_data['who'] !=[]:
				print('主催者(登壇者)をお間違いではないでしょうか？')
				print('タイトル'  +result['data']['title'])
				print('日にち：'  + result['data']['when_day'])
				print('開催時間：'+ result['data']['when_time'])
				print('主催者：'  + result['data']['who'])
				print('これではないでしょうか？(yes/no)')

'''
		if result['data']['where'] == data['where']:
			#日付が異なっている時
			if data['when_day'] != []:
				if result['when_day'] != data['when_day']:
					print('日付をお間違いではないでしょうか？')
					print('タイトル'  +result['data']['title'])
					print('日にち：'  + result['data']['when_day'])
					print('開催時間：'+ result['data']['when_time'])
					print('主催者：'  + result['data']['who'])
					print('これではないでしょうか？(yes/no)')
			#時間が異なっている時
			if data['when_time'] != []:
				if result['when_time'] != data['when_time']:
					print('時間をお間違いではないでしょうか？')
					print('タイトル'  +result['data']['title'])
					print('日にち：'  + result['data']['when_day'])
					print('開催時間：'+ result['data']['when_time'])
					print('主催者：'  + result['data']['who'])
					print('これではないでしょうか？(yes/no)')
			#主催者を間違えている時
			if data['who'] != []:
				if result['who'] != data['who']:
					print('主催者(登壇者)をお間違いではないでしょうか？')
					print('タイトル'  +result['data']['title'])
					print('日にち：'  + result['data']['when_day'])
					print('開催時間：'+ result['data']['when_time'])
					print('主催者：'  + result['data']['who'])
					print('これではないでしょうか？(yes/no)')

		if result['data']['when_day'] == data['when_day']:

		if result['data']['when_time'] == data['when_time']:

		if result['data']['who'] == data['who']:
'''
