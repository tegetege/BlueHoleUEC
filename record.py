# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#履歴の作成、保存、展開をするコードファイル


import csv

#履歴を作成するモジュール


#開始&終了フラグの書き込み
def record_A(text):
	st = text +','+''+ '\n'
	#テキストモードでファイルをオープンo-punn
	font = open('conversation_log.csv','a')
	font.write(st)
	font.close()


#システム出力を履歴登録
def record_for_s(text):
	st = text + ',' + 's' +'\n'
	#テキストモードでファイルをオープンo-punn
	font = open('conversation_log.csv','a')
	font.write(st)
	font.close()
	print(text)



#ユーザー入力を履歴登録
def record_for_u(text):
	st = text + ',' + 'u' +'\n'
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



