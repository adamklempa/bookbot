def get_word_count(path_to_book):
    words = get_book_text(path_to_book).split()
    word_count = len(words)
    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(path_to_book):
    book_text = get_book_text(path_to_book)
    character_dict = {}
    text_list = list(book_text.lower())
    for letter in text_list:
        if letter in character_dict:
            character_dict[letter] += 1
        else: 
            character_dict[letter] = 1

    return character_dict


            

