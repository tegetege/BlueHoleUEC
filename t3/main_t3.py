# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

'''
追加学習が必要な質問集
・今夜8時に始まるイベントは何ですか？

'''

import json
import sys
import codecs
import MeCab
import re
import datetime
#----外ファイルインポート----
import python_mecab
import get_nlc
import get_day
import record
from ..k3.main import K3


#　入力
st = input('Input: ')


#履歴の表示
#"input:"に[履歴]が入力されたら、即履歴を表示して終了
#最後の「履歴」が追加でcsvファイルに書き込まれないように
#この位置指定!!
get_record = re.search('履歴', st)
if get_record :
	dataReader_user = record.record_user_read()
	for row in dataReader_user:
		print(row)
	dataReader_sys  = record.record_sys_read()
	for row in dataReader_sys:
		print(row)
	sys.exit()


#履歴(ユーザー)の作成
#引数'u'はユーザー入力を示す
record.record_make_user(st,'u')


#データを格納する辞書の作成
data ={'category' :'null',
	   'what'     :'null',
	   'where'    :'null',
	   'who'      :'null',
	   'when_time':'null',
	   'when_day' :'null',
	   'how'      :'null'}


#　get_nlcからカテゴリータグの取得
category_ans = get_nlc.nlc_0(st)
category ='カテゴリー: '
print( category + category_ans)
data['category']=category_ans

if category_ans != 'what':
	#python_mecab.pyのmecab関数を利用
	#一般(固有)名詞の取得
	mecab_noun = python_mecab.mecab_general_noun_get(st)
	data['what']=mecab_noun

if category_ans != 'where':
	#場所名詞の取得
	mecab_where = python_mecab.mecab_where_get(st)
	data['where']=mecab_where

#人名の取得
mecab_name = python_mecab.mecab_name_get(st)
data['who']=mecab_name[0]


#時間を表現する数字の取得(import reを使用)
t = re.search('\d+',st)
if t != None:
	time = t.group()
	data['when_time']=time

#ユーザー発話から日付情報を獲得してくる
data['when_day'] =  get_day.get_day(st)



'''
if category_ans == 'what':
	print('category is what')

elif category_ans == 'when':
	print('category is when')

elif category_ans == 'who':
	print('category is who')

elif category_ans == 'where':
	print('category is where')


elif category_ans == 'how':
	print('category is how')

else:
	print('category is why')
'''

#とりあえずの結果表示
#print (data)

k3 = K3()
k3.set_params(data)