# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる



 
import json
import sys
import os
import codecs
import MeCab
import re
import datetime
import numpy as np 
import pandas
#----外ファイルインポート----
import record



#　入力
st = input('Input: ')


t_hour = re.compile("([0-9]+)(時)")
t_min  = re.compile("([0-9]+)(分)") 
t_min_half = re.compile("([0-9]+)(時半)")

t_get_hour = t_hour.findall(st)
t_get_min  = t_min.findall(st) 
if t_get_hour != []:
	if t_get_min !=[]:
		print( t_get_hour[0][0] + ":" + t_get_min[0][0])
	print( t_get_hour[0][0] + ":00")


t_get_hour_half = t_min_half.findall(st)
if t_get_hour_half !=[]:
	print(t_get_hour_half[0][0] + ":30")
	

'''
t = re.compile("([0-9][0-9]):([0-9][0-9])")
get_time = t.findall(st)
if get_time !=[]:
	print(t.findall(st)[0][0] + ":" + t.findall(st)[0][1])
else:
	print('時間は得られませんでした。')

'''

'''
#時間を表現する数字の取得(import reを使用)
#~~:~~の表現をカバー
t_day = re.compile("([0-9]+)(日)")
print("day")
t_day_get = t_day.findall(st)

if t_day_get != []:
	print(t_day_get[0][0])

t_time = re.compile("([0-9]+)(時)")
print("time")
t_time_get = t_time.findall(st)
if t_time_get != []:
	print(t_time_get[0][0])
'''
