from stats import get_word_count, sort_and_print_dict
def main():
    book_path="books/frankenstein.txt"
    word_count_text = f"Found {get_word_count(book_path)} total words"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ---------")
    print(word_count_text)
    print("--------- Character Count -------")
    sort_and_print_dict(book_path)
    print("============= END ===============")


main()