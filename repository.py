from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models
from datetime import datetime
import pytz


tz = pytz.timezone('Asia/Tehran')

engine = create_engine('postgresql+psycopg2://postgres:sec123@localhost:5432/url_db', echo=False)

models.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

class Repository:
    def __init__(self, db):
        self.db = db

    def get_all_urls(self):
        return self.db.query(models.Url).all()
    

    def get_url(self, code:str):
        return self.get_Url_by_code(code)
    
    
