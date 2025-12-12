from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata

class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    address = Column(String(100), unique=True)
    code = Column(String(10), unique=True)
    date = Column(String(50))
