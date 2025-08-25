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

def sort_and_print_dict(path_to_book):
    dict_to_sort = count_characters(path_to_book)
    sorted_lists = []
    for entry in dict_to_sort:
        if entry.isalpha():
            sorted_lists.append({"char": entry, "num": dict_to_sort[entry]})
    sorted_lists.sort(reverse=True, key=sort_on)
    for s in sorted_lists:
        print(f"{s["char"]}: {s["num"]}")

def sort_on(dict):
    return dict["num"]
            

