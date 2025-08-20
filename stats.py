def word_count(file_contents):
    words = file_contents.split()
    words_list = list(words)
    word_count = len(words_list)
    return word_count

def char_count(file_contents):
    words = file_contents
    char_index = []

    for i in range(0, len(words)):
        if words[i] in char_count