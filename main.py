import sys
from stats import get_book_text, count_distinct_letters, sorter

print("Usage: python3 main.py <path_to_book>")

sys.exit(1)

book_path = sys.argv[1]
book_text = get_book_text(book_path)

words = book_text.split()
litery = count_distinct_letters(book_text)
#print("Found", len(words), "total words")
#print(litery)
sorter(litery, book_path, words)
