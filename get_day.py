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

	day_today = re.search('今日|本日|これから',text)
	if day_today :
		return today
		#return today.day

	day_tomorrow =re.search('明日',text)
	if day_tomorrow :
		#tomorrow = today + one_day
		tomorrow = today + 1
		#return tomorrow.day
		return tomorrow

	day_after_tomorrow =re.search('あさって|明後日',text)
	if day_after_tomorrow :
		#tomorrow = today + two_day
		day_after_tomorrow = today + 2
		#return tomorrow.day
		return day_after_tomorrow