def main():
    path = "books/frankenstein.txt"
    
    file_contents = read_books(path)
    word_count = wordcount(file_contents)
    
    title = get_title(path)
    
    print (f"File {title} has {word_count} words.")

def wordcount(text):
    words = text.split()
    return len(words)

def read_books(book):
    with open(book) as f:
        return f.read()
    
def get_title(file_path):
    file_path = file_path.replace('books/', '')
    return file_path

main()