# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0

#履歴の作成、保存、展開をするコードファイル


import csv


#履歴を作成するモジュール
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



#履歴を返すモジュール
#今の所ユーザー履歴のみを表示できる
def record_user_read():

	f_u = open('data_user.csv', 'r')
	dataReader = csv.reader(f_u)
	return dataReader
	f_u.close()



def record_sys_read():

	f_s = open('data_sys.csv','r')
	dataReader = csv.reader(f_s)
	return dataReader
	f_s.close()

