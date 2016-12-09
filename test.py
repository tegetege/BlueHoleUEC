#小さいモジュール単体でテストをするためのpythonファイル

#!/usr/bin/env python
#　coding: utf-8


#pythonにて時間の数字の抜き出し

import json
import sys
import re


if data['when_time'] != 'null' :
	print('日付はいつのことでしょうか？')
	print('26日ですか？それとも27日でしょうか？')
	day = input('Input: ')
	d = re.search('\d+',day)
	day = d.group()
	data['when_day']=day

	print(data)



if data['when_time'] != 'null':
	#datetimeの呼び出し
	today = datetime.date.today()
	one_day = datetime.timedelta(days=1)

	day_today = re.search('今日',st)
	if day_today :
		data['when_day']= today.day

	day_tomorrow =re.search('明日',st)
	if day_tomorrow :
		tomorrow = today + one_day
		data['when_day']= tomorrow.day



