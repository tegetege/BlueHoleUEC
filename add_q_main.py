# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#追加質問を生成するプログラム
#K3システムから受け取った"最重要キーワード"によって
#ユーザーへの質問の仕方を変更する



import sys
import re
#----外ファイルインポート----
import python_mecab
import record
import get_day_time

#入出力を記録
rfs = record.record_for_s
rfu = record.record_for_u

def make_q(key):
	#K３から受け取った最重要キーワード

	if key == 'what':
		rfs('>Key is "what"')
		rfs('>イベント名はわかりますか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')
		rfu(st)

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return [add_q_ans]
		else:
			mecab_noun = python_mecab.mecab_general_noun_get(st)
			return  mecab_noun


	elif key == 'when_day':
		rfs('>Key is "when_day"')
		rfs('>イベントは何日に行われるかわかりますか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')
		rfu(st)

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return [add_q_ans]
		#時間を表現する数字の取得(import reを使用)
		else:
			#日付の指定
			today = 25
			return [get_day_time.get_day(st,today)]




	elif key == 'when_time':
		rfs('>Key is "when_time"')
		rfs('>イベントは何時から始まるかわかりますか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')
		rfu(st)

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return [add_q_ans]
		#時間を表現する数字の取得(import reを使用)
		else:
			return [get_day_time.get_time(st)]


	elif key == 'who':
		rfs('>Key is "who"')
		rfs('>どなたがご出演かわかりますか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')
		rfu(st)

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return [add_q_ans]
		#人名の取得
		else:
			mecab_name = python_mecab.mecab_name_get(st)
			return mecab_name

	elif key == 'where':
		rfs('>key is "where"')
		rfs('>どこで行われるかわかりますか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')
		rfu(st)

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return [add_q_ans]
		else:
			mecab_where = python_mecab.mecab_general_noun_get(st)
			return mecab_where

#	elif key == 'how_time':
#		rfs('>key is "how_time"')
#		rfs('>そのイベントは何時間開催される予定かわかりますか？(わからない場合は"わからない"を入力)')
#		#　入力
#		st = input('Input: ')
#		rfu(st)
#
#		null_word = re.search('わからない|わかりません',st)
#		if null_word :
#			add_q_ans = 'null'
#			return [add_q_ans]
#		else:
#			#how_timeを取り出す正規表現が入る予定でした...
#			return 

	elif key == None:
		rfs('>検索結果が絞り込めませんでした。スタッフへ引き継ぎます')
		rfs('>履歴を表示して、システムを終了します')
		record.record_A('----- conversation end   -----')
		#履歴の表示
		df = pandas.read_csv('conversation_log.csv')
		print_record = df[count_row_start:]
		print(print_record)
		sys.exit()

