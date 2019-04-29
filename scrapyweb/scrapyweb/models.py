#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+mysqldb://root@localhost:3306/lagou?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)


