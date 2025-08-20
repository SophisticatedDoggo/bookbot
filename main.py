import sys
from stats import word_count, char_count, sorted_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        print(sys.argv[1])
    book = sys.argv[1]
    contents = get_books_text(book)
    num_of_words = word_count(contents)
    character_count = char_count(contents)
    sorted_char_count = sorted_dictionary(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_count:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def get_books_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()