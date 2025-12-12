from repository import Repository

class LinkService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_original_url(self, short_code: str):
        try:
            obj = self.repository.get_url(short_code)
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
