# coding: utf-8
#!/usr/bin/env python

import add_q_main
import re 
import sys
import get_day

today = 25

st = input('Input: ')

day =  get_day.get_day(st,today)

print(day)