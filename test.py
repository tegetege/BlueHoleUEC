# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる

import pandas
import sys


df = pandas.read_csv('conversation_log.csv',header = None)
print_record = df[104:]
print(print_record)
sys.exit()
