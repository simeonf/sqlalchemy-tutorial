from config import engine, Session
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'  
    id = Column(Integer, primary_key=True) 
    email = Column(String(255))
    is_active = Column(Boolean(), default=True)

