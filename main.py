from stats import word_count, char_count, sorted_dictionary

def main():
    book = "books/frankenstein.txt"
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