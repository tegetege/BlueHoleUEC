#!/usr/bin/env python
#　coding: utf-8

# 小俣のコメント（あとで削除してください）

#tnlabのpcにて
#python のバージョン指定：anaconda3-2.5.0

import json
import sys
import codecs
import MeCab
import re
import datetime
#----外ファイルインポート----
import python_mecab
import get_nlc


#　入力
st = input('Input: ')
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

#datetimeの呼び出し
today = datetime.date.today()
one_day = datetime.timedelta(days=1)

day_today = re.search('今日|本日',st)
if day_today :
	data['when_day']= today.day

day_tomorrow =re.search('明日',st)
if day_tomorrow :
	tomorrow = today + one_day
	data['when_day']= tomorrow.day

#履歴の作成
record_user=[]
record_user.append(st)
#履歴の表示
record_print = re.search('履歴の表示',st)
if record_print :
	print(record_user)


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

