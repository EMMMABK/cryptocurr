from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine(r'sqlite:///C:\Users\user\Desktop\cryptocurr//db.sqlite') # Может меняться
base = declarative_base()

class Price(base):
    __tablename__ = 'Price'
    coin = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    price = Column(Integer)

    def __init__(self, coin, price):
        self.coin = coin
        self.price = price
        self.date = datetime.now()


base.metadata.create_all(engine)