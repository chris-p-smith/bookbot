def main():
    path = "books/frankenstein.txt"
    title = get_title(path)
    file_contents = read_books(path)
    word_count = wordcount(file_contents)
    chars_dictionary = letter_count(file_contents)
    chars_list = dict_to_list(chars_dictionary)
    print (f" --- Begin report --- ")
    report_print(title,word_count,chars_list)
    print (" --- End report --- ")

def get_title(path):
    path = path.replace('books/', '')
    return path

def read_books(path):
    with open(path) as f:
        return f.read()

def wordcount(file_contents):
    words = file_contents.split()
    return len(words)

def letter_count(file_contents):
    chars_dictionary = {}
    for c in file_contents:
        lowercase = c.lower()
        if lowercase in chars_dictionary:
            chars_dictionary[lowercase] += 1
        else:
            chars_dictionary[lowercase] = 1
    return chars_dictionary

def dict_to_list(chars_dictionary):
    char_list = []
    for c in chars_dictionary:
        char_list.append({"char": c, "num": chars_dictionary[c]})    
    char_list.sort(reverse=True, key=sort_on)
    return (char_list)

def sort_on(d):
    return d["num"]

def report_print(title,word_count,chars_dictionary):
    print (f"Title: {title}")
    print (f"{word_count} words found in document.")

    for char in chars_dictionary:
        if char["char"].isalpha():
            print (f"Letter '{char["char"]}' found {char["num"]} times")

main()