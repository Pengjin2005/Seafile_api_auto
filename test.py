import requests
from urllib.parse import quote
from urllib.parse import urljoin

# file_path = "/归档"
# file_url = quote(file_path, safe='')
# file_url = "?path=" + file_url

# base_url = "https://box.nju.edu.cn/api/v2.1/via-repo-token/dir/"

# url = urljoin(base_url, file_url)

url = "https://box.nju.edu.cn/api/v2.1/multi-share-links/?path=%E5%BE%80%E5%B9%B4%E5%8D%B7/%E5%BD%92%E6%A1%A3"


headers = {
    "accept": "application/json",
    "authorization": "Token d7751374bd48a96de2ba83c51762355917efb058",
}

# response = requests.get(url, headers=headers).json()
# name_lst = []
# for item in response["dirent_list"]:
#     str = item["name"]
#     name_lst.append(str)

# print(name_lst)

response = requests.post(url, headers=headers)
print(response.text)


# url = "https://box.nju.edu.cn/api/v2.1/via-repo-token/download-link/?path=16%E5%B9%B4%E7%A6%BB%E6%95%A3%E6%95%B0%E5%AD%A6%E6%9C%9F%E4%B8%AD%E7%AD%94%E6%A1%88%202.pdf"
