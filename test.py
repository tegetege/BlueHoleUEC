# coding: utf-8
#!/usr/bin/env python

#python のバージョン指定：python 3.5.0
#(条件)MeCabをpythonから利用することができる



 
import record


from k3.main import K3


#入出力を記録
rfs = record.record_for_s

ans_what = '講演会'

rfs(ans_what + 'です。','s')
