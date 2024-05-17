from seatable_api import Base, context
from seatable_api.constants import UPDATE_DTABLE


class TableCtrl:
    def __init__(self, api_token="caf934f72e577afa78fa03bd3dd8d4ffc8137486"):
        server_url = "https://table.nju.edu.cn"
        self.base = Base(api_token, server_url)
        self.base.auth()

    def get_all(self):
        query = "SELECT * FROM Table1"
        return self.base.query(query)

    def if_exists(self, file_name) -> bool:
        query = f""" SELECT * FROM Table1 WHERE 文件名 = '{file_name}' """
        if self.base.query(query):
            return True
        else:
            return False

    def insert(self, file_name, link):
        self.base.append_row("Table1", {"文件名": file_name, "文件外链": link})


if __name__ == "__main__":
    test = TableCtrl()
    test.insert("test", "test")
    print(test.get_all())
