from stats import get_book_text, count_distinct_letters

book_path = "~/workspace/github.com/Vic3Q/bookbot/books/frankenstein.txt"
book_text = get_book_text(book_path)

words = book_text.split()
litery = count_distinct_letters(book_text)
print("Found", len(words), "total words")
print(litery)