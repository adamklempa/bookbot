from stats import get_word_count, count_characters
def main():
    book_path="books/frankenstein.txt"
    word_count_text = f"{get_word_count(book_path)} words found in the document"
    print(word_count_text)
    print(count_characters(book_path))


main()