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