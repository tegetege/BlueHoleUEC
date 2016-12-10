# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

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


#　入力
st = input('Input: ')


#履歴の作成
record_user=[]
record_user.append(st)
#履歴の表示
record_print = re.search('履歴の表示',st)
if record_print :
	print(record_user)

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


print (data)

