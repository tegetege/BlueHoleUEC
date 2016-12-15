# coding:utf-8

"""
brew update
brew install mysql
unset TMPDIR
mysql_install_db --verbose --user=`whoami` --basedir="$(brew --prefix mysql)" --datadir=/usr/local/var/mysql --tmpdir=/tmp
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
k3 = K3();

# 検索要求の受け渡し
k3.set_params(data);

"""

import sqlalchemy

class K3:

  def __init__(self, debug = False):
    self.debug = (debug == True)
    
    url = 'mysql+pymysql://k3:@localhost/k3?charset=utf8'
    self.engine = sqlalchemy.create_engine(url, echo=True)
    
  """
  params = {
    'what': 'null',
    'when_time': 'null',
    'when_day': None,
    'who': 'null',
    'how': 'null',
    'where': '講堂',
    'category': 'what'
  }
  形式が違えば例外（TypeError,ValueError）を投げるので例外処理してください
  """
  def set_params(self, params):
    if not isinstance(params, dict): raise TypeError('不正な引数')
    if 'what' not in params: raise ValueError('whatが存在しません')
    if 'when_time' not in params: raise ValueError('when_timeが存在しません')
    if 'when_day' not in params: raise ValueError('when_dayが存在しません')
    if 'who' not in params: raise ValueError('whoが存在しません')
    if 'how' not in params: raise ValueError('howが存在しません')
    if 'where' not in params: raise ValueError('whereが存在しません')
    if 'category' not in params: raise ValueError('categoryが存在しません')
    
    self.params = params
    
        
