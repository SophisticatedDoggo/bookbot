from stats import word_count, char_count

def main():
    book = "books/frankenstein.txt"
    contents = get_books_text(book)
    num_of_words = word_count(contents)
    character_count = char_count(contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for k, v in character_count.items():
        print(f"'{k}': {v}")

def get_books_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()