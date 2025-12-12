from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Tehran')
import string
import random

engine = create_engine('postgresql+psycopg2://postgres:sec123@localhost:5432/url_db', echo=False)

models.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


class Repository:
    def __init__(self, db):
        self.db = db

    def get_all_urls(self):
        return self.db.query(models.Url).all()

    def get_url(self, code: str):
        return self.get_Url_by_code(code)

    def add(self, url: str, code: str, date: str) -> int:
        """
        :param url:
        :return: object_id
        """
        obj = models.add(
            url=url,
            code=code,
            date=date
        )

        self.db.add(obj)
        self.db.commit()

        return obj.id

    def delete(self, obj: models.Url) -> None:
        self.db.delete(obj)
        self.db.commit()

    def check_code_exists(self, code: str) -> bool:
        """
        :param code:
        :return: True if code exists else False
        """
        return session.query(models.Url).filter_by(code=code).one_or_none() is not None

    def get_url_id(self, url: str) -> int | None:
        """
        :param url:
        :return: id if exists else None
        """
        url = session.query(models.Url).filter_by(address=url).one_or_none()
        return url.id if url is not None else None

    def get_Url_by_code(self, code: str) -> models.Url | None:
        """
        :param code:
        :return: url object if exists else None
        """
        return session.query(models.Url).filter_by(code=code).one_or_none()

    def get_Url_by_id(self, id: int) -> models.Url | None:
        """
        :param code:
        :return: url object if exists else None
        """
        return session.query(models.Url).filter_by(id=id).one_or_none()

    def generate_code(self, length: int = 6) -> str:
        """
        :param length: len short code
        :return: unique short code
        """
        alphabet = string.ascii_letters + string.digits
        code = ''.join(random.choices(alphabet, k=length))
        while self.check_code_exists(code):
            code = ''.join(random.choices(alphabet, k=length))
        return code