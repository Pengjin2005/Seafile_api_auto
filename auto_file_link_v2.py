import requests
from urllib.parse import quote
from urllib.parse import urljoin
import json

class Linkgen():
    repo_id = "c3b850d1-c9ba-4372-ad87-fc037f03a587"
    token = "Token d7751374bd48a96de2ba83c51762355917efb058"
    url = "https://box.nju.edu.cn/api/v2.1/share-links/"

    def __init__(self, path = "/入学咨询"):
        self.path = path
        self.payload = {
            "permissions": {
                "can_edit": False,
                "can_download": True,
                "can_upload": True,
            },
            "repo_id": f"""{Linkgen.repo_id}""",
            "path": f"""{path}""",
            # "expire_days": "1",
        }
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": Linkgen.token,
        }

    def check_links(self) -> str:
        '''check if such link already exists'''
        headers = {
            "accept": "application/json",
            "authorization": Linkgen.token,
        }
        url_base = "https://box.nju.edu.cn/api/v2.1/share-links/"
        url_app = f"""?repo_id={Linkgen.repo_id}&path={quote(self.path,safe='')}"""
        url = urljoin(url_base, url_app)
        response = requests.get(url, headers=headers)
        response = json.loads(response.text)[0]
        return response.get('link')

    def get_link(self) -> str:
        '''Get the link of the file at file_path'''
        links = self.check_links()
        if (links != '[]'):
            return links
        else:
            links = requests.post(Linkgen.url, json=self.payload, headers=self.headers).text
            # print(links)
            return links


if __name__ == "__main__":
    linkgen = Linkgen()
    print(linkgen.get_link())