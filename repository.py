from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models
from datetime import datetime
import pytz
import string
import random

tz = pytz.timezone('Asia/Tehran')


engine = create_engine('postgresql+psycopg2://postgres:sec123@localhost:5432/url_db', echo=False)

models.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

def check_code_exists(code:str) -> bool:
    """
    :param code:
    :return: True if code exists else False
    """
    return session.query(models.Url).filter_by(code=code).one_or_none() is not None

def get_url_id(url:str) -> int | None:
    """
    :param url:
    :return: id if exists else None
    """
    url = session.query(models.Url).filter_by(address=url).one_or_none()
    return url.id if url is not None else None

def get_code(code:str) -> int | None:
    """
    :param code:
    :return: url object if exists else None
    """
    return session.query(models.Url).filter_by(code=code).one_or_none()


def generate_code(length:int=6) -> str:
    """
    :param length: len short code
    :return: unique short code
    """
    alphabet = string.ascii_letters + string.digits
    code = ''.join(random.choices(alphabet, k=length))
    while check_code_exists(code):
        code = ''.join(random.choices(alphabet, k=length))
    return code

def add(url:str) -> tuple[int, int] | tuple[int]:
    """
    :param url:
    :return: tuple of status code and [id]
    status code: 201 for add and 208 for exists already
    [id] : new id if url not exists else return old id
    """
    try:
        url_id = get_url_id(url)
        if url_id is not None:
            return 208, url_id

        short_code = generate_code()
        ct = datetime.now(tz)

        obj = models.add(
            url=url,
            code=short_code,
            date=str(ct)
        )

        session.add(obj)
        session.commit()


        return 201, obj.id
    except:
        return (500,)



def delete(code:str) -> int:
    try:
        obj = get_code(code)
        if obj is None:
            return 404

        session.delete(obj)
        return 200
    except:
        return 500
