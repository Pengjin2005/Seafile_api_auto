import requests
from urllib.parse import quote
from urllib.parse import urljoin

class link_gen:
    def __init__(self, token):
        self.headers = {
            "accept": "application/json",
            "authorization": f"""Token {token}""",
        }

        self.base_url = "https://box.nju.edu.cn/api/v2.1/via-repo-token/dir/"
        self.base_download = "https://box.nju.edu.cn/api/v2.1/via-repo-token/download-link/"

    def get_files(self, folder_path):
        '''Get all files in the folder_path'''
        file_url = quote(folder_path, safe='')
        file_url = "?path=" + file_url

        url = urljoin(self.base_url, file_url)
        response = requests.get(url, headers=self.headers).json()
        name_lst = []
        for item in response["dirent_list"]:
            str = item["name"]
            name_lst.append(str)
        return name_lst

    def get_link(self, file_path):
        '''Get the link of the file at file_path'''
        file_url = quote(file_path, safe='')
        file_url = "?path=" + file_url

        url = urljoin(self.base_download, file_url)
        response = requests.get(url, headers=self.headers)
        return response.text

    def get_all_links(self, folder_path):
        '''Get links of all the files in the folder_path'''
        file_lst = self.get_files(folder_path)
        ans_lst = []
        for file in file_lst:
            file_url = quote(folder_path+'/'+file, safe="")
            file_url = "?path=" + file_url
            url = urljoin(self.base_download, file_url)
            # print(url+'\n')
            response = requests.get(url, headers=self.headers)
            ans_lst.append(response.text)
        return ans_lst

if __name__ == "__main__":
    test = link_gen("e86e560e3327a3022ed2f38f58f9b66af706ae68")
    print(test.get_all_links("/归档"))
