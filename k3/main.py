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
mysql -uroot
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
      pprint(key)
      if key in params:
        self.params[key] = params[key]
      else:
        raise ValueError('%sが存在しません' % key)
      
    
    self.category = params['category']


  def __generate_query(self):
    query = self.session.query(Knowledge)
    
    pprint(self.params)

    if self.mode == self.MODE_STR['and']: # AND検索
      for key in self.params.keys():
        print('AND')
        if self.params[key] and self.params[key] != 'null':
          query = query.filter(getattr(Knowledge, key) == self.params[key])
    elif self.mode == self.MODE_STR['or']: # OR検索
      or_str = (Knowledge.id == '')
      for key in self.params.keys():
        print('OR')
        if self.params[key] and self.params[key] != 'null':
          or_str |= getattr(Knowledge, key) == self.params[key]
      query = query.filter(or_str)

  
    return query


  def to_dict(self, result):
    return list(map(lambda n:n.to_dict(), result)) # 結果を辞書に変換

  """
  辞書形式の情報を要素とするリストを返します。
  何も結果がなければ空のリストを返します。
  [{'created_at': None,
  'how_time': '1時間',
  'id': 3,
  'title': '説明会',
  'updated_at': None,
  'what': '説明会',
  'when_day': '17',
  'when_time': '11',
  'where': '講堂',
  'who': '教務課'}]
  """
  def search(self):
    query = self.__generate_query()
    try:
      result = self.to_dict(query.all())
    except:
      raise Exception('データベースに接続できません' % key)
    
    if len(result) == 0:
      self.mode = self.MODE_STR['or']
      query = self.__generate_query()
      result = self.to_dict(query.all())
      
#    return_hash = {
#      'answer': [],
#      'data': result
#    }
#    for value in result:
#      pprint(value)
#      return_hash['answer'].append(value[str(self.category)])
    
#    pprint(self.params)
    pprint(result)
    return result

