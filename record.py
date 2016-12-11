# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#履歴の作成、保存、展開をするコードファイル

'''
12/10
日本語でcsvファイルに読み/書きこみする際の文字コードによる
バグをなんとかしないといけない。
"pandas"というメソッドを利用して色々やっている人も
いるけど、実際どうなんでしょう？


'''

import re
import csv
import pandas as pd


def record_make(text,who):
	st = [text,who]
	#w:csvファイルがなければ、新たに作る
	#b:バイナリモードでcsvファイルを開く
	with open('data.csv','wb') as font:
		csv_out = csv.writer(font)
		csv_out.writerows(st)

		print('CSVファイルに書き込めました。')


def record_read():
	with open ('data.csv','rb','utf-8') as fin:
		cin = csv.reader(fin)
		record=[row for row in cin]
		return record




count = 1

while count <= 5:
	text = input('Input: ')	
	record_make(text,'user')
	count += 1


record = record_read()
print(record)

