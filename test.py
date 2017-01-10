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


r_read = record.record_read()
count_row_start = 0
for row in r_read:
	count_row_start +=  1 

record.record_A('----- conversation start   -----')

record.record_A('----- conversation end   -----')

print("以下に履歴を表示します。")


df = pandas.read_csv('conversation_log.csv')
print_record = df[count_row_start:]

print(print_record)

sys.exit()