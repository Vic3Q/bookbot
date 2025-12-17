import os
from collections import Counter

def get_book_text(path):
    path = os.path.expanduser(path)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def count_distinct_letters(text):
    text = text.lower()
    licznik = Counter(text)
    return licznik

def sorter(litery, sciezka, slowa):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sciezka, "...")
    print("----------- Word Count ----------")
    print("Found", len(slowa), "total words")
    print("--------- Character Count -------")
    # 1. Convert the input dictionary to a list of dictionaries with specific keys
    list_of_dicts = [{"char": char, "num": count} for char, count in litery.items()]
    
    # 2. Sort the list
    # key: tells Python to sort based on the 'num' value
    # reverse=True: ensures the highest numbers come first
    list_of_dicts.sort(key=lambda item: item["num"], reverse=True)
    
    # 3. Print the sorted results
    for item in list_of_dicts:
        print(item["char"], ":", item["num"])
    print("============= END ===============")
