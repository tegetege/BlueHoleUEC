# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#履歴の作成、保存、展開をするコードファイル


import csv


#履歴を作成するモジュール
def record_make(text,who):
	st = text + ',' + who +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('data.csv','a')
	font.write(st)
	font.close()
	print('----- CSVファイルに記録しました -----')

#履歴を返すモジュール
def record_read():

	f = open('data.csv', 'r')
	dataReader = csv.reader(f)
	return dataReader



