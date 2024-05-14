import requests
import re
import sys
import json
from urllib.parse import quote
from urllib.parse import urljoin


class FileLink:
    def __init__(self, token):
        """Initialize the class with the token of the NJU Box"""
        self.headers = {
            "accept": "application/json",
            "authorization": f"""Token {token}""",
        }

        self.base_url = "https://box.nju.edu.cn/api/v2.1/via-repo-token/dir/"
        self.base_download = (
            "https://box.nju.edu.cn/api/v2.1/via-repo-token/download-link/"
        )
        self.folder_download = "https://box.nju.edu.cn/api/v2.1/multi-share-links/"

    @staticmethod
    def is_file(str):
        pattern = r"^.+\.+.+$"
        return re.match(pattern, str)

    def get_sub(self, type,folder_path=""):
        """type file or folder"""
        file_url = quote(folder_path, safe="")
        file_url = "?path=" + file_url

        try:
            url = urljoin(self.base_url, file_url)
            response = requests.get(url, headers=self.headers).json()
            name_lst = []
            for item in response["dirent_list"]:
                str = item["name"]
                name_lst.append(str)
            ans = []
            if type == "folder":
                return [item for item in name_lst if not self.is_file(item)]
            elif type == "files":
                return [item for item in name_lst if self.is_file(item)]
            else:
                raise ValueError("Unvalid type")
        except Exception as error:
            print(error, file=sys.stderr)
            return response.get("error_msg")

    def get_all_files(self, file_path=""):
        """Get all files in the repo"""
        ans = {}
        for file in self.get_sub("files", file_path):
            ans[file] = self.get_link(file_path + "/" + file)
        for folder in self.get_sub("folder", file_path):
            ans = {**ans, **self.get_all_files(file_path + "/" + folder)}
        return ans

    def get_link(self, file_path):
        """Get the link of the file at file_path"""
        file_url = quote(file_path, safe="")
        file_url = "?path=" + file_url

        try:
            url = urljoin(self.base_download, file_url)
            response = requests.get(url, headers=self.headers)
            return response.text
        except Exception as error:
            print(error, file=sys.stderr)
            return response.get("error_msg")

    def get_all_links(self, folder_path):
        """Get links of all the files in the folder_path"""
        file_lst = self.get_files_lst(folder_path)
        ans_lst = []
        try:
            for file in file_lst:
                file_url = quote(folder_path + "/" + file, safe="")
                file_url = "?path=" + file_url
                url = urljoin(self.base_download, file_url)
                # print(url+'\n')
                response = requests.get(url, headers=self.headers).text
                response = response[1:-1]
                ans_lst.append(response)
            return ans_lst
        except Exception as error:
            print(error, file=sys.stderr)
            return response.get("error_msg")


if __name__ == "__main__":
    test = FileLink("e86e560e3327a3022ed2f38f58f9b66af706ae68")
    ans = test.get_all_files()
    # ans = test.get_sub("files")
    # ans = test.get_link("归档/16年离散数学期中答案.pdf")
    print(ans)
