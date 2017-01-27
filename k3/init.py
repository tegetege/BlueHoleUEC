# coding:utf-8
#! /usr/bin/python

# DBの準備
#
# python k3/init.py
#
# ※すでにDBに入っているデータは消えます

__author__ = "k.komata"
__date__ = "$2017/01/27 23:19:41$"

import csv
from pprint import pprint
from sqlalchemy import (
    create_engine,
    not_
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from operator import itemgetter, add
Base = declarative_base()

from models.knowledge import Knowledge

headers = {
 'id': 0,
 'title': 1,
 'what': 2,
 'when_time': 3,
 'when_day': 4,
 'who': 5,
 'how_time': 6,
 'where': 7,
 'parent_id': 8,
 'image': 9,
 'detail': 10
}

engine = create_engine('mysql+pymysql://k3:k3_password@localhost/k3?charset=utf8', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(Knowledge)

knowledges = []


# ファイルを読み込みモードでオープン
with open('./data/data.csv', 'r') as f:
 
  reader = csv.reader(f) # readerオブジェクトを作成
  header = next(reader)  # 最初の一行をヘッダーとして取得
 
  print(header)  # ヘッダーをスペース区切りで表示
  
  # 行ごとのリストを処理する
  for row in reader:
    knowledge = Knowledge(
      id = row[headers['id']],
      title = row[headers['title']],
      what = row[headers['what']] if row[headers['what']] != '' else None,
      when_time = row[headers['when_time']] if row[headers['when_time']] != '' else None,
      when_day = row[headers['when_day']] if row[headers['when_day']] != '' else None,
      who = row[headers['who']] if row[headers['who']] != '' else None,
      how_time = row[headers['how_time']] if row[headers['how_time']] != '' else None,
      where = row[headers['where']] if row[headers['where']] != '' else None,
      parent_id = row[headers['parent_id']] if row[headers['parent_id']] != '' else None,
      image = row[headers['image']] if row[headers['image']] != '' else None,
      detail = row[headers['detail']] if row[headers['detail']] != '' else None
    )
    knowledges.append(knowledge)
    print(row)   # １行ずつスペース区切りで表示
  
  query.delete()
  session.add_all(knowledges)
  session.commit()
  