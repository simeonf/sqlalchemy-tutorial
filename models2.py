from config import engine, Session
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    is_active = Column(Boolean(), default=True)

    def __repr__(self):
      return "<User instance: %(id)s>" % self.__dict__

class Page(Base):
  __tablename__ = 'page'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship(User, primaryjoin=user_id == User.id, backref="pages")
  url = Column(String(255))
  content = Column(Text())

  def __repr__(self):
      return "<Page instance: %(id)s>" % self.__dict__
