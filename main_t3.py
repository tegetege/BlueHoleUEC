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
import t3.python_mecab as python_mecab
import t3.get_nlc as get_nlc
import t3.get_day as get_day
import t3.record as record
from k3.main import K3


#　入力
st = input('Input: ')
#st = "明日の西野先生の講演会はどこで行われますか？"

#履歴の表示
#"input:"に[履歴]が入力されたら、即履歴を表示して終了
#最後の「履歴」が追加でcsvファイルに書き込まれないように
#この位置指定!!
get_record = re.search('履歴', st)
if get_record :
	dataReader = record.record_read()
	for row in dataReader:
		print(row)
	sys.exit()


#履歴(ユーザー)の作成
#引数'u'はユーザー入力を示す
record.record_make(st,'u')


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



#とりあえずの結果表示
#print (data)

#情報検索部に抽出した情報を受け渡す。
k3 = K3()
k3.set_params(data)

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
