from seatable_api import Base, context
from seatable_api.constants import UPDATE_DTABLE

class TableCtrl:
    def __init__(self, api_token="caf934f72e577afa78fa03bd3dd8d4ffc8137486"):
        server_url = "https://table.nju.edu.cn"
        self.base = Base(api_token, server_url)
        self.base.auth()

    def if_exists(self, file_name) -> bool:
        query = f""" SELECT * FROM Table1 WHERE file_name = '{file_name}' """
        if self.base.query(query):
            return True
        else:
            return False
    
    def insert(self, file_name, link):
        query = f""" INSERT INTO Table1 (file_name, link) VALUES ('{file_name}', '{link}') """
        self.base.query(query)
