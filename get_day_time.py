# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#ユーザーの入力から日付を獲得するプログラム

import re
import datetime

def get_day(text,today):
	#datetimeの呼び出し
	#today = datetime.date.today()
	#one_day = datetime.timedelta(days=1)
	#two_day = datetime.timedelta(days=2)

	#「今日|本日|これから」に反応して日付を得る
	day_today = re.search('今日|本日|これから',text)
	if day_today :
		return today
		#return today.day

	#「明日」に反応して日付を得る
	day_tomorrow =re.search('明日',text)
	if day_tomorrow :
		#tomorrow = today + one_day
		tomorrow = today + 1
		#return tomorrow.day
		return tomorrow
	#「明後日」に反応して日付を得る
	day_after_tomorrow =re.search('あさって|明後日',text)
	if day_after_tomorrow :
		#tomorrow = today + two_day
		day_after_tomorrow = today + 2
		#return tomorrow.day
		return day_after_tomorrow

	#正規表現によって日付を得る
	else:
		t_day = re.compile("([0-9]+)(日)")
		t_day_get = t_day.findall(text)

		if t_day_get != []:
			return t_day_get[0][0]


def get_time(text):
	#正規表現を利用して「~~:~~」の形の時間を得る
	t = re.compile("([0-9][0-9]):([0-9][0-9])")
	get_time = t.findall(text)
	if get_time !=[]:
		#~~:~~の形に形成して返す
		return t.findall(text)[0][0] + ":" + t.findall(text)[0][1]
	
	
	t_hour = re.compile("([0-9]+)(時)")
	t_min  = re.compile("([0-9]+)(分)") 
	t_min_half = re.compile("([0-9]+)(時半)")

	t_get_hour = t_hour.findall(text)
	t_get_min  = t_min.findall(text) 
	if t_get_hour != []:

		if t_get_min !=[]:
			return t_get_hour[0][0] + ":" + t_get_min[0][0]

		return t_get_hour[0][0] + ":00"

	t_get_hour_half = t_min_half.findall(text)
	if t_get_hour_half !=[]:
		return t_get_hour_half[0][0] + ":30"
