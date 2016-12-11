# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

import re
import datetime

def get_day(text):
	#datetimeの呼び出し
	today = datetime.date.today()
	one_day = datetime.timedelta(days=1)

	day_today = re.search('今日|本日|これから',text)
	if day_today :
		return today.day

	day_tomorrow =re.search('明日',text)
	if day_tomorrow :
		tomorrow = today + one_day
		return tomorrow.day