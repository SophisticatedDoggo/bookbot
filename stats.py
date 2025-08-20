def word_count(file_contents):
    words = file_contents.split()
    words_list = list(words)
    word_count = len(words_list)
    return word_count

def char_count(file_contents):
    words = file_contents
    char_index = {}

    for i in range(0, len(words)):
        character = words[i].lower()
        if character in char_index:
            char_index[character] = char_index[character] + 1
        else:
            char_index[character] = 1
    return char_index

def sort_on(dictionary):
    return dictionary["num"]

def sorted_dictionary(char_index):
    sorted_index = []
    for char, count in char_index.items():
        if char.isalpha():
            dictionary = {
                "char": char, "num": count
            }
            sorted_index.append(dictionary)
    sorted_index.sort(reverse=True, key=sort_on)
    return sorted_index