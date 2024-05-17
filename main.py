from file_link import *
from table_ctrl import *


def insert_all_files(file_base, table_base, file_path=""):
    """Get all files in the repo"""
    ans = {}
    for file in file_base.get_sub("files", file_path):
        table_base.insert(file, file_base.get_link(file_path + "/" + file))
    for folder in file_base.get_sub("folder", file_path):
        insert_all_files(file_base, table_base, file_path + "/" + folder)

def main():
    file = FileLink()
    table = TableCtrl()
    insert_all_files(file, table)


if __name__ == "__main__":
    main()
