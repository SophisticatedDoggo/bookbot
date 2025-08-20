from stats import word_count

def main():
    book = "books/frankenstein.txt"
    contents = get_books_text(book)
    num_of_words = word_count(contents)
    print(f"{num_of_words} words found in the document")

def get_books_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()