import time
import requests
from urllib.parse import quote
from urllib.parse import urljoin

from seatable_api import Base, context
from seatable_api.constants import UPDATE_DTABLE

class link_gen:
    def __init__(self, token):
        '''Initialize the class with the token of the NJU Box'''
        self.headers = {
            "accept": "application/json",
            "authorization": f"""Token {token}""",
        }

        self.base_url = "https://box.nju.edu.cn/api/v2.1/via-repo-token/dir/"
        self.base_download = "https://box.nju.edu.cn/api/v2.1/via-repo-token/download-link/"
        self.folder_download = "https://box.nju.edu.cn/api/v2.1/multi-share-links/"

    def get_files_lst(self, folder_path):
        '''Get all files in the folder_path'''
        file_url = quote(folder_path, safe='')
        file_url = "?path=" + file_url

        try:
            url = urljoin(self.base_url, file_url)
            response = requests.get(url, headers=self.headers).json()
            name_lst = []
            for item in response["dirent_list"]:
                str = item["name"]
                name_lst.append(str)
            return name_lst
        except:
            return response.get('error_msg')

    def get_link(self, file_path):
        '''Get the link of the file at file_path'''
        file_url = quote(file_path, safe='')
        file_url = "?path=" + file_url

        try:
            url = urljoin(self.base_download, file_url)
            response = requests.get(url, headers=self.headers)
            return response.text
        except:
            return response.get('error_msg')

    def get_all_links(self, folder_path):
        '''Get links of all the files in the folder_path'''
        file_lst = self.get_files_lst(folder_path)
        ans_lst = []
        try:
            for file in file_lst:
                file_url = quote(folder_path+'/'+file, safe="")
                file_url = "?path=" + file_url
                url = urljoin(self.base_download, file_url)
                # print(url+'\n')
                response = requests.get(url, headers=self.headers).text
                response = response[1:-1]
                ans_lst.append(response)
            return ans_lst
        except:
            return response.get('error_msg')

def on_update(data, index, *args):
    try:
        print("Updated\n")
        print("Data: " + data + "\n")
    except:
        print("Error\n")


if __name__ == '__main__':
    server_url = context.server_url or "https://table.nju.edu.cn"
    api_token = context.api_token or "85fcdee63a06458873aaefd93a6e9b425ac2d90d"
    base = Base(api_token, server_url)
    base.auth(with_socket_io=True)
    start_time = time.time()

    n_time = time.time()
    base.socketIO.on(UPDATE_DTABLE, on_update)
    base.socketIO.wait()
