import sys
from stats import get_word_count, sort_and_print_dict
def main():
    book_path = None
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count_text = f"Found {get_word_count(book_path)} total words"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ---------")
    print(word_count_text)
    print("--------- Character Count -------")
    sort_and_print_dict(book_path)
    print("============= END ===============")


main()