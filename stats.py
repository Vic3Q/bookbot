import os

def get_book_text(path):
    path = os.path.expanduser(path)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content