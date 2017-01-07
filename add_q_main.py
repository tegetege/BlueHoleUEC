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


def make_q(key):
	#K３から受け取った最重要キーワード

	if key == 'what':
		print('Key is "what"')
		print('イベント名はご存知ですか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return add_q_ans
		else:
			mecab_noun = python_mecab.mecab_general_noun_get(st)
			return  mecab_noun





	elif key == 'when_time':
		print('Key is "when"')
		print('イベントは何時から始まるかご存知ですか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return add_q_ans
		#時間を表現する数字の取得(import reを使用)
		else:
			t = re.search('\d+',st)
			if t != None:
				time = t.group()
				add_q_ans = [time]
			return add_q_ans


	elif key == 'who':
		print('Key is "who"')
		print('どなたがご出演かご存知ですか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return add_q_ans
		#人名の取得
		else:
			mecab_name = python_mecab.mecab_name_get(st)
			return mecab_name



	elif key == 'where':
		print('どこで行われるかご存知ですか？(わからない場合は"わからない"を入力)')
		#　入力
		st = input('Input: ')

		null_word = re.search('わからない|わかりません',st)
		if null_word :
			add_q_ans = 'null'
			return add_q_ans
		else:
			mecab_where = python_mecab.mecab_general_noun_get(st)
			return mecab_where
