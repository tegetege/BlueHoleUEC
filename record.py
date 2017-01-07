# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#履歴の作成、保存、展開をするコードファイル


import csv

#履歴を作成するモジュール

'''
#ユーザーインプットを記録
def record_make_user(text,who):
	st = text + ',' + who +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('data_user.csv','a')
	font.write(st)
	font.close()
	print('----- ユーザーファイルに記録しました -----')


#システム出力を記録
def record_make_sys(text,who):
	st = text + ',' + who +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('data_sys.csv','a')
	font.write(st)
	font.close()
	print('----- システムファイルに記録しました -----')
'''

def record_A(text):
	st = text + '\n'
	#テキストモードでファイルをオープンo-punn
	font = open('conversation_log.csv','a')
	font.write(st)
	font.close()



def record_for_s(text,who):
	st = text + ',' + who +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('conversation_log.csv','a')
	font.write(st)
	font.close()
	print(text)



def record_for_u(text,who):
	st = text + ',' + who +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('conversation_log.csv','a')
	font.write(st)
	font.close()
	print('----- ログファイルに記録しました -----')




#履歴を返すモジュール

#今の所ユーザー履歴のみを表示できる
def record_read():

	record_csv_open = open('conversation_log.csv', 'r')
	dataReader = csv.reader(record_csv_open)
	return dataReader
	record_csv_open.close()



