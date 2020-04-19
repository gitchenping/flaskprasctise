#encoding=utf-8

from sqlalchemy import Column, Integer, String, DateTime, BIGINT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine=create_engine("mssql+pymssql://writeuser:ddbackend@10.255.254.195/customer",encoding='utf-8', echo=True)

DBSession = sessionmaker(bind=engine)


Base = declarative_base()

class Customer (Base):
	#指定数据库表之间的关联
	__tablename__ = 'Customers'
     	__table_args__ = {"extend_existing": True}
	#创建字段类型
     	custid=Column(String,primary_key=True)
     	Nickname=Column(String)
     	email=Column(String)
	Mobile_phone=Column(String)


db=DBSession()
