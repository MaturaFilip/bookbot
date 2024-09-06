#!/usr/bin/python3
'''
Take text from file and count words and character counts
'''

book_path = "books/frankenstein.txt"

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {book_path} ---")

    # print number of words in a book
    print(f"{count_words(file_contents)} words found in the document.\n")

    # print number of characters in a book
    char_sorted_list = sort_dict(count_characters(file_contents))
    for character in char_sorted_list:
        print(f"The '{character["char"]}' character was found {str(character["num"]).ljust(5)} times")

    print(f"--- End report ---")




# return number of words in a string
def count_words(text):
    words = text.split()
    return len(words)

# return number of characters in a string
def count_characters(text):
    counter = {}
    for i in text.lower():
        if i.isalpha():   # check string
            counter.setdefault(i, 0) # if i is not in dict -> set default 0
            counter[i] += 1
    return counter


def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dicts = [{"char": key, "num": value} for key, value in dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


main(book_path)
