FILE_PATH = "books/frankenstein.txt"

def get_word_count(text):
   return len(text.split())

def get_letter_count(text):
    dict_of_letters = {}

    words = text.split(" ")
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter.isalpha():
                if letter in dict_of_letters:
                    dict_of_letters[letter] += 1
                else:
                    dict_of_letters[letter] = 1
    return dict_of_letters

def sort_on(dict):
    return dict["number"]

def build_report(text):
    new_list = []
    num_of_words = get_word_count(text)
    dict_of_letters = get_letter_count(text)

    for letter in dict_of_letters:
        new_list.append({"letter": letter, "number": dict_of_letters[letter]})

    new_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {FILE_PATH} ---")
    print(f"{num_of_words} found in this document.")
    print(f"")
    for item in new_list:
        print(f"The {item['letter']} character was found {item['number']}'times.")
    print(f"--- End report ---")

with open(FILE_PATH) as f:
    text = f.read()
    text.split()
    build_report(text)