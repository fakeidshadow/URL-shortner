from repository import Repository
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Tehran')

class LinkService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def create_short_link(self, url: str):
        try:
            url_id = self.repository.get_url_id(url)
            if url_id is not None:
                return 208, url_id

            short_code = self.repository.generate_code()
            ct = datetime.now(tz)

            id = self.repository.add(url, short_code, str(ct))

            return 201, id
        except:
            return (500,)


    def delete_link(self, code: str):
        try:
            obj = self.repository.get_Url_by_code(code)

            self.repository.delete(obj)
            return 200
        except:
            return 500
