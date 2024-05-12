import requests

url = "https://box.nju.edu.cn/api/v2.1/share-links/"

payload = {
    "permissions": {"can_edit": False, "can_download": True, "can_upload": True},
    "repo_id": "c3b850d1-c9ba-4372-ad87-fc037f03a587",
    "path": "/入学咨询",
    "expire_days": "1",
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Token d7751374bd48a96de2ba83c51762355917efb058",
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)