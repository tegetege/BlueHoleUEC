# coding:utf-8

"""
brew update
brew install mysql
unset TMPDIR
mysql_install_db --verbose --user=`whoami` --basedir="$(brew --prefix mysql)" --datadir=/usr/local/var/mysql
 # 起動時に MySQL を立ち上げる。
ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents 
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist

mysql.server start
mysql -u root

 # ここから、起動したMySQL上で入力
-- 新しくデータベースを作成する
CREATE DATABASE k3;
-- 新しくユーザーを作成する
CREATE USER 'k3'@'localhost' IDENTIFIED BY 'k3_password';
-- 作成したユーザーに作成したデータベースの操作権限を付与する
GRANT ALL PRIVILEGES ON k3.* TO 'k3'@'localhost';
-- 設定を反映する
FLUSH PRIVILEGES;
EXIT;
 # ここまで、起動したMySQL上で入力

pip install sqlalchemy
pip install PyMySQL

 # DBの内容を簡単に確認するには、MySQLWorkbenchをインストールしてください
 
K3をソースコードで使用する
from k3.main import K3

# k3の読み込み
k3 = K3()

# 検索要求の受け渡し
k3.set_params(data)

# 検索実行
result = k3.search()

"""

from pprint import pprint
from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from operator import itemgetter
Base = declarative_base()

from k3.models.knowledge import Knowledge

class K3:
  
  MODE_STR = {
    'and': 0,
    'or': 1
  }

  def __init__(self, debug = False):
    self.debug = (debug == True)
    
    self.engine = create_engine('mysql+pymysql://k3:k3_password@localhost/k3?charset=utf8', echo=True)
    Session = sessionmaker(bind=self.engine)
    self.session = Session()
    
    self.mode = self.MODE_STR['and']
    self.category = 'what'

    self.params = {
      'what': None,
      'when_time': None,
      'when_day': None,
      'who': None,
      'how_time': None,
      'where': None
    }

  """
  params = {
    'what': 'null',
    'when_time': 'null',
    'when_day': None,
    'who': 'null',
    'how_time': 'null',
    'where': '講堂',
    'category': 'what'
  }
  形式が違えば例外（TypeError,ValueError）を投げるので例外処理してください
  """
  def set_params(self, params):
#    params = {
#      'what': 'null',
#      'when_time': 'null',
#      'when_day': None,
#      'who': 'null',
#      'how_time': 'null',
#      'where': '講堂',
#      'category': 'what'
#    }
    if not isinstance(params, dict): raise TypeError('不正な引数')

    for key in self.params.keys():
      if key == 'category': continue
      if key in params:
        if params[key] and params[key] != 'null':
          self.params[key] = params[key]
      else:
        raise ValueError('%sが存在しません' % key)
      
    
    self.category = params['category']


  def __generate_queries(self):
    pattern = []
    queries = []
    n = len(self.params)
    keys = list(self.params.keys())

    for i in range(1, pow(2, n)):
      s = "%0" + str(n) + "d"
      pattern.append(s % int(format(i, 'b')))

    for i in pattern:
      query = self.session.query(Knowledge)
      count = 0
      for j, v in enumerate(list(i)[::-1]):
        if v == "1" :
          if self.params[keys[j]] == None: continue
          query = query.filter(getattr(Knowledge, keys[j]).like("%%%s%%" % self.params[keys[j]]))
          count += 1
      if count: queries.append({'query': query, 'count': count})

    pprint(self.params)
#    query = self.session.query(Knowledge)
#    if self.mode == self.MODE_STR['and']: # AND検索
#      for key in self.params.keys():
#        print('AND')
#        if self.params[key] and self.params[key] != 'null':
#          query = query.filter(getattr(Knowledge, key) == self.params[key])
#    elif self.mode == self.MODE_STR['or']: # OR検索
#      or_str = (Knowledge.id == '')
#      for key in self.params.keys():
#        print('OR')
#        if self.params[key] and self.params[key] != 'null':
#          or_str |= getattr(Knowledge, key) == self.params[key]
#      query = query.filter(or_str)

  
    return queries


  def to_dict(self, result):
    return list(map(lambda n:n.to_dict(), result)) # 結果を辞書に変換

  """
  辞書形式の情報を要素とする'data'と、信頼度を表す'reliability'を要素として持つ辞書を列挙するリストを返します。
  何も結果がなければ空のリストを返します。
  [{'data': {'created_at': None,
             'how_time': '1時間',
             'id': 5,
             'title': '西野教授の模擬講義',
             'updated_at': None,
             'what': '模擬講義（西野教授）',
             'when_day': '17',
             'when_time': '14',
             'where': '講堂',
             'who': '西野哲郎'},
    'reliability': 64},
   {'data': {'created_at': None,
             'how_time': '3時間',
             'id': 1,
             'title': '講演会',
             'updated_at': None,
             'what': '講演会',
             'when_day': '17',
             'when_time': '13',
             'where': '東3-501',
             'who': '西野教授'},
    'reliability': 16}]
  """
  def search(self):
    results = []
    queries = self.__generate_queries()
    try:
      for query in queries:
        result = self.to_dict(query['query'].all())
        results.extend(list(map(lambda n:{'data': n, 'count': query['count']}, result)))
    
#        if len(result) == 0:
#          self.mode = self.MODE_STR['or']
#          query = self.__generate_query()
#          result = self.to_dict(query.all())
        
    except:
      raise Exception('データベースに接続できません' % key)
    
    results_uniq = []
    data = []
    reliabilities = []
    for result in results:
      if result['data'] not in data:
        data.append(result['data'])
        reliabilities.append(result['count'])
      else:
        idx = data.index(result['data'])
        reliabilities[idx] += result['count']
      
    
    for idx, item in enumerate(data):
      results_uniq.append({'data': item, 'reliability': reliabilities[idx]})
      
    results_uniq.sort(key=itemgetter('reliability'), reverse=True)
    
    pprint(results_uniq)
    return results_uniq

