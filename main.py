def main():
    book = input("Book Filepath: ")
    contents = get_books_text(book)
    print(contents)

def get_books_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()