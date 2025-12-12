from repository import Repository
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Tehran')

class LinkService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_original_url(self, short_code: str):
        try:
            obj = self.repository.get_Url_by_code(short_code)
            if obj is None:
                return 404,
            return 302, str(obj.address)
        except:
            return 500,

    def get_all_links(self):
        all_urls = self.repository.get_all_urls()
        try:
            ans:tuple[dict[str:str]] = tuple()
            for url in all_urls:
                ans += (
                    {
                    "address":url.address,
                    "code":url.code,
                    "date":url.date
                    }
                    ,
                )

            return 200, ans
        except:
            return 500,

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
            if obj is None:
                return 404
            self.repository.delete(obj)
            return 200
        except:
            return 500
