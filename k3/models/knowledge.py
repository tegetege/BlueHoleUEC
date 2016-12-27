# coding:utf-8

from datetime import datetime
from sqlalchemy import (
    Column,
    VARCHAR,
    DATETIME,
)
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Knowledge(Base):
  __tablename__ = 'knowledges'

  # unsinged=True を利用する場合
  # sqlalchemy.dialects.mysql.BIGINT を利用する
  id = Column(BIGINT, primary_key=True)
  # length は必須ではない
  title = Column(VARCHAR(length=255))
  what = Column(VARCHAR(length=255))
  when_time = Column(VARCHAR(length=255))
  when_day = Column(VARCHAR(length=255))
  who = Column(VARCHAR(length=255))
  how_time = Column(VARCHAR(length=255))
  where = Column(VARCHAR(length=255))
  created_at = Column(VARCHAR(length=50))
  updated_at = Column(VARCHAR(length=50))

  # __init__ や __repr__ を定義すると便利だが、省略

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'what': self.what,
      'when_time': self.when_time,
      'when_day': self.when_day,
      'who': self.who,
      'how_time': self.how_time,
      'where': self.where,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
    }
  