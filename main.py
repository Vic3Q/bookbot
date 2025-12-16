import os

def get_book_text(path):
    path = os.path.expanduser(path)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

book_path = "~/workspace/github.com/Vic3Q/bookbot/books/frankenstein.txt"
book_text = get_book_text(book_path)
print(book_text)
